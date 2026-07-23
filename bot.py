<!DOCTYPE html>
<html lang="fa">
<head>
<meta charset="UTF-8">
<title>🎮 Sens FF</title>

<style>
body{
  margin:0;
  font-family:sans-serif;
  background:linear-gradient(135deg,#020617,#0f172a);
  color:white;
  text-align:center;
}

h2{
  margin-top:20px;
  text-shadow:0 0 20px #38bdf8;
}

.btn{
  padding:12px 20px;
  margin:10px;
  border:none;
  border-radius:12px;
  background:#0ea5e9;
  color:white;
  box-shadow:0 0 10px #0ea5e9,0 0 30px #0ea5e9;
  cursor:pointer;
}

.card{
  background:rgba(30,41,59,0.8);
  margin:6px;
  padding:10px;
  border-radius:10px;
  box-shadow:0 0 10px #0ea5e9;
  cursor:pointer;
}

input{
  padding:10px;
  width:80%;
  border-radius:10px;
  border:none;
}

.hidden{display:none;}
</style>
</head>

<body>

<h2>🔥 انتخاب سنس حرفه‌ای</h2>

<div id="os"></div>

<div id="brands" class="hidden"></div>

<div id="models" class="hidden">
<button class="btn" onclick="back()">🔙 برگشت</button>
<h3 id="title"></h3>
<input id="search" placeholder="جستجو..." onkeyup="filter()">
<div id="list"></div>
</div>

<script>

const BOT = "FF_Ranked0011";

// سیستم عامل
const OS = ["Android","iOS"];

// برندهای اندروید (8 تا)
const ANDROID_BRANDS = [
  "Xiaomi","Samsung","Poco","Realme","Oppo","Vivo","Huawei","OnePlus"
];

// برندهای iOS
const IOS_BRANDS = ["iPhone","Apple"];

// ساخت مدل‌ها اتوماتیک
function generateModels(brand){
  let arr = [];
  for(let i=1;i<=80;i++){
    arr.push(brand+" "+i);
    arr.push(brand+" "+i+" Pro");
    arr.push(brand+" "+i+" Pro Max");
    arr.push(brand+" "+i+" Ultra");
  }
  return arr;
}

// ساخت OS
const osDiv = document.getElementById("os");
OS.forEach(o=>{
  let btn = document.createElement("button");
  btn.className="btn";
  btn.innerText=o;
  btn.onclick=()=>showBrands(o);
  osDiv.appendChild(btn);
});

function showBrands(os){
  osDiv.classList.add("hidden");
  document.getElementById("brands").classList.remove("hidden");

  let bDiv = document.getElementById("brands");
  bDiv.innerHTML="";

  let brands = os==="Android" ? ANDROID_BRANDS : IOS_BRANDS;

  brands.forEach(b=>{
    let btn=document.createElement("button");
    btn.className="btn";
    btn.innerText=b;
    btn.onclick=()=>showModels(b);
    bDiv.appendChild(btn);
  });
}

function showModels(brand){
  document.getElementById("brands").classList.add("hidden");
  document.getElementById("models").classList.remove("hidden");

  document.getElementById("title").innerText=brand;

  let list=document.getElementById("list");
  list.innerHTML="";

  let models = generateModels(brand);

  models.forEach(m=>{
    let div=document.createElement("div");
    div.className="card";
    div.innerText=m;

    div.onclick=()=>{
      let url="https://t.me/"+BOT+"?start="+encodeURIComponent(m);
      window.location.href=url;
    };

    list.appendChild(div);
  });
}

function filter(){
  let val=document.getElementById("search").value.toLowerCase();
  document.querySelectorAll(".card").forEach(c=>{
    c.style.display=c.innerText.toLowerCase().includes(val)?"block":"none";
  });
}

function back(){
  document.getElementById("models").classList.add("hidden");
  document.getElementById("brands").classList.remove("hidden");
}

</script>

</body>
</html>
