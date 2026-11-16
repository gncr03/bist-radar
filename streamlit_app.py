import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="BIST RADAR", layout="wide")
st.title("📡 BIST RADAR - Gerçek Veri")
st.caption("Veri: Yahoo Finance - 15 dk gecikmeli. Yatırım tavsiyesi değildir.")

BIST = ["THYAO.IS","ASELS.IS","TUPRS.IS","EREGL.IS","SISE.IS","KCHOL.IS","BIMAS.IS","AKBNK.IS","GARAN.IS","YKBNK.IS","SAHOL.IS","PETKM.IS","PGSUS.IS","ENKAI.IS","FROTO.IS","TCELL.IS","TOASO.IS","EKGYO.IS","KOZAL.IS","SASA.IS"]

def rsi_hesapla(series, period=14):
    delta = series.diff()
    gain = (delta.where(delta > 0, 0)).rolling(period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(period).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

if st.button("🔄 RADARI TARA - Gerçek Veriyle"):
    sonuclar = []
    bar = st.progress(0)
    for i, sym in enumerate(BIST):
        try:
            df = yf.download(sym, period="3mo", interval="1d", progress=False)
            if df.empty: continue
            if isinstance(df.columns, pd.MultiIndex):
                df.columns = df.columns.get_level_values(0)
            df['RSI'] = rsi_hesapla(df['Close'])
            df['EMA20'] = df['Close'].ewm(span=20).mean()
            df['EMA50'] = df['Close'].ewm(span=50).mean()
            df['Hacim_Ort'] = df['Volume'].rolling(20).mean()
            df['Hacim_Artis'] = (df['Volume'] / df['Hacim_Ort'] - 1) * 100
            exp1 = df['Close'].ewm(span=12).mean()
            exp2 = df['Close'].ewm(span=26).mean()
            df['MACD'] = exp1 - exp2
            df['Signal'] = df['MACD'].ewm(span=9).mean()
            son = df.iloc[-1]
            onceki = df.iloc[-2]
            fiyat = float(son['Close'])
            degisim = (fiyat / float(onceki['Close']) - 1) * 100
            rsi = float(son['RSI'])
            hacim = float(son['Hacim_Artis'])
            sinyal = "NÖTR"
            if rsi < 30: sinyal = "RADAR - ALIM BÖLGESİ"
            elif rsi < 40 and hacim > 80: sinyal = "İZLE - TOPLANIYOR"
            elif rsi > 70: sinyal = "DİKKAT - AŞIRI ALIM"
            elif float(son['MACD']) > float(son['Signal']): sinyal = "AL SİNYALİ - MACD"
            destek = float(df['Low'].tail(20).min())
            direnc = float(df['High'].tail(20).max())
            sonuclar.append({"Hisse": sym.replace(".IS",""), "Fiyat": round(fiyat,2), "Günlük %": round(degisim,2), "RSI": round(rsi,1), "Hacim Artış %": round(hacim,0), "Destek": round(destek,2), "Direnç": round(direnc,2), "Sinyal": sinyal})
        except: continue
        bar.progress((i+1)/len(BIST))
    if sonuclar:
        df_son = pd.DataFrame(sonuclar).sort_values("RSI")
        st.dataframe(df_son, use_container_width=True, hide_index=True)
        secilen = st.selectbox("Detay için hisse seç", df_son["Hisse"].tolist())
        df_detay = yf.download(secilen+".IS", period="6mo", interval="1d", progress=False)
        if isinstance(df_detay.columns, pd.MultiIndex):
            df_detay.columns = df_detay.columns.get_level_values(0)
        fig = go.Figure()
        fig.add_trace(go.Candlestick(x=df_detay.index, open=df_detay['Open'], high=df_detay['High'], low=df_detay['Low'], close=df_detay['Close'], name="Fiyat"))
        fig.update_layout(height=400, xaxis_rangeslider_visible=False)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Veri çekilemedi, tekrar dene.")
else:
    st.info("Başlamak için butona bas. Borsa kapalıysa son kapanış verisini gösterir.")