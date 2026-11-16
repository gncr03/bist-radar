
import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
import time

st.set_page_config(
    page_title="BIST RADAR",
    page_icon="📡",
    layout="wide"
)

st.title("📡 BIST RADAR - Gerçek Veri")
st.caption(
    "Yahoo Finance verileri | Günlük analiz | "
    "Veriler gecikmeli olabilir. Yatırım tavsiyesi değildir."
)

BIST = [
    "THYAO.IS", "ASELS.IS", "TUPRS.IS", "EREGL.IS",
    "SISE.IS", "KCHOL.IS", "BIMAS.IS", "AKBNK.IS",
    "GARAN.IS", "YKBNK.IS", "SAHOL.IS", "PETKM.IS",
    "PGSUS.IS", "ENKAI.IS", "FROTO.IS", "TCELL.IS",
    "TOASO.IS", "EKGYO.IS", "KOZAL.IS", "SASA.IS"
]

@st.cache_data(ttl=300, show_spinner=False)
def veri_cek(sembol, period="3mo"):
    try:
        df = yf.download(
            sembol,
            period=period,
            interval="1d",
            progress=False,
            auto_adjust=False,
            threads=False,
            timeout=20
        )

        if df is None or df.empty:
            return pd.DataFrame()

        if isinstance(df.columns, pd.MultiIndex):
            for level in range(df.columns.nlevels):
                values = df.columns.get_level_values(level)
                if any(
                    col in values
                    for col in ["Open", "High", "Low", "Close", "Volume"]
                ):
                    df.columns = values
                    break

        df = df.loc[:, ~df.columns.duplicated()]
        gerekli = ["Open", "High", "Low", "Close", "Volume"]

        if not all(col in df.columns for col in gerekli):
            return pd.DataFrame()

        df = df[gerekli].copy()

        for col in gerekli:
            df[col] = pd.to_numeric(df[col], errors="coerce")

        df = df.dropna(subset=["Close", "High", "Low"])

        return df

    except Exception:
        return pd.DataFrame()


def rsi_hesapla(series, period=14):
    delta = series.diff()

    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    ort_gain = gain.ewm(
        alpha=1 / period,
        min_periods=period,
        adjust=False
    ).mean()

    ort_loss = loss.ewm(
        alpha=1 / period,
        min_periods=period,
        adjust=False
    ).mean()

    rs = ort_gain / ort_loss.replace(0, float("nan"))

    rsi = 100 - (100 / (1 + rs))

    rsi = rsi.mask((ort_loss == 0) & (ort_gain > 0), 100)
    rsi = rsi.mask((ort_loss == 0) & (ort_gain == 0), 50)

    return rsi


def analiz_yap(sembol):
    df = veri_cek(sembol)

    if len(df) < 30:
        return None

    df["RSI"] = rsi_hesapla(df["Close"])
    df["EMA20"] = df["Close"].ewm(span=20, adjust=False).mean()
    df["EMA50"] = df["Close"].ewm(span=50, adjust=False).mean()

    df["Hacim_Ort"] = df["Volume"].rolling(20).mean()

    df["Hacim_Artis"] = (
        (df["Volume"] / df["Hacim_Ort"].replace(0, float("nan"))) - 1
    ) * 100

    exp1 = df["Close"].ewm(span=12, adjust=False).mean()
    exp2 = df["Close"].ewm(span=26, adjust=False).mean()

    df["MACD"] = exp1 - exp2
    df["Signal"] = df["MACD"].ewm(span=9, adjust=False).mean()

    son = df.iloc[-1]
    onceki = df.iloc[-2]

    if pd.isna(son["RSI"]):
        return None

    fiyat = float(son["Close"])
    onceki_fiyat = float(onceki["Close"])

    if onceki_fiyat == 0:
        return None

    degisim = (fiyat / onceki_fiyat - 1) * 100

    rsi = float(son["RSI"])
    hacim = son["Hacim_Artis"]

    hacim = float(hacim) if pd.notna(hacim) else 0

    sinyal = "NÖTR"

    if rsi < 30:
        sinyal = "RADAR - ALIM BÖLGESİ"

    elif rsi < 40 and hacim > 80:
        sinyal = "İZLE - TOPLANIYOR"

    elif rsi > 70:
        sinyal = "DİKKAT - AŞIRI ALIM"

    elif son["MACD"] > son["Signal"]:
        sinyal = "AL SİNYALİ - MACD"

    elif son["MACD"] < son["Signal"]:
        sinyal = "SAT SİNYALİ - MACD"

    destek = float(df["Low"].tail(20).min())
    direnc = float(df["High"].tail(20).max())

    return {
        "Hisse": sembol.replace(".IS", ""),
        "Fiyat": round(fiyat, 2),
        "Günlük %": round(degisim, 2),
        "RSI": round(rsi, 1),
        "Hacim Artış %": round(hacim, 1),
        "EMA20": round(float(son["EMA20"]), 2),
        "EMA50": round(float(son["EMA50"]), 2),
        "Destek": round(destek, 2),
        "Direnç": round(direnc, 2),
        "Sinyal": sinyal
    }


