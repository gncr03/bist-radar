import yfinance as yf
import json
import datetime
import time

# BIST 100 - TAM LİSTE
HISSELER = [
"AEFES.IS","AGHOL.IS","AGROT.IS","AHGAZ.IS","AKBNK.IS","AKCNS.IS","AKFYE.IS",
"AKSA.IS","AKSEN.IS","ALARK.IS","ALFAS.IS","ALCAR.IS","ALTNY.IS","ANHYT.IS",
"ANSGR.IS","ARCLK.IS","ARDYZ.IS","ASELS.IS","ASTOR.IS","AYGAZ.IS","BERA.IS",
"BIMAS.IS","BINHO.IS","BRSAN.IS","BRYAT.IS","BTCIM.IS","BUCIM.IS","CANTE.IS",
"CCOLA.IS","CIMSA.IS","CMENT.IS","CVKMD.IS","DOAS.IS","DOHOL.IS","ECILC.IS",
"ECZYT.IS","EGEEN.IS","EKGYO.IS","ENJSA.IS","ENKAI.IS","EREGL.IS","EUREN.IS",
"FROTO.IS","GARAN.IS","GESAN.IS","GLRMK.IS","GUBRF.IS","HALKB.IS","HEKTS.IS",
"ISCTR.IS","ISDMR.IS","ISMEN.IS","ISGYO.IS","KARSN.IS","KCAER.IS","KCHOL.IS",
"KENT.IS","KLRHO.IS","KONTR.IS","KONYA.IS","KOZAA.IS","KOZAL.IS","KRDMD.IS",
"KTLEV.IS","KUYAS.IS","MAGEN.IS","MGROS.IS","MPARK.IS","OBAMS.IS","ODINE.IS",
"OTKAR.IS","OYAKC.IS","PETKM.IS","PGSUS.IS","REEDR.IS","SAHOL.IS","SASA.IS",
"SELEC.IS","SISE.IS","SNGYO.IS","SOKM.IS","TABGD.IS","TAVHL.IS","TCELL.IS",
"TCKRC.IS","THYAO.IS","TKFEN.IS","TOASO.IS","TSKB.IS","TTKOM.IS","TTRAK.IS",
"TUPRS.IS","TURSG.IS","ULKER.IS","VAKBN.IS","VESTL.IS","YKBNK.IS","ZOREN.IS",
"AKSUE.IS","EUPWR.IS","KONKA.IS","PATEK.IS","SMRTG.IS","YEOTK.IS"
]

def rsi_hesapla(prices, period=14):
    if len(prices) < period + 1:
        return 50
    gains=[]; losses=[]
    for i in range(1, len(prices)):
        diff=prices[i]-prices[i-1]
        gains.append(max(diff,0)); losses.append(max(-diff,0))
    avg_gain=sum(gains[-period:])/period
    avg_loss=sum(losses[-period:])/period
    if avg_loss==0: return 100
    rs=avg_gain/avg_loss
    return round(100-(100/(1+rs)),1)

def analiz_yap(sym, df):
    close=df['Close'].tolist()
    volume=df['Volume'].tolist()
    fiyat=round(float(close[-1]),2)
    degisim=round(((close[-1]-close[-2])/close[-2]*100),2) if len(close)>1 else 0
    rsi=rsi_hesapla(close)
    ort_hacim=sum(volume[-20:])/20 if len(volume)>=20 else volume[-1]
    hacim_oran=round(volume[-1]/ort_hacim,2) if ort_hacim else 1
    hacim_durum="Yüksek 🔥" if hacim_oran>1.5 else "Normal" if hacim_oran>0.8 else "Düşük"
    son20=close[-20:]
    destek=round(min(son20)*1.01,2)
    direnc=round(max(son20)*0.99,2)
    skor=50
    if rsi<30: skor+=20
    elif rsi>70: skor-=15
    elif 50<=rsi<=65: skor+=15
    if degisim>1: skor+=15
    elif degisim>0: skor+=5
    elif degisim<-1: skor-=15
    if hacim_oran>1.5 and degisim>0: skor+=10
    skor=max(5,min(95,skor))
    if skor>=75: sinyal="GÜÇLÜ AL"
    elif skor>=60: sinyal="AL"
    elif skor<=25: sinyal="GÜÇLÜ SAT"
    elif skor<=40: sinyal="SAT"
    else: sinyal="TUT"
    hedef=round(fiyat*1.04,2); stop=round(fiyat*0.97,2)
    if sinyal in ["SAT","GÜÇLÜ SAT"]:
        hedef=round(fiyat*1.02,2); stop=round(fiyat*0.94,2)
    return {"sym":sym.replace(".IS",""),"fiyat":fiyat,"degisim":f"%{degisim}","sinyal":sinyal,"rsi":rsi,"hacim":hacim_durum,"hacim_oran":hacim_oran,"skor":skor,"destek":destek,"direnc":direnc,"hedef":hedef,"stop":stop}

sonuclar=[]
for sym in HISSELER:
    try:
        df=yf.download(sym, period="1mo", interval="1d", progress=False, auto_adjust=True)
        if df.empty: continue
        try: df.columns=df.columns.get_level_values(0)
        except: pass
        sonuclar.append(analiz_yap(sym, df))
        print(f"{sym} OK")
        time.sleep(0.3)
    except Exception as e:
        print(f"Hata {sym}: {e}")

simdi=datetime.datetime.utcnow()+datetime.timedelta(hours=3)
data={"Güncellendi":simdi.strftime("%H:%M"),"hisseler":sonuclar}
with open("data.json","w",encoding="utf-8") as f:
    json.dump(data,f,ensure_ascii=False,indent=2)
print(f"OK - {len(sonuclar)} hisse yazıldı")