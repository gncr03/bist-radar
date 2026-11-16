<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>BIST RADAR - Canlı Tarama</title>
<style>
:root{--bg:#0f172a;--card:#1e293b;--hover:#334155;--text:#f8fafc;--sec:#94a3b8;--green:#10b981;--red:#ef4444;--border:#334155}
*{box-sizing:border-box;margin:0;padding:0;font-family:system-ui,sans-serif}
body{background:var(--bg);color:var(--text);padding:16px;line-height:1.5}
.container{max-width:1200px;margin:0 auto}
h1{font-size:1.5rem;margin-bottom:8px}
.subtitle{color:var(--sec);font-size:.875rem;margin-bottom:20px}
.stats-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px;margin-bottom:20px}
.stat-card{background:var(--card);padding:14px;border-radius:8px;border:1px solid var(--border)}
.stat-title{font-size:.75rem;color:var(--sec);text-transform:uppercase;font-weight:600}
.stat-value{font-size:1.5rem;font-weight:700;margin-top:4px}
.controls-card{background:var(--card);padding:16px;border-radius:8px;border:1px solid var(--border);margin-bottom:20px;display:flex;flex-wrap:wrap;gap:12px;align-items:center;justify-content:space-between}
.control-group{display:flex;flex-direction:column;gap:4px}
.control-label{font-size:.75rem;color:var(--sec);font-weight:600}
select,input,button{background:var(--bg);color:var(--text);border:1px solid var(--border);padding:8px 12px;border-radius:6px;font-size:.875rem;outline:none}
button{background:#3b82f6;color:#fff;font-weight:600;cursor:pointer}
.btn-refresh{background:var(--green)}
.section-title{font-size:1.125rem;font-weight:700;margin-bottom:12px}
.signals-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:12px;margin-bottom:24px}
.signal-card{background:linear-gradient(135deg,#1e293b,#0f172a);border:1px solid var(--green);border-radius:8px;padding:14px;cursor:pointer}
.signal-header{display:flex;justify-content:space-between;align-items:center;margin-bottom:8px}
.signal-symbol{font-weight:800;font-size:1.1rem}
.signal-score{background:rgba(16,185,129,.2);color:var(--green);padding:2px 8px;border-radius:12px;font-size:.75rem;font-weight:700}
.signal-details{font-size:.8rem;color:var(--sec);display:flex;flex-direction:column;gap:3px}
.radar-box{background:var(--card);border-radius:8px;border:1px solid var(--border);padding:20px;margin-bottom:24px}
.radar-header{display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;border-bottom:1px solid var(--border);padding-bottom:12px}
.chart-container{display:flex;flex-direction:column;gap:10px;position:relative}
.bar-row{display:flex;align-items:center;gap:10px;cursor:pointer;padding:4px;border-radius:6px}
.bar-row:hover{background:var(--hover)}
.bar-label{width:65px;font-weight:700;font-size:.85rem;text-align:right;flex-shrink:0}
.bar-track{flex-grow:1;background:rgba(255,255,255,.05);height:26px;border-radius:4px;position:relative;display:flex;align-items:center;overflow:hidden}
.bar-fill{height:100%;border-radius:4px;position:absolute;left:0}
.bar-text{position:absolute;right:8px;font-size:.75rem;font-weight:700;z-index:4;white-space:nowrap;text-shadow:0 1px 2px #000}
table{width:100%;border-collapse:collapse;font-size:.85rem}
th,td{padding:10px 12px;border-bottom:1px solid var(--border);text-align:left}
th{color:var(--sec)}
tr:hover td{background:var(--hover);cursor:pointer}
.modal{display:none;position:fixed;inset:0;background:rgba(0,0,0,.7);z-index:1000;align-items:center;justify-content:center;padding:16px}
.modal.active{display:flex}
.modal-content{background:var(--card);border:1px solid var(--border);border-radius:12px;width:100%;max-width:550px;padding:24px;position:relative;max-height:90vh;overflow-y:auto}
.modal-close{position:absolute;top:16px;right:16px;background:none;border:none;color:var(--sec);font-size:1.25rem;cursor:pointer}
.modal-grid{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:16px}
.modal-box{background:var(--bg);padding:12px;border-radius:8px;border:1px solid var(--border)}
.modal-box-title{font-size:.75rem;color:var(--sec);font-weight:600}
.modal-box-val{font-size:1.1rem;font-weight:700}
.badge{display:inline-block;padding:2px 8px;border-radius:4px;font-size:.75rem;font-weight:700}
.badge-green{background:rgba(16,185,129,.2);color:var(--green)}
.badge-red{background:rgba(239,68,68,.2);color:var(--red)}
.badge-gray{background:rgba(100,116,139,.2);color:var(--sec)}
</style>
</head>
<body>
<div class="container">
<h1>📊 BIST RADAR & Doğru Alış Sinyalleri</h1>
<p class="subtitle">CANLI - Stooq / BIST Verisi | RSI(14) + Hacim + ATR Planı | <span id="liveDot" style="color:#f59e0b">● DEMO VERİ</span></p>
<div class="stats-grid">
<div class="stat-card"><div class="stat-title">Taranan Hisse</div><div class="stat-value" id="statTotalCount">0</div></div>
<div class="stat-card"><div class="stat-title">Güçlü Al</div><div class="stat-value" style="color:var(--green)" id="statBuyCount">0</div></div>
<div class="stat-card"><div class="stat-title">Dip / İzleme</div><div class="stat-value" style="color:#f59e0b" id="statWatchCount">0</div></div>
<div class="stat-card"><div class="stat-title">Aşırı Alım RSI≥70</div><div class="stat-value" style="color:var(--red)" id="statSellCount">0</div></div>
</div>
<div class="section-title">⭐ Öne Çıkan Doğru Alış Sinyalleri</div>
<div class="signals-grid" id="topSignalsGrid"></div>
<div class="controls-card">
<div class="control-group"><span class="control-label">Endeks Havuzu</span><div style="display:flex;gap:6px"><button onclick="setPool('bist30')" id="btnPool30">BIST 30</button><button onclick="setPool('bist100')" id="btnPool100" style="background:var(--card)">BIST 100</button><button onclick="setPool('all')" id="btnPoolAll" style="background:var(--card)">Tümü</button></div></div>
<div class="control-group"><span class="control-label">Filtre</span><select id="quickFilterSelect" onchange="renderApp()"><option value="all">Tümü</option><option value="buy">Sadece Güçlü Al</option><option value="watch">Dip / İzleme</option><option value="rsi30">RSI &lt; 30</option></select></div>
<div class="control-group"><span class="control-label">Canlı Veri Motoru</span><button class="btn-refresh" onclick="fetchLiveMarketData()">🔄 Canlı Fiyatları Çek</button></div>
</div>
<div class="radar-box"><div class="radar-header"><h3>BIST RADAR - Canlı Tarama</h3><span id="scanStatus" style="font-size:.8rem;color:var(--sec)">Hazır</span></div><div class="chart-container" id="chartContainer"></div></div>
<div class="radar-box"><div class="radar-header"><h3>📋 Tüm Hisseler</h3><input id="searchInput" placeholder="Hisse ara THYAO..." oninput="renderApp()" style="width:200px"></div><div style="overflow-x:auto"><table><thead><tr><th>Hisse</th><th>Dün Kapanış</th><th>Son Fiyat</th><th>Günlük %</th><th>RSI</th><th>Hacim %</th><th>Sinyal</th><th>Skor</th></tr></thead><tbody id="stockTableBody"></tbody></table></div></div>
</div>
<div class="modal" id="detailModal"><div class="modal-content"><button class="modal-close" onclick="closeModal()">×</button><div style="font-size:1.25rem;font-weight:800" id="modalSymbol">THYAO</div><div style="color:var(--sec);font-size:.85rem;margin-bottom:16px" id="modalName"></div><div class="modal-grid"><div class="modal-box"><div class="modal-box-title">Dün Kapanış</div><div class="modal-box-val" id="modalPrev"></div></div><div class="modal-box"><div class="modal-box-title">Son Fiyat</div><div class="modal-box-val" id="modalPrice"></div></div><div class="modal-box"><div class="modal-box-title">Skor</div><div class="modal-box-val" id="modalScore"></div></div><div class="modal-box"><div class="modal-box-title">RSI</div><div class="modal-box-val" id="modalRsi"></div></div><div class="modal-box"><div class="modal-box-title">Hacim</div><div class="modal-box-val" id="modalVol"></div></div><div class="modal-box"><div class="modal-box-title">Son İşlem Tarihi</div><div class="modal-box-val" style="font-size:.9rem" id="modalDate"></div></div></div><div style="background:var(--bg);padding:14px;border-radius:8px;border:1px solid var(--border);margin-bottom:16px"><div style="font-size:.8rem;font-weight:700;color:var(--sec);margin-bottom:8px">🎯 ATR RİSK / ÖDÜL PLANI</div><div style="display:flex;justify-content:space-between"><span>Giriş:</span><strong id="modalEntry" style="color:#3b82f6"></strong></div><div style="display:flex;justify-content:space-between"><span>Stop:</span><strong id="modalStop" style="color:var(--red)"></strong></div><div style="display:flex;justify-content:space-between"><span>Hedef 1:2:</span><strong id="modalTarget" style="color:var(--green)"></strong></div></div><div style="font-size:.8rem;color:var(--sec)" id="modalTechDesc"></div></div></div>
<script>
const baseTickers=[
["THYAO","Türk Hava Yolları"],["GARAN","Garanti BBVA"],["ASELS","Aselsan"],["EREGL","Ereğli"],["BIMAS","BİM"],["TUPRS","Tüpraş"],["KCHOL","Koç Holding"],["SISE","Şişecam"],["AKBNK","Akbank"],["YKBNK","Yapı Kredi"],["ISCTR","İş Bankası"],["PETKM","Petkim"],["SASA","Sasa"],["HEKTS","Hektaş"],["ENKAI","Enka"],["KRDMD","Kardemir"],["TOASO","Tofaş"],["FROTO","Ford"],["PGSUS","Pegasus"],["MGROS","Migros"],["ASTOR","Astor"],["ALARK","Alarko"],["KOZAL","Koza Altın"],["KOZAA","Koza Anadolu"],["KONTR","Kontrolmatik"],["EUPWR","Europower"],["ODAS","Odaş"],["KCAER","Kocaer"],["MAVI","Mavi"],["ARCLK","Arçelik"],["VESTL","Vestel"],["OTKAR","Otokar"],["DOHOL","Doğan"],["AGHOL","Anadolu Grubu"],["SOKM","Şok"],["CIMSA","Çimsa"],["AKCNS","Akçansa"],["OYAKC","Oyak Çimento"],["ZOREN","Zorlu Enerji"],["EKGYO","Emlak Konut"],["TSKB","TSKB"],["TURSG","Türkiye Sigorta"],["ENJSA","Enerjisa"],["ECILC","Eczacıbaşı İlaç"],["SELEC","Selçuk Ecza"],["MPARK","MLP Sağlık"],["VAKBN","Vakıfbank"],["HALKB","Halkbank"],["LOGO","Logo"],["GESAN","Girişim Elektrik"],["CWENE","CW Enerji"],["YEOTK","Yeo Teknoloji"],["TABGD","Tab Gıda"]
];
let rawStocks=baseTickers.map(([s,n],i)=>({s,n,p:20+(i*13)%400,prevClose:20+(i*13)%400,c:((i%5-2)*1.2),r:15+(i*7)%75,v:20+(i*23)%350,ema:"-",trend:"Yatay",live:false,lastDate:"-"}));
let currentPool='bist30';
function setPool(p){currentPool=p;document.getElementById('btnPool30').style.background=p==='bist30'?'#3b82f6':'var(--card)';document.getElementById('btnPool100').style.background=p==='bist100'?'#3b82f6':'var(--card)';document.getElementById('btnPoolAll').style.background=p==='all'?'#3b82f6':'var(--card)';renderApp();}
function getList(){if(currentPool==='bist30')return rawStocks.slice(0,30);if(currentPool==='bist100')return rawStocks.slice(0,60);return rawStocks;}
function calcRSI(closes,period=14){
 if(closes.length<period+1) return 50;
 let gains=0,losses=0;
 for(let i=closes.length-period;i<closes.length;i++){let d=closes[i]-closes[i-1];if(d>=0)gains+=d;else losses-=d;}
 let rs=(gains/period)/((losses/period)||1);
 return Math.round(100-(100/(1+rs)));
}
async function fetchOne(st){
 try{
  const sym=st.s.toLowerCase()+".is";
  const res=await fetch(`https://stooq.com/q/d/l/?s=${sym}&i=d`);
  const text=await res.text();
  const lines=text.trim().split("\n");
  const rows=lines.slice(1).slice(-30).map(l=>{
    const p=l.split(",");
    return {date:p[0], close:parseFloat(p[4]), vol:parseFloat(p[5])}
  }).filter(x=>!isNaN(x.close));
  if(rows.length<15) throw new Error("yetersiz veri");
  const closes=rows.map(r=>r.close);
  const price=closes[closes.length-1];
  const prev=closes[closes.length-2];
  const change=((price-prev)/prev*100);
  const rsi=calcRSI(closes);
  const vols=rows.map(r=>r.vol);
  const lastVol=vols[vols.length-1];
  const avgVol=vols.slice(0,-1).reduce((a,b)=>a+b,0)/Math.max(1,vols.length-1);
  const volChange=Math.round((lastVol-avgVol)/avgVol*100);
  Object.assign(st,{p:price,prevClose:prev,c:parseFloat(change.toFixed(2)),r:rsi,v:volChange,ema:rsi<32?"Dip Teyit":rsi>68?"Direnç":"Pozitif",trend:rsi<32?"Dip Dönüşü":rsi>68?"Düzeltme":"Yükseliş",live:true,lastDate:rows[rows.length-1].date});
  return true;
 }catch(e){return false;}
}
async function fetchLiveMarketData(){
 document.getElementById('scanStatus').innerText="Canlı veriler çekiliyor... (30 hisse, ~20 sn)";
 const list=getList();
 for(let i=0;i<list.length;i+=5){
   await Promise.all(list.slice(i,i+5).map(fetchOne));
   renderApp();
 }
 const liveCount=list.filter(x=>x.live).length;
 document.getElementById('scanStatus').innerText=`Son Güncelleme: ${new Date().toLocaleTimeString()} - ${liveCount}/${list.length} canlı - Son işlem: ${list[0]?.lastDate||"-"}`;
 document.getElementById('liveDot').innerText=liveCount>0?"● CANLI VERİ":"● DEMO VERİ";
 document.getElementById('liveDot').style.color=liveCount>0?"#10b981":"#f59e0b";
 if(liveCount===0) alert("Veri kaynağı şu an cevap vermedi, demo veride kaldı. 1 dk sonra tekrar dene.");
}
function calculateSignal(st){
 let score=50,status="İZLE",cls="badge-gray";
 if(st.r<=32&&st.v>=20){score=92;status="GÜÇLÜ AL (Dip Dönüşü)";cls="badge-green";}
 else if(st.r<=35){score=80;status="AL (RSI Destekte)";cls="badge-green";}
 else if(st.r>=70){score=20;status="AŞIRI ALIM";cls="badge-red";}
 else if(st.v>=50&&st.c>0){score=75;status="AL (Hacim Patlaması)";cls="badge-green";}
 return{score,status,badgeClass:cls};
}
function renderApp(){
 const stocks=getList();
 const q=(document.getElementById('searchInput').value||"").toLowerCase();
 const f=document.getElementById('quickFilterSelect').value;
 let filtered=stocks.filter(st=>{
  if(!st.s.toLowerCase().includes(q)&&!st.n.toLowerCase().includes(q))return false;
  const sig=calculateSignal(st);
  if(f==='buy')return sig.score>=75;
  if(f==='watch')return st.r>=30&&st.r<=45;
  if(f==='rsi30')return st.r<30;
  return true;
 });
 document.getElementById('statTotalCount').innerText=stocks.length;
 document.getElementById('statBuyCount').innerText=stocks.filter(s=>calculateSignal(s).score>=75).length;
 document.getElementById('statWatchCount').innerText=stocks.filter(s=>s.r>=30&&s.r<=45).length;
 document.getElementById('statSellCount').innerText=stocks.filter(s=>s.r>=70).length;
 const top=[...stocks].sort((a,b)=>calculateSignal(b).score-calculateSignal(a).score).slice(0,3);
 document.getElementById('topSignalsGrid').innerHTML=top.map(st=>{const sig=calculateSignal(st);return `<div class="signal-card" onclick="openDetailModal('${st.s}')"><div class="signal-header"><span class="signal-symbol">${st.s} ${st.live?'🟢':''}</span><span class="signal-score">Skor: ${sig.score}/100</span></div><div class="signal-details"><span>Kapanış: ₺${(st.prevClose||st.p).toFixed(2)} | Son: ₺${st.p.toFixed(2)} (${st.c>=0?'+':''}${st.c}%)</span><span>RSI: ${st.r} | Hacim: %${st.v}</span><strong style="color:var(--green)">${sig.status}</strong></div></div>`}).join('');
 document.getElementById('chartContainer').innerHTML=filtered.slice(0,30).map(st=>{let col=st.r<=30?"var(--green)":st.r>=70?"var(--red)":"#64748b";return `<div class="bar-row" onclick="openDetailModal('${st.s}')"><div class="bar-label">${st.s}</div><div class="bar-track"><div class="bar-fill" style="width:${st.r}%;background:${col}"></div><div class="bar-text">₺${st.p.toFixed(2)} (${st.c>=0?'+':''}${st.c}%) | RSI ${st.r} | Hacim %${st.v}</div></div></div>`}).join('');
 document.getElementById('stockTableBody').innerHTML=filtered.map(st=>{const sig=calculateSignal(st);return `<tr onclick="openDetailModal('${st.s}')"><td><strong>${st.s}</strong> <span style="font-size:.75rem;color:var(--sec)">${st.n}</span></td><td>₺${(st.prevClose||st.p).toFixed(2)}</td><td>₺${st.p.toFixed(2)}</td><td style="color:${st.c>=0?'var(--green)':'var(--red)'};font-weight:700">${st.c>=0?'+':''}${st.c}%</td><td><strong>${st.r}</strong></td><td>%${st.v}</td><td><span class="badge ${sig.badgeClass}">${sig.status}</span></td><td><strong>${sig.score}</strong></td></tr>`}).join('');
}
function openDetailModal(sym){
 const st=rawStocks.find(x=>x.s===sym);if(!st)return;
 const sig=calculateSignal(st);const atr=st.p*0.035;
 document.getElementById('modalSymbol').innerText=st.s+(st.live?" 🟢 CANLI":"");
 document.getElementById('modalName').innerText=st.n;
 document.getElementById('modalPrev').innerText=`₺${(st.prevClose||st.p).toFixed(2)}`;
 document.getElementById('modalPrice').innerText=`₺${st.p.toFixed(2)} (${st.c>=0?'+':''}${st.c}%)`;
 document.getElementById('modalScore').innerText=`${sig.score} / 100`;
 document.getElementById('modalRsi').innerText=st.r;
 document.getElementById('modalVol').innerText=`%${st.v}`;
 document.getElementById('modalDate').innerText=st.lastDate||"-";
 document.getElementById('modalEntry').innerText=`₺${st.p.toFixed(2)}`;
 document.getElementById('modalStop').innerText=`₺${(st.p-atr).toFixed(2)} (-%3.5)`;
 document.getElementById('modalTarget').innerText=`₺${(st.p+atr*2).toFixed(2)} (+%7.0)`;
 document.getElementById('modalTechDesc').innerHTML=`<strong>Teknik Özet:</strong> ${st.s} ${st.trend} eğiliminde. Dün kapanış <strong>₺${(st.prevClose||st.p).toFixed(2)}</strong>, son fiyat <strong>₺${st.p.toFixed(2)}</strong>. RSI <strong>${st.r}</strong>, Hacim <strong>%${st.v}</strong>. Durum: <b>${sig.status}</b>. ${st.live?"Veri Stooq/BIST'ten canlı çekildi.":"Veri demo, Canlı butonuna bas."}`;
 document.getElementById('detailModal').classList.add('active');
}
function closeModal(){document.getElementById('detailModal').classList.remove('active');}
window.onload=()=>{renderApp(); fetchLiveMarketData();}
</script>
</body>
</html>