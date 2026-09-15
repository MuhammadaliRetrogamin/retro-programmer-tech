from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="uz">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Retro Programmer Tech</title>

<style>

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
}

body {
    background: #030305;
    color: white;
    font-family: Arial, Helvetica, sans-serif;
    overflow-x: hidden;
}

/* GALACTIC BACKGROUND */

body::before {
    content: "";
    position: fixed;
    inset: 0;
    z-index: -2;
    background:
        radial-gradient(circle at 75% 20%, rgba(70,70,255,.18), transparent 28%),
        radial-gradient(circle at 20% 70%, rgba(0,200,255,.10), transparent 25%),
        radial-gradient(circle at 50% 50%, rgba(255,255,255,.04), transparent 35%),
        #030305;
}

body::after {
    content: "";
    position: fixed;
    inset: 0;
    z-index: -1;
    opacity: .18;
    background-image:
        linear-gradient(rgba(255,255,255,.08) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255,255,255,.08) 1px, transparent 1px);
    background-size: 50px 50px;
    mask-image: linear-gradient(to bottom, black, transparent);
}

/* SIDEBAR */

.sidebar {
    position: fixed;
    left: 20px;
    top: 20px;
    bottom: 20px;
    width: 230px;
    background: rgba(10,10,14,.82);
    border: 1px solid #292936;
    border-radius: 22px;
    backdrop-filter: blur(18px);
    padding: 28px 20px;
    z-index: 20;
    box-shadow: 0 0 50px rgba(0,0,0,.5);
}

.logo {
    font-size: 18px;
    font-weight: 900;
    letter-spacing: 3px;
    line-height: 1.3;
    margin-bottom: 8px;
}

.logo span {
    color: #8d8dff;
}

.tagline {
    color: #666;
    font-size: 11px;
    letter-spacing: 2px;
    margin-bottom: 45px;
}

.menu-title {
    color: #555;
    font-size: 10px;
    letter-spacing: 3px;
    margin-bottom: 15px;
}

.menu a {
    display: block;
    color: #aaa;
    text-decoration: none;
    padding: 13px 12px;
    margin-bottom: 7px;
    border-radius: 10px;
    transition: .25s;
}

.menu a:hover {
    background: #171720;
    color: white;
    transform: translateX(5px);
}

.side-bottom {
    position: absolute;
    bottom: 25px;
    left: 20px;
    right: 20px;
}

.side-bottom p {
    color: #555;
    font-size: 11px;
    line-height: 1.6;
}

/* MAIN */

.main {
    margin-left: 270px;
    padding: 25px;
}

/* TOP BAR */

.topbar {
    min-height: 65px;
    border: 1px solid #20202a;
    border-radius: 17px;
    background: rgba(10,10,14,.65);
    backdrop-filter: blur(15px);
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 15px;
    padding: 12px 25px;
}

.status {
    color: #777;
    font-size: 12px;
    letter-spacing: 2px;
}

.status b {
    color: #aaa;
}

.top-buttons {
    display: flex;
    align-items: center;
    justify-content: flex-end;
    flex-wrap: wrap;
    gap: 8px;
}

.top-buttons a {
    text-decoration: none;
    color: white;
    border: 1px solid #333;
    padding: 9px 14px;
    border-radius: 9px;
    font-size: 12px;
    white-space: nowrap;
    transition: .25s;
}

.top-buttons a:hover {
    background: white;
    color: black;
}

/* HERO */

.hero {
    min-height: 650px;
    display: grid;
    grid-template-columns: 1.5fr .8fr;
    gap: 25px;
    align-items: stretch;
    padding: 25px 0;
}

