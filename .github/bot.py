import yfinance as yf, json, datetime
TICKS="AEFES,AGHOL,AHGAZ,AKBNK,AKCNS,AKSA,AKSEN,ALARK,ALFAS,ALBRK,ANHYT,ANSGR,ARCLK,ARDYZ,ASELS,ASTOR,BERA,BIMAS,BINHO,BRSAN,BRYAT,BTCIM,CANTE,CCOLA,CIMSA,CWENE,DOAS,DOHOL,ECILC,ECZYT,EGEEN,EGGUB,EKGYO,ENERY,ENJSA,ENKAI,EREGL,EUPWR,FENER,FROTO,GARAN,GENIL,GESAN,GLRMK,GOLTS,GUBRF,HALKB,HEKTS,ISCTR,ISDMR,ISMEN,KARSN,KCAER,KCHOL,KENT,KMPUR,KONTR,KOZAA,KOZAL,KRDMD,KTLEV,MAVI,MGROS,MIATK,MPARK,ODAS,OTKAR,OYAKC,PAHOL,PETKM,PGSUS,SAHOL,SASA,SDTTR,SELEC,SISE,SKBNK,SMRTG,SOKM,TABGD,TAVHL,TCELL,THYAO,TKFEN,TOASO,TSKB,TTKOM,TTRAK,TUPRS,TURSG,ULKER,VAKBN,VESTL,YKBNK,ZOREN,AGROT,AKFYE,ALTNY,CMENT,IEYHO".split(",")
def rsi_calc(c):
    if len(c)<15: return 50
    d=[c[i]-c[i-1] for i in range(1,len(c))]
    g=[x if x>0 else 0 for x in d[-14:]]
    l=[-x if x<0 else 0 for x in d[-14:]]
    ag=sum(g)/14; al=sum(l)/14
    if al==0: return 100
    rs=ag/al
    return round(100-(100/(1+rs)),1)
stocks=[]
for t in TICKS:
    try:
        df=yf.download(t+".IS", period="1mo", interval="1d", progress=False)
        if df.empty: continue
        closes=df['Close'].values.flatten()
        price=round(float(closes[-1]),2)
        prev=float(closes[-2]) if len(closes)>1 else price
        ch=round((price-prev)/prev*100,2)
        stocks.append({"sym":t,"price":price,"ch":ch,"rsi":rsi_calc(list(closes)),"time":datetime.datetime.now().strftime("%H:%M")})
    except: continue
open("data.json","w",encoding="utf-8").write(json.dumps({"updated":datetime.datetime.now().strftime("%H:%M"),"stocks":stocks},ensure_ascii=False))
print("toplam",len(stocks))