import yfinance as yf, json
from datetime import datetime, timezone, timedelta
import numpy as np
TR = timezone(timedelta(hours=3))
def now(): return datetime.now(TR).strftime("%H:%M")

TICKS="AEFES,AGHOL,AHGAZ,AKBNK,AKCNS,AKSA,AKSEN,ALARK,ALFAS,ALBRK,ANHYT,ANSGR,ARCLK,ARDYZ,ASELS,ASTOR,BERA,BIMAS,BINHO,BRSAN,BRYAT,BTCIM,CANTE,CCOLA,CIMSA,CWENE,DOAS,DOHOL,ECILC,ECZYT,EGEEN,EGGUB,EKGYO,ENERY,ENJSA,ENKAI,EREGL,EUPWR,FENER,FROTO,GARAN,GENIL,GESAN,GLRMK,GOLTS,GUBRF,HALKB,HEKTS,ISCTR,ISDMR,ISMEN,KARSN,KCAER,KCHOL,KENT,KMPUR,KONTR,KOZAA,KOZAL,KRDMD,KTLEV,MAVI,MGROS,MIATK,MPARK,ODAS,OTKAR,OYAKC,PAHOL,PETKM,PGSUS,SAHOL,SASA,SDTTR,SELEC,SISE,SKBNK,SMRTG,SOKM,TABGD,TAVHL,TCELL,THYAO,TKFEN,TOASO,TSKB,TTKOM,TTRAK,TUPRS,TURSG,ULKER,VAKBN,VESTL,YKBNK,ZOREN,AGROT,AKFYE,ALTNY,CMENT,IEYHO".split(",")

def rsi(c):
    if len(c)<15: return 50
    d=np.diff(c)
    g=np.where(d>0,d,0)[-14:]; l=np.where(d<0,-d,0)[-14:]
    ag=g.mean(); al=l.mean()
    if al==0: return 100
    return round(100-(100/(1+ag/al)),1)

def ema(c,n):
    k=2/(n+1); e=c[0]
    for v in c[1:]: e=v*k+e*(1-k)
    return e

stocks=[]
for t in TICKS:
    try:
        df1=yf.download(t+".IS", period="1d", interval="1m", progress=False)
        if df1.empty: continue
        price=round(float(df1['Close'].values.flatten()[-1]),2)
        df=yf.download(t+".IS", period="6mo", interval="1d", progress=False)
        if df.empty: continue
        c=df['Close'].values.flatten(); v=df['Volume'].values.flatten()
        prev=float(c[-2]) if len(c)>1 else price
        ch=round((price-prev)/prev*100,2)
        ma20=round(float(np.mean(c[-20:])),2); ma50=round(float(np.mean(c[-50:])),2)
        r=rsi(list(c))
        macd=round(ema(list(c),12)-ema(list(c),26),2)
        vol=int(v[-1]); avgvol=int(np.mean(v[-20:]))
        # Tahmini para akisi: hacim x fiyat
        money=round(vol*price/1000000,1) # Milyon TL
        money_trend="GİRİŞ" if vol>avgvol and ch>0 else "ÇIKIŞ" if vol>avgvol and ch<0 else "NÖTR"
        support=round(float(np.min(c[-20:])),2); resist=round(float(np.max(c[-20:])),2)
        # SKOR
        score=50
        if r<30: score+=20
        elif r<40: score+=10
        elif r>70: score-=20
        elif r>60: score-=10
        if price>ma20: score+=10
        if price>ma50: score+=10
        if macd>0: score+=10
        else: score-=10
        if ch>1: score+=5
        if ch<-1: score-=5
        if score>=75: sig="🟢 GÜÇLÜ AL"; yorum="RSI, trend ve MACD aynı anda güçlü. Alıcılar baskın. Destek üstünde kaldıkça yükseliş beklenebilir."
        elif score>=60: sig="🟢 AL"; yorum="Göstergeler pozitife dönüyor. Kademeli alım düşünülebilir, destek altı stop olmalı."
        elif score>=45: sig="🟡 NÖTR / BEKLE"; yorum="Net yön yok. Destek kırılırsa sat, direnç kırılırsa al tarafı güçlenir. Şu an izle."
        elif score>=30: sig="🔴 SAT"; yorum="Göstergeler zayıflıyor. Tepki yükselişleri satış fırsatı olabilir."
        else: sig="🔴 GÜÇLÜ SAT"; yorum="Tüm göstergeler satıcıda. Destek kırılmış, düşüş trendi sürüyor. Uzak dur."
        stocks.append({"sym":t,"price":price,"ch":ch,"rsi":r,"ma20":ma20,"ma50":ma50,"macd":macd,"vol":vol,"avgvol":avgvol,"money":money,"money_trend":money_trend,"support":support,"resist":resist,"score":score,"signal":sig,"comment":yorum,"time":now()})
    except: continue

open("data.json","w",encoding="utf-8").write(json.dumps({"updated":now(),"stocks":stocks},ensure_ascii=False))
print("toplam",len(stocks))