if "scan_results" not in st.session_state:
    st.session_state.scan_results = None

if st.button("🔄 RADARI TARA - GERÇEK VERİYLE", type="primary"):
    sonuclar = []
    hatalar = []

    progress = st.progress(0)
    durum = st.empty()

    for i, sembol in enumerate(BIST):
        durum.write(f"📊 Analiz ediliyor: {sembol}")

        try:
            sonuc = analiz_yap(sembol)

            if sonuc:
                sonuclar.append(sonuc)
            else:
                hatalar.append(sembol)

        except Exception as e:
            hatalar.append(f"{sembol}: {str(e)}")

        progress.progress((i + 1) / len(BIST))

    st.session_state.scan_results = sonuclar
    st.session_state.scan_errors = hatalar

    durum.empty()
    progress.empty()

    st.cache_data.clear()

    if sonuclar:
        st.success(f"Tarama tamamlandı: {len(sonuclar)} hisse analiz edildi.")
    else:
        st.error("Hiçbir hisseden veri alınamadı.")


sonuclar = st.session_state.scan_results

if sonuclar:

    df_son = pd.DataFrame(sonuclar)

    st.subheader("📈 Piyasa Özeti")

    c1, c2, c3 = st.columns(3)

    c1.metric("Taranan Hisse", len(df_son))
    c2.metric(
        "AL Sinyali",
        int(df_son["Sinyal"].str.contains("AL", regex=False).sum())
    )
    c3.metric(
        "Aşırı Alım",
        int((df_son["RSI"] > 70).sum())
    )

    st.subheader("📡 Hisse Radar Tablosu")

    sinyal_filtre = st.selectbox(
        "Sinyal filtresi",
        ["Tümü", "AL", "SAT", "İZLE", "NÖTR"]
    )

    goster = df_son.copy()

    if sinyal_filtre != "Tümü":
        if sinyal_filtre == "AL":
            goster = goster[
                goster["Sinyal"].str.contains("AL", regex=False)
            ]
        elif sinyal_filtre == "SAT":
            goster = goster[
                goster["Sinyal"].str.contains("SAT", regex=False)
            ]
        elif sinyal_filtre == "İZLE":
            goster = goster[
                goster["Sinyal"].str.contains("İZLE", regex=False)
            ]
        else:
            goster = goster[goster["Sinyal"] == "NÖTR"]

    st.dataframe(
        goster.sort_values("RSI"),
        use_container_width=True,
        hide_index=True
    )

    secilen = st.selectbox(
        "🔍 Detaylı analiz için hisse seç",
        df_son["Hisse"].tolist()
    )

    st.subheader(f"📊 {secilen} Teknik Analizi")

    df_detay = veri_cek(secilen + ".IS", "6mo")

    if not df_detay.empty:

        df_detay["EMA20"] = df_detay["Close"].ewm(
            span=20, adjust=False
        ).mean()

        df_detay["EMA50"] = df_detay["Close"].ewm(
            span=50, adjust=False
        ).mean()

        fig = go.Figure()

        fig.add_trace(go.Candlestick(
            x=df_detay.index,
            open=df_detay["Open"],
            high=df_detay["High"],
            low=df_detay["Low"],
            close=df_detay["Close"],
            name="Mum Grafiği"
        ))

        fig.add_trace(go.Scatter(
            x=df_detay.index,
            y=df_detay["EMA20"],
            name="EMA 20"
        ))

        fig.add_trace(go.Scatter(
            x=df_detay.index,
            y=df_detay["EMA50"],
            name="EMA 50"
        ))

        fig.update_layout(
            height=500,
            xaxis_rangeslider_visible=False,
            template="plotly_dark",
            title=f"{secilen} - 6 Aylık Grafik"
        )

        st.plotly_chart(fig, use_container_width=True)

    if st.session_state.get("scan_errors"):
        with st.expander("⚠️ Veri alınamayan hisseler"):
            st.write(st.session_state.scan_errors)

else:
    st.info("Başlamak için RADARI TARA butonuna bas.")

st.caption(
    "BIST RADAR | Teknik analiz amaçlıdır. "
    "Sinyaller otomatik emir değildir ve yatırım tavsiyesi oluşturmaz."
)
