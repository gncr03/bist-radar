import yfinance as yf
import json
import datetime

# Takip edilecek hisseler
HISSELER = ["THYAO.IS", "ASELS.IS", "YKBNK.IS", "KCHOL.IS", "AKBNK.IS", "GARAN.IS", "VAKBN.IS", "EREGL.IS", "TUPRS.IS", "SISE.IS", "SAHOL.IS", "BIMAS.IS"]

def rsi_hesapla(prices, period=14):
    if len(prices) < period + 1:
        return 50
    gains = []
    losses = []
    for i in range(1, len(prices)):
        diff = prices[i] - prices[i-1]
        gains.append(max(diff, 0))
        losses.append(max(-diff, 0))
    avg_gain = sum(gains[-period:]) / period
    avg_loss = sum(losses[-period:]) / period
    if avg_loss == 0:
        return 100
    rs = avg_gain / avg_loss
    return round(100 - (100 / (1 + rs)), 1)

def analiz_yap(sym, df):
    close = df['Close'].tolist()
    volume = df['Volume'].tolist()
    fiyat = round(float(close[-1]), 2)
    # Değişim
    degisim = round(((close[-1] - close[-2]) / close[-2] * 100), 2) if len(close) > 1 else 0
    # RSI
    rsi = rsi_hesapla(close)
    # Hacim analizi
    ort_hacim = sum(volume[-20:]) / 20 if len(volume) >= 20 else volume[-1]
    hacim_oran = round(volume[-1] / ort_hacim, 2) if ort_hacim else 1
    hacim_durum = "Yüksek 🔥" if hacim_oran > 1.5 else "Normal" if hacim_oran > 0.8 else "Düşük"
    # Destek / Direnç - son 20 gün
    son20 = close[-20:]
    destek = round(min(son20) * 1.01, 2)
    direnc = round(max(son20) * 0.99, 2)
    # Sinyal + Skor
    skor = 50
    if rsi < 30: skor += 20  # aşırı satım, tepki gelebilir
    elif rsi > 70: skor -= 15 # aşırı alım
    elif 50 <= rsi <= 65: skor += 15
    if degisim > 1: skor += 15
    elif degisim > 0: skor += 5
    elif degisim < -1: skor -= 15
    if hacim_oran > 1.5 and degisim > 0: skor += 10
    skor = max(5, min(95, skor))

    if skor >= 75: sinyal = "GÜÇLÜ AL"
    elif skor >= 60: sinyal = "AL"
    elif skor <= 25: sinyal = "GÜÇLÜ SAT"
    elif skor <= 40: sinyal = "SAT"
    else: sinyal = "TUT"

    hedef = round(fiyat * 1.04, 2)
    stop = round(fiyat * 0.97, 2)
    if sinyal in ["SAT", "GÜÇLÜ SAT"]:
        hedef = round(fiyat * 1.02, 2)
        stop = round(fiyat * 0.94, 2)

    return {
        "sym": sym.replace(".IS", ""),
        "fiyat": fiyat,
        "degisim": f"%{degisim}",
        "sinyal": sinyal,
        "rsi": rsi,
        "hacim": hacim_durum,
        "hacim_oran": hacim_oran,
        "skor": skor,
        "destek": destek,
        "direnc": direnc,
        "hedef": hedef,
        "stop": stop
    }

sonuclar = []
for sym in HISSELER:
    try:
        df = yf.download(sym, period="1mo", interval="1d", progress=False, auto_adjust=True)
        if df.empty: continue
        # yfinance bazen MultiIndex döndürür
        if hasattr(df.columns, 'get_level_values'):
            try: df.columns = df.columns.get_level_values(0)
            except: pass
        sonuclar.append(analiz_yap(sym, df))
        print(f"{sym} -> {sonuclar[-1]}")
    except Exception as e:
        print(f"Hata {sym}: {e}")

# Türkiye saati
simdi = datetime.datetime.utcnow() + datetime.timedelta(hours=3)
data = {
    "Güncellendi": simdi.strftime("%H:%M"),
    "hisseler": sonuclar
}
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
print("OK - data.json yazıldı")