.hero-main {
    position: relative;
    overflow: hidden;
    border: 1px solid #292936;
    border-radius: 25px;
    padding: 70px 55px;
    background:
        radial-gradient(circle at 80% 30%, rgba(100,100,255,.18), transparent 30%),
        linear-gradient(135deg,#111118,#050507);
}

.hero-main::before {
    content: "RETRO";
    position: absolute;
    right: -20px;
    bottom: -45px;
    font-size: 180px;
    font-weight: 900;
    color: rgba(255,255,255,.025);
}

.hero h1 {
    font-size: clamp(50px,6vw,90px);
    line-height: .9;
    letter-spacing: -5px;
    font-weight: 900;
}

.hero h1 span {
    color: #8d8dff;
}

.hero h2 {
    margin-top: 25px;
    font-size: 22px;
    color: #bbb;
    letter-spacing: 2px;
}

.hero-text {
    max-width: 650px;
    color: #777;
    line-height: 1.7;
    margin-top: 25px;
    font-size: 16px;
}

.hero-buttons {
    display: flex;
    gap: 12px;
    margin-top: 35px;
    flex-wrap: wrap;
}

.btn {
    display: inline-block;
    padding: 15px 22px;
    border-radius: 10px;
    text-decoration: none;
    color: white;
    border: 1px solid #444;
    background: #111118;
    font-weight: bold;
    font-size: 13px;
    transition: .3s;
}

.btn:hover {
    transform: translateY(-4px);
    background: white;
    color: black;
    box-shadow: 0 10px 35px rgba(255,255,255,.15);
}

.btn-main {
    background: white;
    color: black;
}

/* AD PANEL */

.ad-panel {
    border: 1px solid #292936;
    border-radius: 25px;
    background: linear-gradient(160deg,#111118,#07070a);
    padding: 25px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.ad-label {
    color: #666;
    letter-spacing: 3px;
    font-size: 10px;
}

.ad-box {
    min-height: 300px;
    border: 1px dashed #3b3b4a;
    border-radius: 18px;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 15px;
    overflow: hidden;
    background:
        radial-gradient(circle,rgba(100,100,255,.15),transparent 60%);
}

.ad-box img {
    width: 100%;
    max-height: 430px;
    object-fit: contain;
    border-radius: 12px;
    display: block;
}

/* LOGO IMAGE */

.ad-box img {
    width: 100%;
    max-width: 100%;
    height: auto;
    max-height: 430px;
    object-fit: contain;
    display: block;
    margin: auto;
}

/* AD BOTTOM */

.ad-bottom {
    border-top: 1px solid #222;
    padding-top: 20px;
}

.ad-bottom strong {
    font-size: 20px;
}

.ad-bottom p {
    color: #666;
    font-size: 12px;
    margin-top: 6px;
}

/* SECTION */

section {
    padding: 80px 0;
}

.section-head {
    display: flex;
    align-items: end;
    justify-content: space-between;
    margin-bottom: 30px;
}

.section-head h2 {
    font-size: 40px;
    letter-spacing: -2px;
}

.section-head p {
    color: #666;
}

/* CARDS */

.cards {
    display: grid;
    grid-template-columns: repeat(4,1fr);
    gap: 15px;
}

.card {
    min-height: 240px;
    border: 1px solid #24242e;
    border-radius: 18px;
    padding: 28px;
    background: linear-gradient(145deg,#111117,#07070a);
    transition: .3s;
}

.card:hover {
    transform: translateY(-8px);
    border-color: #555;
    box-shadow: 0 20px 50px rgba(0,0,0,.5);
}

.card-icon {
    font-size: 38px;
    margin-bottom: 25px;
}

.card h3 {
    font-size: 20px;
    margin-bottom: 12px;
}

.card p {
    color: #777;
    line-height: 1.6;
    font-size: 14px;
}

/* CPU */

.cpu-section {
    background: #07070a;
    margin: 0 -25px;
    padding-left: 25px;
    padding-right: 25px;
}

.cpu-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
}

.cpu {
    min-height: 270px;
    border-radius: 22px;
    padding: 40px;
    border: 1px solid #30303b;
    position: relative;
    overflow: hidden;
}

.cpu::after {
    content: "CPU";
    position: absolute;
    right: -15px;
    bottom: -45px;
    font-size: 150px;
    font-weight: 900;
    opacity: .03;
}

.intel {
    background: linear-gradient(135deg,#10141b,#08090c);
}

.amd {
    background: linear-gradient(135deg,#17100f,#090807);
}

.cpu-label {
    color: #666;
    letter-spacing: 4px;
    font-size: 11px;
}

.cpu h3 {
    font-size: 48px;
    margin: 20px 0 10px;
}

.cpu p {
    color: #777;
}

/* FEATURES */

.features {
    display: grid;
    grid-template-columns: repeat(3,1fr);
    gap: 15px;
}

.feature {
    border-left: 2px solid #555;
    padding: 20px;
    background: #09090c;
}

.feature strong {
    display: block;
    margin-bottom: 8px;
}

.feature span {
    color: #666;
    font-size: 13px;
}

/* CONTACT */

.contact {
    border: 1px solid #30303b;
    border-radius: 25px;
    padding: 55px;
    background:
        radial-gradient(circle at 80% 50%,rgba(100,100,255,.15),transparent 30%),
        #0b0b10;
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 30px;
}

.contact h2 {
    font-size: 45px;
}

.contact p {
    color: #777;
    margin-top: 12px;
}

/* FOOTER */

footer {
    border-top: 1px solid #20202a;
    padding: 35px 0;
    margin-top: 30px;
    color: #555;
    font-size: 12px;
    display: flex;
    justify-content: space-between;
}

/* MOBILE */

@media(max-width:1000px) {

    .topbar {
        height: auto;
        flex-wrap: wrap;
    }

    .top-buttons {
        justify-content: flex-start;
    }

    .sidebar {
        position: relative;
        width: auto;
        height: auto;
        left: auto;
        top: auto;
        bottom: auto;
        margin: 15px;
    }

    .side-bottom {
        display: none;
    }

    .main {
        margin-left: 0;
    }

    .hero {
        grid-template-columns: 1fr;
    }

    .cards {
        grid-template-columns: repeat(2,1fr);
    }

    .features {
        grid-template-columns: 1fr;
    }
}

@media(max-width:600px) {

    .main {
        padding: 12px;
    }

    .topbar {
        display: none;
    }

    .hero-main {
        padding: 45px 25px;
    }

    .hero h1 {
        font-size: 52px;
    }

    .cards,
    .cpu-grid {
        grid-template-columns: 1fr;
    }

    .section-head {
        display: block;
    }

    .section-head h2 {
        font-size: 32px;
        margin-bottom: 10px;
    }

    .contact {
        padding: 30px;
        display: block;
    }

    .contact h2 {
        font-size: 34px;
    }

    footer {
        display: block;
        line-height: 2;
    }
}

</style>
</head>

<body>

<!-- SIDEBAR -->

<aside class="sidebar">

<div class="logo">
RETRO<br><span>PROGRAMMER</span><br>TECH
</div>

<div class="tagline">
PC TECHNOLOGY
</div>

<div class="menu-title">NAVIGATION</div>

<nav class="menu">
<a href="#home">⌂ Главная</a>
<a href="#services">⚡ Xizmatlar</a>
<a href="#build">⚙ PC Sborka</a>
<a href="#systems">🖥 Gaming PC</a>
<a href="#contact">✉ Buyurtma</a>
</nav>

<div class="side-bottom">
<p>
Gaming PC<br>
Intel Core / AMD Ryzen<br>
Design / Montage<br>
Programming
</p>
</div>

</aside>

<!-- MAIN -->

<main class="main">

<div class="topbar">

<div class="status">
● <b>RETRO PROGRAMMER TECH</b> — ONLINE
</div>

<div class="top-buttons">
<a href="https://t.me/RetroProgrammerTech" target="_blank">TELEGRAM KANAL</a>
<a href="https://t.me/RETROUZX" target="_blank">TELEGRAM</a>
<a href="https://www.olx.uz/list/user/AagtZ/" target="_blank">OLX</a>
<a href="https://birbir.uz/ru/profile/5294370a-5276-4b23-a912-d21275f73ac4" target="_blank">BIRBIR</a>
<a href="#contact">BUYURTMA</a>
</div>

</div>

<!-- HERO -->

<header class="hero" id="home">

<div class="hero-main">

<h1>
GALACTIC<br>
<span>PC</span><br>
TECHNOLOGY
</h1>

<h2>
POWER • PERFORMANCE • STYLE
</h2>

<p class="hero-text">
Gaming PC, professional PC yig‘ish, Office,
Design, Montage va Programming uchun
zamonaviy kompyuter yechimlari.
Siz konfiguratsiyani tanlaysiz — biz yig‘amiz.
</p>

<div class="hero-buttons">

<a class="btn btn-main" href="#systems">
GAMING PC
</a>

<a class="btn" href="#build">
PC SBORKA
</a>

<a class="btn" href="https://t.me/RetroProgrammerTech" target="_blank">
TELEGRAM
</a>

</div>

</div>

<!-- AD -->

<div class="ad-panel">

<div class="ad-label">
FEATURED / ADVERTISEMENT
</div>

<div class="ad-box">

<img src="/static/logo.png" alt="Retro Programmer Tech">

</div>

<div class="ad-bottom">
<strong>RETRO PROGRAMMER TECH</strong>
<p>Professional PC solutions</p>
</div>

</div>

</header>

<!-- SERVICES -->

<section id="services">

<div class="section-head">
<div>
<h2>XIZMATLAR</h2>
<p>Kompyuter bo‘yicha professional xizmatlar</p>
</div>
</div>

<div class="cards">

<div class="card">
<div class="card-icon">🎮</div>
<h3>Gaming PC</h3>
<p>
CS2, GTA V, PUBG PC, Valorant,
Fortnite, Apex Legends, Forza
va boshqa o‘yinlar uchun.
</p>
</div>

<div class="card">
<div class="card-icon">⚙️</div>
<h3>PC SBORKA</h3>
<p>
Intel Core yoki AMD Ryzen asosida
byudjetdan kuchli Gaming PC gacha
individual yig‘ish.
</p>
</div>

<div class="card">
<div class="card-icon">💼</div>
<h3>Office PC</h3>
<p>
Ofis, o‘qish, internet, hujjatlar
va kundalik ishlar uchun optimal
kompyuterlar.
</p>
</div>

<div class="card">
<div class="card-icon">🎬</div>
<h3>Design & Montage</h3>
<p>
Photoshop, Premiere Pro,
After Effects, Blender va boshqa
professional dasturlar.
</p>
</div>

</div>

</section>

<!-- CPU -->

<section class="cpu-section" id="build">

<div class="section-head">
<div>
<h2>PLATFORM</h2>
<p>Intel yoki AMD — tanlov sizniki.</p>
</div>
</div>

<div class="cpu-grid">

<div class="cpu intel">
<div class="cpu-label">PROCESSOR PLATFORM</div>
<h3>INTEL CORE</h3>
<p>Core i3 • i5 • i7 • i9</p>
</div>

<div class="cpu amd">
<div class="cpu-label">PROCESSOR PLATFORM</div>
<h3>AMD RYZEN</h3>
<p>Ryzen 5 • Ryzen 7 • Ryzen 9</p>
</div>

</div>

</section>

<!-- SYSTEMS -->

<section id="systems">

<div class="section-head">
<div>
<h2>GAMING SYSTEMS</h2>
<p>Gaming va kuchli ishchi kompyuterlar</p>
</div>
</div>

<div class="features">

<div class="feature">
<strong>GPU</strong>
<span>GTX / RTX / Radeon RX</span>
</div>

<div class="feature">
<strong>RAM</strong>
<span>DDR4 / DDR5 konfiguratsiyalar</span>
</div>

<div class="feature">
<strong>STORAGE</strong>
<span>SSD / NVMe / HDD</span>
</div>

<div class="feature">
<strong>COOLING</strong>
<span>Air Cooling / RGB / Performance</span>
</div>

<div class="feature">
<strong>CASE</strong>
<span>Gaming va Professional Case</span>
</div>

<div class="feature">
<strong>BUILD</strong>
<span>Sizning byudjetingizga mos</span>
</div>

</div>

</section>

<!-- CONTACT -->

<section id="contact">

<div class="contact">

<div>
<h2>PC KERAKMI?</h2>
<p>
Konfiguratsiyani ayting — siz uchun variant tayyorlaymiz.
</p>
</div>

<div class="hero-buttons">

<a class="btn btn-main"
href="https://t.me/RetroProgrammerTech"
target="_blank">
TELEGRAM
</a>

<a class="btn"
href="tel:+998940728098">
📞 +998 94 072 80 98
</a>

</div>

</div>

</section>

<footer>

<div>
© 2026 RETRO PROGRAMMER TECH
</div>

<div>
GAMING • OFFICE • DESIGN • PC BUILD
</div>

</footer>

</main>

</body>
</html>
    """
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)