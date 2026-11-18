import yfinance as yf
import pandas as pd
import numpy as np
import json
from datetime import datetime

# BIST 100 - En çok işlem görenler
SYMBOLS = ["THYAO.IS","ASELS.IS","BIMAS.IS","KCHOL.IS","SAHOL.IS","AKBNK.IS","GARAN.IS","YKBNK.IS","ISCTR.IS","SISE.IS","TUPRS.IS","EREGL.IS","FROTO.IS","TOASO.IS","TCELL.IS","TTKOM.IS","PGSUS.IS","ENKAI.IS","KOZAL.IS","SASA.IS","HEKTS.IS","GUBRF.IS","PETKM.IS","MGROS.IS","AKSEN.IS","ARCLK.IS","DOHOL.IS","KRDMD.IS","VAKBN.IS","HALKB.IS"]

def rsi(series, period=14):
    delta = series.diff()
    gain = delta.where(delta>0,0).rolling(period).mean()
    loss = -delta.where(delta<0,0).rolling(period).mean()
    rs = gain/loss
    return 100 - (100/(1+rs))

def analyze(sym):
    try:
        df = yf.download(sym, period="6mo", interval="1d", progress=False, auto_adjust=True)
        if df.empty or len(df)<30: return None
        if isinstance(df.columns, pd.MultiIndex): df.columns = df.columns.get_level_values(0)
        close = df['Close']
        price = float(close.iloc[-1])
        prev = float(close.iloc[-2])
        ch = round((price/prev-1)*100, 2)
        # Ortalamalar
        ma20 = float(close.rolling(20).mean().iloc[-1])
        ma50 = float(close.rolling(50).mean().iloc[-1])
        ma200 = float(close.rolling(200).mean().iloc[-1]) if len(close)>=200 else ma50
        # RSI
        r = float(rsi(close).iloc[-1])
        # MACD
        ema12 = close.ewm(span=12).mean()
        ema26 = close.ewm(span=26).mean()
        macd = float((ema12-ema26).iloc[-1])
        macd_sig = float((ema12-ema26).ewm(span=9).mean().iloc[-1])
        # Hacim
        vol = float(df['Volume'].iloc[-1])
        vol_avg = float(df['Volume'].rolling(20).mean().iloc[-1])
        vol_ratio = round(vol/vol_avg, 2) if vol_avg else 1
        # Destek / Direnç (son 20 gün)
        support = round(float(df['Low'].tail(20).min()),2)
        resist = round(float(df['High'].tail(20).max()),2)
        # Hedef / Stop
        target = round(price*1.07,2)
        stop = round(price*0.96,2)

        # SKORLAMA - Tam Analiz
        score = 50
        reasons = []
        if price > ma20: score+=8; reasons.append("Fiyat MA20 üstünde ✅")
        else: score-=8; reasons.append("Fiyat MA20 altında ❌")
        if price > ma50: score+=8; reasons.append("Fiyat MA50 üstünde ✅")
        else: score-=8; reasons.append("Fiyat MA50 altında ❌")
        if price > ma200: score+=5; reasons.append("Uzun vade trend YUKARI")
        else: score-=5; reasons.append("Uzun vade trend AŞAĞI")
        if r < 30: score+=12; reasons.append(f"RSI {r:.0f} - Aşırı satılmış, tepki gelebilir")
        elif r < 45: score+=5; reasons.append(f"RSI {r:.0f} - Alım bölgesine yakın")
        elif r > 70: score-=12; reasons.append(f"RSI {r:.0f} - Aşırı alınmış, dikkat!")
        elif r > 60: score-=5; reasons.append(f"RSI {r:.0f} - Yorulma var")
        else: reasons.append(f"RSI {r:.0f} - Nötr")
        if macd > macd_sig: score+=10; reasons.append("MACD AL sinyali verdi")
        else: score-=10; reasons.append("MACD SAT sinyali verdi")
        if vol_ratio > 1.5: score+=7; reasons.append(f"Hacim %{int((vol_ratio-1)*100)} arttı - Güçlü hareket")
        elif vol_ratio < 0.7: score-=3; reasons.append("Hacim düşük - Güçsüz")

        score = max(0, min(100, score))
        if score >= 70: signal="GÜÇLÜ AL 🟢"; action="AL - Kademeli al, stopa uy"
        elif score >= 60: signal="AL 🟢"; action="AL - Küçük miktar dene"
        elif score >= 45: signal="TUT / İZLE 🟡"; action="BEKLE - Destekten almayı düşün"
        elif score >= 30: signal="ZAYIF 🔴"; action="SATMA / ALMA - Düşüşte"
        else: signal="GÜÇLÜ SAT 🔴"; action="SAT / UZAK DUR"

        comment = " | ".join(reasons)
        return {
            "sym": sym.replace(".IS",""), "price": round(price,2), "ch": ch,
            "rsi": round(r,1), "score": score, "signal": signal, "action": action,
            "ma20": round(ma20,2), "ma50": round(ma50,2), "ma200": round(ma200,2),
            "macd": round(macd,2), "vol_ratio": vol_ratio,
            "support": support, "resist": resist, "target": target, "stop": stop,
            "comment": comment
        }
    except Exception as e:
        print(sym, e); return None

stocks=[]
for s in SYMBOLS:
    a=analyze(s)
    if a: stocks.append(a); print(a["sym"], a["price"], a["signal"])

stocks=sorted(stocks, key=lambda x: x["score"], reverse=True)
out={"updated": datetime.now().strftime("%H:%M"), "stocks": stocks}
with open("data.json","w",encoding="utf-8") as f: json.dump(out,f,ensure_ascii=False,indent=2)
print("OK", len(stocks))