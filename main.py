# app.py
# Execute com: python app.py
# Acesse em: http://localhost:8000

from http.server import HTTPServer, BaseHTTPRequestHandler
import json, urllib.parse, os, datetime

HTML = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<meta name="description" content="Jet Livery – Tele-entrega rápida e humanizada em Tramandaí e região."/>
<meta name="keywords" content="motoboy Tramandaí, tele entrega Tramandaí, entregas rápidas"/>
<title>Jet Livery – Na velocidade que você precisa</title>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800&family=Inter:wght@400;500&display=swap" rel="stylesheet"/>
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{
  --yellow:#FFD230;--black:#0A0A0A;--white:#fff;
  --gray:#F5F5F5;--gray2:#9E9E9E;--gray3:#444;
  --shadow:0 4px 24px rgba(0,0,0,.09);
  --shadow2:0 8px 32px rgba(0,0,0,.15);--trans:.3s ease
}
html{scroll-behavior:smooth}
body{font-family:'Inter',sans-serif;color:var(--black);background:var(--white);line-height:1.6;overflow-x:hidden}
a{text-decoration:none;color:inherit}ul{list-style:none}
.container{width:100%;max-width:1100px;margin:0 auto;padding:0 24px}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;
  font-family:'Poppins',sans-serif;font-size:.92rem;font-weight:600;
  padding:13px 28px;border-radius:999px;border:2px solid transparent;
  cursor:pointer;transition:all var(--trans)}
.btn-yellow{background:var(--yellow);color:var(--black);border-color:var(--yellow)}
.btn-yellow:hover{background:#f5c800;transform:translateY(-2px);box-shadow:0 6px 20px rgba(255,210,48,.4)}
.btn-outline-white{background:transparent;color:var(--white);border-color:rgba(255,255,255,.4)}
.btn-outline-white:hover{background:rgba(255,255,255,.1);transform:translateY(-2px)}
.btn-outline{background:transparent;color:var(--black);border-color:var(--black)}
.btn-outline:hover{background:var(--black);color:var(--white);transform:translateY(-2px)}
.btn-dark{background:var(--black);color:var(--white);border-color:var(--black)}
.btn-dark:hover{background:#222;transform:translateY(-2px)}
.btn-wa{background:#25D366;color:#fff;border-color:#25D366}
.btn-wa:hover{background:#1fb855;transform:translateY(-2px);box-shadow:0 6px 20px rgba(37,211,102,.4)}
.btn-wa svg{width:18px;height:18px;fill:#fff;flex-shrink:0}
.tag{display:inline-block;background:var(--yellow);color:var(--black);
  font-family:'Poppins',sans-serif;font-size:.7rem;font-weight:700;
  letter-spacing:.1em;text-transform:uppercase;padding:4px 14px;
  border-radius:999px;margin-bottom:14px}
.s-title{font-family:'Poppins',sans-serif;font-size:clamp(1.6rem,3vw,2.3rem);
  font-weight:700;line-height:1.2;margin-bottom:14px}
.s-sub{font-size:.97rem;color:var(--gray3);max-width:540px;margin:0 auto 44px}
.tc{text-align:center}

/* NAV */
nav{position:fixed;top:0;left:0;right:0;z-index:1000;
  transition:background var(--trans),box-shadow var(--trans)}
nav.scrolled{background:rgba(255,255,255,.97);
  box-shadow:0 2px 16px rgba(0,0,0,.08);backdrop-filter:blur(8px)}
.nav-inner{display:flex;align-items:center;justify-content:space-between;height:90px}
.logo{position:relative;display:flex;align-items:center;height:80px;width:220px}
.logo-branca,.logo-preta{position:absolute;top:0;left:0;height:80px;width:auto;
  object-fit:contain;transition:opacity var(--trans)}
.logo-branca{opacity:1}
.logo-preta{opacity:0}
nav.scrolled .logo-branca{opacity:0}
nav.scrolled .logo-preta{opacity:1}
.nav-links{display:flex;align-items:center;gap:28px}
.nav-links a{font-family:'Poppins',sans-serif;font-size:.85rem;font-weight:500;
  color:rgba(255,255,255,.85);transition:color var(--trans);position:relative}
nav.scrolled .nav-links a{color:var(--black)}
.nav-links a::after{content:'';position:absolute;bottom:-3px;left:0;
  width:0;height:2px;background:var(--yellow);transition:width var(--trans)}
.nav-links a:hover::after{width:100%}
.hbg{display:none;flex-direction:column;gap:5px;cursor:pointer;
  background:none;border:none;padding:4px}
.hbg span{display:block;width:23px;height:2px;background:var(--white);
  border-radius:2px;transition:all var(--trans)}
nav.scrolled .hbg span{background:var(--black)}
.hbg.open span:nth-child(1){transform:translateY(7px) rotate(45deg)}
.hbg.open span:nth-child(2){opacity:0}
.hbg.open span:nth-child(3){transform:translateY(-7px) rotate(-45deg)}
.mob{display:none;position:fixed;top:70px;left:0;right:0;
  background:var(--white);padding:20px 24px;
  box-shadow:0 8px 32px rgba(0,0,0,.1);z-index:999;
  flex-direction:column;gap:4px}
.mob.open{display:flex}
.mob a{font-family:'Poppins',sans-serif;font-size:.95rem;font-weight:500;
  padding:12px 0;border-bottom:1px solid #f0f0f0;color:var(--black)}
.mob .btn{margin-top:12px;width:100%}

/* HERO */
.hero{min-height:100vh;display:flex;align-items:center;
  background:var(--black);position:relative;overflow:hidden;padding-top:70px}
.hero-bg{position:absolute;inset:0;
  background:radial-gradient(ellipse 60% 50% at 80% 50%,rgba(255,210,48,.12) 0%,transparent 70%),
  radial-gradient(ellipse 40% 60% at 10% 80%,rgba(255,210,48,.06) 0%,transparent 60%)}
.hero-grid{position:absolute;inset:0;
  background-image:linear-gradient(rgba(255,210,48,.04) 1px,transparent 1px),
  linear-gradient(90deg,rgba(255,210,48,.04) 1px,transparent 1px);
  background-size:56px 56px}
.hero-inner{position:relative;z-index:2;display:grid;
  grid-template-columns:1fr 1fr;gap:60px;align-items:center;padding:80px 0}
.hero-badge{display:inline-flex;align-items:center;gap:8px;
  background:rgba(255,210,48,.1);border:1px solid rgba(255,210,48,.25);
  color:var(--yellow);font-family:'Poppins',sans-serif;font-size:.75rem;
  font-weight:600;letter-spacing:.08em;text-transform:uppercase;
  padding:6px 16px;border-radius:999px;margin-bottom:26px}
.hero-badge::before{content:'';width:6px;height:6px;background:var(--yellow);
  border-radius:50%;animation:pulse 2s infinite}
@keyframes pulse{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.5;transform:scale(1.4)}}
.hero-title{font-family:'Poppins',sans-serif;
  font-size:clamp(2.2rem,4vw,3.8rem);font-weight:800;
  color:var(--white);line-height:1.1;margin-bottom:22px}
.hero-title .hl{color:var(--yellow)}
.hero-sub{font-size:clamp(.95rem,1.5vw,1.1rem);color:rgba(255,255,255,.6);
  line-height:1.8;margin-bottom:36px}
.hero-btns{display:flex;gap:14px;flex-wrap:wrap}
.hero-stats{display:flex;gap:32px;margin-top:52px;padding-top:32px;
  border-top:1px solid rgba(255,255,255,.07);flex-wrap:wrap}
.stat-num{font-family:'Poppins',sans-serif;font-size:2rem;font-weight:700;
  color:var(--yellow);display:block;line-height:1}
.stat-lbl{font-size:.75rem;color:rgba(255,255,255,.4);margin-top:4px;display:block}
.hero-visual{display:flex;flex-direction:column;gap:16px;align-items:flex-end}
.hero-card{background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.08);
  border-radius:20px;padding:24px;width:100%;backdrop-filter:blur(10px)}
.hero-card-top{display:flex;align-items:center;gap:14px;margin-bottom:16px}
.hero-card-ico{width:48px;height:48px;background:var(--yellow);border-radius:12px;
  display:flex;align-items:center;justify-content:center;font-size:1.4rem;flex-shrink:0}
.hero-card-title{font-family:'Poppins',sans-serif;font-size:.95rem;
  font-weight:600;color:var(--white)}
.hero-card-sub{font-size:.8rem;color:rgba(255,255,255,.4)}
.hero-card-bar{height:6px;background:rgba(255,255,255,.08);border-radius:999px;overflow:hidden}
.hero-card-fill{height:100%;background:var(--yellow);border-radius:999px;
  animation:fillbar 2s ease forwards}
@keyframes fillbar{from{width:0}to{width:var(--w)}}
.hero-card2{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.hero-mini{background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.08);
  border-radius:14px;padding:18px;text-align:center}
.hero-mini-num{font-family:'Poppins',sans-serif;font-size:1.5rem;font-weight:700;
  color:var(--yellow);display:block}
.hero-mini-lbl{font-size:.72rem;color:rgba(255,255,255,.4);margin-top:2px;display:block}

/* SOBRE */
.sobre{padding:100px 0;background:var(--white)}
.sobre-grid{display:grid;grid-template-columns:1fr 1fr;gap:70px;align-items:center}
.sobre-visual{position:relative}
.sobre-box{background:var(--black);border-radius:24px;padding:40px;
  color:var(--white);position:relative;overflow:hidden}
.sobre-box::before{content:'';position:absolute;top:-40px;right:-40px;
  width:180px;height:180px;background:var(--yellow);border-radius:50%;opacity:.06}
.sobre-box::after{content:'';position:absolute;bottom:-60px;left:-40px;
  width:140px;height:140px;background:var(--yellow);border-radius:50%;opacity:.04}
.sobre-icon{font-size:3.2rem;margin-bottom:20px;display:block}
.sobre-box h3{font-family:'Poppins',sans-serif;font-size:1.25rem;
  font-weight:700;margin-bottom:12px}
.sobre-box p{font-size:.88rem;color:rgba(255,255,255,.55);line-height:1.8}
.sobre-float{position:absolute;bottom:-20px;right:24px;
  background:var(--yellow);border-radius:14px;padding:16px 20px;
  box-shadow:0 12px 32px rgba(255,210,48,.3)}
.sobre-float strong{font-family:'Poppins',sans-serif;font-size:1.4rem;
  font-weight:700;color:var(--black);display:block}
.sobre-float span{font-size:.73rem;color:var(--black);opacity:.6}
.sobre-content .s-title,.sobre-content .s-sub{text-align:left;margin-left:0}
.feats{display:flex;flex-direction:column;gap:20px;margin-top:8px}
.feat{display:flex;align-items:flex-start;gap:16px}
.feat-icon{width:44px;height:44px;background:var(--yellow);border-radius:12px;
  display:flex;align-items:center;justify-content:center;
  font-size:1.2rem;flex-shrink:0;box-shadow:0 4px 12px rgba(255,210,48,.3)}
.feat h4{font-family:'Poppins',sans-serif;font-size:.93rem;
  font-weight:600;margin-bottom:4px}
.feat p{font-size:.83rem;color:var(--gray3);line-height:1.6}

/* COBERTURA */
.cobertura{padding:100px 0;background:var(--black)}
.cobertura .tag{background:rgba(255,210,48,.12);color:var(--yellow)}
.cobertura .s-title{color:var(--white)}
.cobertura .s-sub{color:rgba(255,255,255,.45)}
.cob-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:44px}
.cob-card{background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.07);
  border-radius:16px;padding:28px 24px;transition:all var(--trans);text-align:center}
.cob-card:hover{border-color:var(--yellow);background:rgba(255,210,48,.05);
  transform:translateY(-4px)}
.cob-ico{font-size:2rem;margin-bottom:12px;display:block}
.cob-card h4{font-family:'Poppins',sans-serif;font-size:.95rem;
  font-weight:600;color:var(--white);margin-bottom:6px}
.cob-card p{font-size:.8rem;color:rgba(255,255,255,.4);line-height:1.6}
.cob-note{text-align:center;margin-top:32px;font-size:.82rem;color:rgba(255,255,255,.3)}

/* PLANOS */
.planos{padding:100px 0;background:var(--gray)}
.plans-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:24px;margin-top:44px}
.plan{background:var(--white);border-radius:22px;padding:34px 28px;
  border:2px solid transparent;transition:all var(--trans);
  position:relative;overflow:hidden}
.plan::before{content:'';position:absolute;top:0;left:0;right:0;
  height:4px;background:#eee;transition:background var(--trans)}
.plan:hover{border-color:var(--yellow);transform:translateY(-6px);box-shadow:var(--shadow2)}
.plan:hover::before,.plan.featured::before{background:var(--yellow)}
.plan.featured{background:var(--black);color:var(--white);
  border-color:var(--yellow);transform:translateY(-8px);
  box-shadow:0 16px 48px rgba(0,0,0,.25)}
.plan-badge{display:inline-block;background:var(--yellow);color:var(--black);
  font-family:'Poppins',sans-serif;font-size:.68rem;font-weight:700;
  letter-spacing:.07em;text-transform:uppercase;padding:3px 12px;
  border-radius:999px;margin-bottom:18px}
.plan-name{font-family:'Poppins',sans-serif;font-size:1.3rem;font-weight:700;margin-bottom:6px}
.plan-desc{font-size:.83rem;color:var(--gray3);margin-bottom:8px;line-height:1.6}
.plan.featured .plan-desc{color:rgba(255,255,255,.5)}
.plan-volume{display:inline-block;background:rgba(255,210,48,.12);
  color:#b8860b;font-family:'Poppins',sans-serif;font-size:.72rem;font-weight:600;
  padding:3px 10px;border-radius:999px;margin-bottom:20px}
.plan.featured .plan-volume{background:rgba(255,210,48,.2);color:var(--yellow)}
.plan-price{margin-bottom:24px;padding-bottom:24px;border-bottom:1px solid #eee}
.plan.featured .plan-price{border-color:rgba(255,255,255,.1)}
.cur{font-family:'Poppins',sans-serif;font-size:.95rem;font-weight:600;
  vertical-align:top;margin-top:8px;display:inline-block}
.amt{font-family:'Poppins',sans-serif;font-size:3rem;font-weight:800;line-height:1}
.per{font-size:.78rem;color:var(--gray2);display:block;margin-top:4px}
.plan.featured .per{color:rgba(255,255,255,.35)}
.plan-feats{display:flex;flex-direction:column;gap:11px;margin-bottom:28px}
.plan-feat{display:flex;align-items:center;gap:10px;font-size:.85rem}
.chk{width:20px;height:20px;background:var(--yellow);border-radius:50%;
  display:flex;align-items:center;justify-content:center;
  font-size:.62rem;font-weight:700;color:var(--black);flex-shrink:0}
.plan.featured .plan-feat{color:rgba(255,255,255,.82)}
.plan-note{text-align:center;font-size:.78rem;color:var(--gray2);margin-top:36px}

/* COMO FUNCIONA */
.como{padding:100px 0;background:var(--white)}
.steps{display:grid;grid-template-columns:repeat(4,1fr);
  gap:28px;margin-top:44px;position:relative}
.steps::before{content:'';position:absolute;top:30px;left:10%;
  width:80%;height:2px;
  background:linear-gradient(90deg,var(--yellow),rgba(255,210,48,.1));z-index:0}
.step{text-align:center;position:relative;z-index:1}
.step-num{width:56px;height:56px;background:var(--yellow);border-radius:50%;
  display:flex;align-items:center;justify-content:center;
  font-family:'Poppins',sans-serif;font-size:1.2rem;font-weight:700;
  color:var(--black);margin:0 auto 18px;border:4px solid var(--white);
  box-shadow:0 0 0 2px var(--yellow);transition:transform var(--trans)}
.step:hover .step-num{transform:scale(1.12)}
.step-ico{font-size:1.5rem;margin-bottom:4px}
.step h3{font-family:'Poppins',sans-serif;font-size:.92rem;font-weight:600;margin-bottom:6px}
.step p{font-size:.81rem;color:var(--gray3);line-height:1.6}

/* DEPOIMENTOS */
.deps{padding:100px 0;background:var(--gray)}
.deps-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;margin-top:44px}
.dep-card{background:var(--white);border-radius:18px;padding:28px;
  border:2px solid transparent;transition:all var(--trans)}
.dep-card:hover{border-color:var(--yellow);transform:translateY(-4px);box-shadow:var(--shadow2)}
.dep-stars{color:var(--yellow);font-size:1rem;margin-bottom:14px;letter-spacing:2px}
.dep-text{font-size:.87rem;color:var(--gray3);line-height:1.75;margin-bottom:20px;font-style:italic}
.dep-author{display:flex;align-items:center;gap:12px}
.dep-avatar{width:40px;height:40px;background:var(--yellow);border-radius:50%;
  display:flex;align-items:center;justify-content:center;
  font-family:'Poppins',sans-serif;font-size:.95rem;font-weight:700;color:var(--black)}
.dep-name{font-family:'Poppins',sans-serif;font-size:.85rem;font-weight:600}
.dep-role{font-size:.75rem;color:var(--gray2)}

/* FAQ */
.faq{padding:100px 0;background:var(--white)}
.faq-list{max-width:720px;margin:44px auto 0}
.faq-item{background:var(--gray);border-radius:14px;margin-bottom:10px;
  border:2px solid transparent;overflow:hidden;transition:border-color var(--trans)}
.faq-item.open{border-color:var(--yellow);background:var(--white)}
.faq-q{display:flex;align-items:center;justify-content:space-between;
  padding:20px 24px;cursor:pointer;font-family:'Poppins',sans-serif;
  font-size:.9rem;font-weight:600;gap:14px;user-select:none}
.faq-ico{width:28px;height:28px;background:var(--white);border-radius:50%;
  display:flex;align-items:center;justify-content:center;
  flex-shrink:0;font-size:.95rem;transition:all var(--trans)}
.faq-item.open .faq-ico{background:var(--yellow);transform:rotate(45deg)}
.faq-a{max-height:0;overflow:hidden;transition:max-height .4s ease}
.faq-a-inner{padding:0 24px 20px;font-size:.86rem;color:var(--gray3);line-height:1.75}
.faq-item.open .faq-a{max-height:200px}

/* CONTATO */
.contato{padding:100px 0;background:var(--black)}
.contato .tag{background:rgba(255,210,48,.12);color:var(--yellow)}
.contato-grid{display:grid;grid-template-columns:1fr 1.3fr;gap:60px;align-items:start}
.contato-info h3{font-family:'Poppins',sans-serif;font-size:1.6rem;
  font-weight:700;margin-bottom:14px;color:var(--white)}
.contato-info>p{font-size:.88rem;color:rgba(255,255,255,.45);line-height:1.8;margin-bottom:36px}
.c-items{display:flex;flex-direction:column;gap:20px}
.c-item{display:flex;align-items:center;gap:14px}
.c-icon{width:44px;height:44px;background:rgba(255,210,48,.12);border:1px solid rgba(255,210,48,.2);
  border-radius:12px;display:flex;align-items:center;justify-content:center;
  font-size:1.1rem;flex-shrink:0}
.c-item strong{font-family:'Poppins',sans-serif;font-size:.76rem;font-weight:600;
  display:block;text-transform:uppercase;letter-spacing:.05em;
  margin-bottom:2px;color:rgba(255,255,255,.4)}
.c-item span{font-size:.88rem;color:var(--white)}
.form-card{background:var(--white);border-radius:22px;padding:40px}
.form-card h4{font-family:'Poppins',sans-serif;font-size:1.1rem;font-weight:700;margin-bottom:26px}
.fg{margin-bottom:16px}
.fg label{display:block;font-family:'Poppins',sans-serif;font-size:.74rem;
  font-weight:600;text-transform:uppercase;letter-spacing:.06em;margin-bottom:6px;color:var(--gray3)}
.fg input,.fg select{width:100%;padding:13px 16px;border:2px solid #e8e8e8;
  border-radius:11px;font-family:'Inter',sans-serif;font-size:.9rem;
  color:var(--black);background:var(--gray);
  transition:border-color var(--trans);outline:none;appearance:none}
.fg input:focus,.fg select:focus{border-color:var(--yellow);background:var(--white)}
.form-ok{display:none;text-align:center;padding:32px}
.form-ok.show{display:block}
.form-ok .ok-ico{font-size:2.8rem;margin-bottom:14px}
.form-ok h4{font-family:'Poppins',sans-serif;margin-bottom:8px;font-size:1.1rem}
.form-ok p{font-size:.86rem;color:var(--gray3)}

/* TOAST */
.toast{position:fixed;bottom:100px;left:50%;transform:translateX(-50%) translateY(20px);
  background:var(--black);color:var(--white);font-family:'Poppins',sans-serif;
  font-size:.85rem;padding:12px 24px;border-radius:999px;
  box-shadow:var(--shadow2);opacity:0;transition:all .4s ease;z-index:9999;
  white-space:nowrap;pointer-events:none}
.toast.show{opacity:1;transform:translateX(-50%) translateY(0)}

/* FOOTER */
footer{background:#050505;color:var(--white);padding:60px 0 0}
.foot-grid{display:grid;grid-template-columns:1.6fr 1fr 1fr;gap:48px;padding-bottom:48px}
.foot-logo-wrap{margin-bottom:16px}
.foot-logo-img{height:44px;width:auto}
.foot-brand p{font-size:.84rem;color:rgba(255,255,255,.35);line-height:1.8;max-width:280px}
.foot-col h5{font-family:'Poppins',sans-serif;font-size:.74rem;font-weight:600;
  text-transform:uppercase;letter-spacing:.1em;color:rgba(255,255,255,.25);margin-bottom:20px}
.foot-col ul{display:flex;flex-direction:column;gap:11px}
.foot-col ul a{font-size:.84rem;color:rgba(255,255,255,.5);transition:color var(--trans)}
.foot-col ul a:hover{color:var(--yellow)}
.foot-bottom{border-top:1px solid rgba(255,255,255,.05);padding:20px 0;
  display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px}
.foot-bottom p{font-size:.74rem;color:rgba(255,255,255,.2)}

/* WA FLOAT */
.wa-float{position:fixed;bottom:28px;right:28px;z-index:2000;display:flex;align-items:center;gap:10px}
.wa-tip{background:var(--black);color:var(--white);font-family:'Poppins',sans-serif;
  font-size:.78rem;font-weight:500;padding:8px 16px;border-radius:999px;white-space:nowrap;
  box-shadow:var(--shadow);opacity:0;transform:translateX(8px);
  transition:all var(--trans);pointer-events:none}
.wa-float:hover .wa-tip{opacity:1;transform:translateX(0)}
.wa-btn{width:58px;height:58px;background:#25D366;border-radius:50%;
  display:flex;align-items:center;justify-content:center;
  box-shadow:0 4px 24px rgba(37,211,102,.45);
  transition:all var(--trans);animation:wab 3.5s ease infinite}
.wa-btn:hover{transform:scale(1.08)}
.wa-btn svg{width:28px;height:28px;fill:#fff}
@keyframes wab{0%,88%,100%{transform:scale(1)}92%{transform:scale(1.09)}96%{transform:scale(.97)}}

/* REVEAL */
.rv{opacity:0;transform:translateY(28px);transition:opacity .65s ease,transform .65s ease}
.rv.on{opacity:1;transform:translateY(0)}
.d1{transition-delay:.1s}.d2{transition-delay:.2s}
.d3{transition-delay:.3s}.d4{transition-delay:.4s}

/* RESPONSIVE */
@media(max-width:1024px){
  .hero-inner{grid-template-columns:1fr}
  .hero-visual{display:none}
  .plans-grid{grid-template-columns:repeat(2,1fr)}
  .plan.featured{transform:none}
  .steps{grid-template-columns:repeat(2,1fr)}
  .steps::before{display:none}
  .deps-grid{grid-template-columns:repeat(2,1fr)}
  .cob-grid{grid-template-columns:repeat(2,1fr)}
  .foot-grid{grid-template-columns:1fr 1fr}
}
@media(max-width:768px){
  .nav-links,.nav-d{display:none}
  .hbg{display:flex}
  .sobre-grid{grid-template-columns:1fr}
  .sobre-visual{display:none}
  .plans-grid{grid-template-columns:1fr}
  .contato-grid{grid-template-columns:1fr}
  .deps-grid{grid-template-columns:1fr}
  .cob-grid{grid-template-columns:1fr}
  .foot-grid{grid-template-columns:1fr;gap:32px}
  .foot-bottom{flex-direction:column;text-align:center}
}
@media(max-width:480px){
  .hero-btns{flex-direction:column}
  .hero-btns .btn{width:100%}
  .steps{grid-template-columns:1fr}
  .form-card{padding:24px}
}
</style>
</head>
<body>

<nav id="nav">
<div class="container">
<div class="nav-inner">
  <a href="#inicio" class="logo">
    <img class="logo-branca" src="/static/logo-branca.png" alt="Jet Livery"/>
    <img class="logo-preta" src="/static/logo-preta.png" alt="Jet Livery"/>
  </a>
  <ul class="nav-links">
    <li><a href="#sobre">Sobre</a></li>
    <li><a href="#planos">Planos</a></li>
    <li><a href="#como">Como Funciona</a></li>
    <li><a href="#cobertura">Cobertura</a></li>
    <li><a href="#faq">FAQ</a></li>
    <li><a href="#contato">Contato</a></li>
  </ul>
  <a href="https://wa.me/5551992516345?text=Ol%C3%A1!%20Vim%20pelo%20site!" class="btn btn-wa nav-d" target="_blank" rel="noopener">
    <svg viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
    WhatsApp
  </a>
  <button class="hbg" id="hbg"><span></span><span></span><span></span></button>
</div>
</div>
</nav>

<div class="mob" id="mob">
  <a href="#sobre">Sobre</a>
  <a href="#planos">Planos</a>
  <a href="#como">Como Funciona</a>
  <a href="#cobertura">Cobertura</a>
  <a href="#faq">FAQ</a>
  <a href="#contato">Contato</a>
  <a href="https://wa.me/5551992516345?text=Ol%C3%A1!%20Vim%20pelo%20site!" class="btn btn-wa" target="_blank" rel="noopener">
    <svg viewBox="0 0 24 24" style="width:18px;height:18px;fill:#fff"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
    Chamar no WhatsApp
  </a>
</div>

<section class="hero" id="inicio">
  <div class="hero-bg"></div>
  <div class="hero-grid"></div>
  <div class="container">
    <div class="hero-inner">
      <div class="hero-content">
        <div class="hero-badge">📍 Tramandaí e região</div>
        <h1 class="hero-title">Na velocidade<br>que você <span class="hl">precisa</span></h1>
        <p class="hero-sub">Tele-entrega humanizada e eficiente para restaurantes, mercados, farmácias e negócios locais. Planos semanais que crescem com sua demanda.</p>
        <div class="hero-btns">
          <a href="https://wa.me/5551992516345?text=Ol%C3%A1!%20Quero%20contratar%20a%20Jet%20Livery!" class="btn btn-wa" target="_blank" rel="noopener">
            <svg viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
            Falar no WhatsApp
          </a>
          <a href="#planos" class="btn btn-outline-white">Ver Planos →</a>
        </div>
        <div class="hero-stats">
          <div><span class="stat-num">3</span><span class="stat-lbl">Planos disponíveis</span></div>
          <div><span class="stat-num">19</span><span class="stat-lbl">Motoboys disponíveis</span></div>
          <div><span class="stat-num">24h</span><span class="stat-lbl">Suporte ativo</span></div>
          <div><span class="stat-num">100%</span><span class="stat-lbl">Dedicação</span></div>
        </div>
      </div>
      <div class="hero-visual">
        <div class="hero-card">
          <div class="hero-card-top">
            <div class="hero-card-ico">🏍️</div>
            <div>
              <div class="hero-card-title">Entrega em andamento</div>
              <div class="hero-card-sub">Deck Pasteis</div>
            </div>
          </div>
          <div class="hero-card-bar">
            <div class="hero-card-fill" style="--w:78%"></div>
          </div>
          <div style="display:flex;justify-content:space-between;margin-top:8px">
            <span style="font-size:.72rem;color:rgba(255,255,255,.35)">Coletado</span>
            <span style="font-size:.72rem;color:var(--yellow);font-weight:600">78% — chegando</span>
          </div>
        </div>
        <div class="hero-card2">
          <div class="hero-mini">
            <span class="hero-mini-num">7.483</span>
            <span class="hero-mini-lbl">Entregas este mês</span>
          </div>
          <div class="hero-mini">
            <span class="hero-mini-num">19</span>
            <span class="hero-mini-lbl">Motoboys disponíveis</span>
          </div>
          <div class="hero-mini">
            <span class="hero-mini-num">5★</span>
            <span class="hero-mini-lbl">Avaliação média</span>
          </div>
          <div class="hero-mini">
            <span class="hero-mini-num">⚡</span>
            <span class="hero-mini-lbl">Tempo médio 25 min</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="sobre" id="sobre">
<div class="container">
<div class="sobre-grid">
  <div class="sobre-visual rv">
    <div class="sobre-box">
      <span class="sobre-icon">🏍️</span>
      <h3>Entrega com propósito</h3>
      <p>A JetLivery nasceu do desejo de trazer uma abordagem mais humana e eficiente para o serviço de tele-entrega. Com uma equipe dedicada, buscamos oferecer mais do que apenas entregas rápidas — oferecemos tranquilidade para o seu negócio.</p>
    </div>
    <div class="sobre-float"><strong>Tramandaí</strong><span>Rio Grande do Sul</span></div>
  </div>
  <div class="sobre-content">
    <span class="tag">Sobre nós</span>
    <h2 class="s-title rv d1">Mais que entregas,<br>conexões reais</h2>
    <p class="s-sub rv d2" style="margin-bottom:28px">Somos uma empresa local que entende as necessidades dos negócios de Tramandaí. Nosso diferencial está no atendimento próximo e no compromisso com cada entrega.</p>
    <div class="feats">
      <div class="feat rv d1"><div class="feat-icon">⚡</div><div><h4>Agilidade garantida</h4><p>Entregas realizadas com rapidez e eficiência, respeitando o tempo do seu cliente.</p></div></div>
      <div class="feat rv d2"><div class="feat-icon">🎯</div><div><h4>Suporte personalizado</h4><p>Atendimento direto via WhatsApp, sem fila, sem robôs. Falamos com você de verdade.</p></div></div>
      <div class="feat rv d3"><div class="feat-icon">📱</div><div><h4>App de rastreamento</h4><p>Acompanhe cada entrega em tempo real pelo nosso aplicativo exclusivo para clientes.</p></div></div>
      <div class="feat rv d4"><div class="feat-icon">🤝</div><div><h4>Parceria de verdade</h4><p>Tratamos seu negócio como se fosse nosso. Cada entrega importa para nós.</p></div></div>
    </div>
  </div>
</div>
</div>
</section>

<section class="cobertura" id="cobertura">
<div class="container">
  <div class="tc">
    <span class="tag">Área de cobertura</span>
    <h2 class="s-title rv">Onde atuamos</h2>
    <p class="s-sub rv d1">Atendemos Tramandaí e cidades vizinhas. Consulte disponibilidade para sua região.</p>
  </div>
  <div class="cob-grid">
    <div class="cob-card rv d1"><span class="cob-ico">📍</span><h4>Tramandaí</h4><p>Atendimento completo em toda a cidade, incluindo bairros afastados.</p></div>
    <div class="cob-card rv d2"><span class="cob-ico">📍</span><h4>Imbé</h4><p>Cobertura total na cidade vizinha, com tempo de resposta rápido.</p></div>
    <div class="cob-card rv d3"><span class="cob-ico">📍</span><h4>Osório</h4><p>Atendimento disponível sob consulta para demandas específicas.</p></div>
  </div>
  <p class="cob-note rv">Não encontrou sua cidade? <a href="https://wa.me/5551992516345" target="_blank" style="color:var(--yellow)">Fale conosco</a> e verificamos a disponibilidade.</p>
</div>
</section>

<section class="planos" id="planos">
<div class="container">
  <div class="tc">
    <span class="tag">Planos</span>
    <h2 class="s-title rv">Escolha o plano ideal<br>para seu negócio</h2>
    <p class="s-sub rv d1">Planos semanais baseados na sua demanda. Comece pequeno e escale conforme cresce.</p>
  </div>
  <div class="plans-grid">
    <div class="plan rv d1">
      <p class="plan-name">Start</p>
      <p class="plan-desc">Ideal para negócios que estão começando com tele-entrega.</p>
      <p class="plan-volume">100 entregas por semana</p>
      <div class="plan-price"><span class="cur">R$</span><span class="amt">100</span><span class="per">por semana</span></div>
      <ul class="plan-feats">
        <li class="plan-feat"><span class="chk">✓</span>100 entregas semanais</li>
        <li class="plan-feat"><span class="chk">✓</span>Horários combinados</li>
        <li class="plan-feat"><span class="chk">✓</span>Suporte via WhatsApp</li>
        <li class="plan-feat"><span class="chk">✓</span>App de rastreamento</li>
      </ul>
      <a href="https://wa.me/5551992516345?text=Ol%C3%A1!%20Tenho%20interesse%20no%20*Plano%20Start*!" class="btn btn-outline" style="width:100%" target="_blank" rel="noopener">Escolher Plano Start</a>
    </div>
    <div class="plan featured rv d2">
      <span class="plan-badge">⭐ Mais Popular</span>
      <p class="plan-name">Pro</p>
      <p class="plan-desc">Para negócios com fluxo regular de entregas e clientes frequentes.</p>
      <p class="plan-volume">200 entregas por semana</p>
      <div class="plan-price"><span class="cur">R$</span><span class="amt">250</span><span class="per">por semana</span></div>
      <ul class="plan-feats">
        <li class="plan-feat"><span class="chk">✓</span>200 entregas semanais</li>
        <li class="plan-feat"><span class="chk">✓</span>Prioridade nas chamadas</li>
        <li class="plan-feat"><span class="chk">✓</span>Suporte dedicado</li>
        <li class="plan-feat"><span class="chk">✓</span>Relatório semanal</li>
        <li class="plan-feat"><span class="chk">✓</span>App de rastreamento</li>
      </ul>
      <a href="https://wa.me/5551992516345?text=Ol%C3%A1!%20Tenho%20interesse%20no%20*Plano%20Pro*!" class="btn btn-yellow" style="width:100%" target="_blank" rel="noopener">Escolher Plano Pro</a>
    </div>
    <div class="plan rv d3">
      <p class="plan-name">Growth</p>
      <p class="plan-desc">Para alta demanda. Máxima prioridade e melhor custo por entrega.</p>
      <p class="plan-volume">Entregas ilimitadas</p>
      <div class="plan-price"><span class="cur">R$</span><span class="amt">350</span><span class="per">por semana</span></div>
      <ul class="plan-feats">
        <li class="plan-feat"><span class="chk">✓</span>Entregas ilimitadas</li>
        <li class="plan-feat"><span class="chk">✓</span>Máxima prioridade</li>
        <li class="plan-feat"><span class="chk">✓</span>Gestor de conta dedicado</li>
        <li class="plan-feat"><span class="chk">✓</span>Relatório detalhado</li>
        <li class="plan-feat"><span class="chk">✓</span>App de rastreamento</li>
      </ul>
      <a href="https://wa.me/5551992516345?text=Ol%C3%A1!%20Tenho%20interesse%20no%20*Plano%20Growth*!" class="btn btn-dark" style="width:100%" target="_blank" rel="noopener">Escolher Plano Growth</a>
    </div>
  </div>
  <p class="plan-note rv">* Os prazos e condições de entrega podem variar conforme região e disponibilidade.</p>
</div>
</section>

<section class="como" id="como">
<div class="container">
  <div class="tc">
    <span class="tag">Processo</span>
    <h2 class="s-title rv">Simples, rápido<br>e sem complicações</h2>
    <p class="s-sub rv d1">Em 4 passos você já tem um serviço de entregas profissional para o seu negócio.</p>
  </div>
  <div class="steps">
    <div class="step rv d1"><div class="step-num">1</div><div class="step-ico">📋</div><h3>Escolha seu plano</h3><p>Selecione o plano que melhor atende ao volume de entregas do seu negócio.</p></div>
    <div class="step rv d2"><div class="step-num">2</div><div class="step-ico">💬</div><h3>Fale conosco</h3><p>Entre em contato pelo WhatsApp e configure os detalhes do serviço.</p></div>
    <div class="step rv d3"><div class="step-num">3</div><div class="step-ico">📱</div><h3>Baixe o app</h3><p>Fornecemos acesso ao nosso aplicativo para você acompanhar cada entrega em tempo real.</p></div>
    <div class="step rv d4"><div class="step-num">4</div><div class="step-ico">📈</div><h3>Acompanhe e cresça</h3><p>Monitore o serviço pelo app e escale seu plano conforme a demanda aumenta.</p></div>
  </div>
</div>
</section>

<section class="deps" id="depoimentos">
<div class="container">
  <div class="tc">
    <span class="tag">Depoimentos</span>
    <h2 class="s-title rv">O que nossos clientes dizem</h2>
    <p class="s-sub rv d1">A satisfação de quem usa a Jet Livery é o nosso maior resultado.</p>
  </div>
  <div class="deps-grid">
    <div class="dep-card rv d1">
      <div class="dep-stars">★★★★★</div>
      <p class="dep-text">"A Jet Livery transformou nossa operação. Entregas pontuais, motoboys educados e o app de rastreamento é incrível. Nossos clientes adoraram!"</p>
      <div class="dep-author"><div class="dep-avatar">M</div><div><div class="dep-name">Mara</div><div class="dep-role">Shekinah</div></div></div>
    </div>
    <div class="dep-card rv d2">
      <div class="dep-stars">★★★★★</div>
      <p class="dep-text">"Desde que contratamos a Jet Livery, as reclamações de atraso zeraram. O suporte é rápido e o custo-benefício é excelente para o nosso volume."</p>
      <div class="dep-author"><div class="dep-avatar">F</div><div><div class="dep-name">Fagner</div><div class="dep-role">Mariah Hamburgueria</div></div></div>
    </div>
    <div class="dep-card rv d3">
      <div class="dep-stars">★★★★★</div>
      <p class="dep-text">"Para farmácia, pontualidade é tudo. A Jet Livery entende isso. Atendimento humanizado, profissional e com rastreamento em tempo real."</p>
      <div class="dep-author"><div class="dep-avatar">M</div><div><div class="dep-name">Mauricio</div><div class="dep-role">Farmácia Sanar</div></div></div>
    </div>
  </div>
</div>
</section>

<section class="faq" id="faq">
<div class="container">
  <div class="tc">
    <span class="tag">FAQ</span>
    <h2 class="s-title rv">Perguntas frequentes</h2>
    <p class="s-sub rv d1">Tire suas dúvidas. Transparência é o nosso compromisso.</p>
  </div>
  <div class="faq-list">
    <div class="faq-item rv"><div class="faq-q">Como funcionam os planos semanais?<span class="faq-ico">+</span></div><div class="faq-a"><div class="faq-a-inner">Nossos planos são cobrados semanalmente. O Start inclui 100 entregas, o Pro inclui 200 entregas e o Growth é ilimitado. Você escolhe, entra em contato pelo WhatsApp e ativamos o serviço.</div></div></div>
    <div class="faq-item rv d1"><div class="faq-q">Como acompanho as entregas em tempo real?<span class="faq-ico">+</span></div><div class="faq-a"><div class="faq-a-inner">Fornecemos acesso ao nosso aplicativo exclusivo onde você acompanha cada entrega em tempo real, desde a coleta até a entrega ao cliente final.</div></div></div>
    <div class="faq-item rv d2"><div class="faq-q">Quais regiões são atendidas?<span class="faq-ico">+</span></div><div class="faq-a"><div class="faq-a-inner">Atendemos Tramandaí, Imbé e região. Não há limitação por raio de distância dentro das áreas de cobertura. Para outras cidades, consulte disponibilidade pelo WhatsApp.</div></div></div>
    <div class="faq-item rv d3"><div class="faq-q">O que acontece se eu ultrapassar o limite de entregas?<span class="faq-ico">+</span></div><div class="faq-a"><div class="faq-a-inner">No plano Start (100 

    <div class="faq-item rv d3"><div class="faq-q">O que acontece se eu ultrapassar o limite de entregas?<span class="faq-ico">+</span></div><div class="faq-a"><div class="faq-a-inner">No plano Start (100 entregas) e Pro (200 entregas), entregas excedentes são cobradas individualmente. No plano Growth as entregas são ilimitadas sem custo extra.</div></div></div>
    <div class="faq-item rv d4"><div class="faq-q">Posso mudar de plano?<span class="faq-ico">+</span></div><div class="faq-a"><div class="faq-a-inner">Sim! Upgrade ou downgrade a qualquer momento. Basta falar conosco pelo WhatsApp e ajustaremos para a semana seguinte sem burocracia.</div></div></div>
    <div class="faq-item rv"><div class="faq-q">Como funciona o suporte?<span class="faq-ico">+</span></div><div class="faq-a"><div class="faq-a-inner">Suporte via WhatsApp, direto, rápido e sem robôs. Você fala com pessoas reais que entendem seu negócio e resolvem qualquer situação com agilidade.</div></div></div>
  </div>
</div>
</section>

<section class="contato" id="contato">
<div class="container">
  <div class="contato-grid">
    <div class="contato-info rv">
      <span class="tag">Contato</span>
      <h3>Pronto para começar?</h3>
      <p>Entre em contato agora e descubra como a Jet Livery pode transformar a logística do seu negócio em Tramandaí.</p>
      <div class="c-items">
        <div class="c-item"><div class="c-icon">📱</div><div><strong>WhatsApp</strong><span>(51) 99251-6345</span></div></div>
        <div class="c-item"><div class="c-icon">✉️</div><div><strong>E-mail</strong><span>jetliveryentregas@gmail.com</span></div></div>
        <div class="c-item"><div class="c-icon">📍</div><div><strong>Endereço</strong><span>Coca Barcelos 13 – Tramandaí / RS</span></div></div>
      </div>
    </div>
    <div class="form-card rv d1">
      <h4>Solicite uma proposta</h4>
      <div id="fWrap">
        <form id="cForm" method="POST" action="https://formspree.io/f/mzdkpyyl">
          <div class="fg"><label>Seu nome</label><input type="text" name="nome" placeholder="João Silva" required></div>
          <div class="fg"><label>WhatsApp</label><input type="tel" name="whatsapp" placeholder="(51) 99999-9999" required></div>
          <div class="fg"><label>E-mail</label><input type="email" name="email" placeholder="joao@email.com" required></div>
          <div class="fg"><label>Cidade</label><input type="text" name="cidade" placeholder="Tramandaí" required></div>
          <div class="fg">
            <label>Plano de interesse</label>
            <select name="plano" required>
              <option value="">Selecione...</option>
              <option value="Start">Plano Start – R$ 100/semana</option>
              <option value="Pro">Plano Pro – R$ 250/semana</option>
              <option value="Growth">Plano Growth – R$ 350/semana</option>
              <option value="Duvida">Ainda não sei</option>
            </select>
          </div>
          <button type="submit" class="btn btn-yellow" style="width:100%;margin-top:8px">Enviar solicitação →</button>
        </form>
      </div>
      <div class="form-ok" id="fOk">
        <div class="ok-ico">✅</div>
        <h4>Mensagem enviada!</h4>
        <p>Entraremos em contato pelo WhatsApp em breve. Obrigado!</p>
      </div>
    </div>
  </div>
</div>
</section>

<footer>
<div class="container">
  <div class="foot-grid">
    <div class="foot-brand">
      <div class="foot-logo-wrap">
        <img class="foot-logo-img" src="/static/logo-branca.png" alt="Jet Livery"/>
      </div>
      <p>Tele-entrega humanizada e eficiente para negócios em Tramandaí e região.</p>
    </div>
    <div class="foot-col">
      <h5>Navegação</h5>
      <ul>
        <li><a href="#sobre">Sobre</a></li>
        <li><a href="#planos">Planos</a></li>
        <li><a href="#como">Como Funciona</a></li>
        <li><a href="#cobertura">Cobertura</a></li>
        <li><a href="#faq">FAQ</a></li>
        <li><a href="#contato">Contato</a></li>
      </ul>
    </div>
    <div class="foot-col">
      <h5>Contato</h5>
      <ul>
        <li><a href="https://wa.me/5551992516345" target="_blank" rel="noopener">📱 (51) 99251-6345</a></li>
        <li><a href="mailto:jetliveryentregas@gmail.com">✉️ jetliveryentregas@gmail.com</a></li>
        <li><a href="#contato">📍 Tramandaí – RS</a></li>
      </ul>
    </div>
  </div>
  <div class="foot-bottom">
    <p>© 2025 Jet Livery. Todos os direitos reservados.</p>
    <p>Prazos e condições podem variar conforme região e disponibilidade.</p>
  </div>
</div>
</footer>

<div class="wa-float">
  <span class="wa-tip">Fale conosco agora!</span>
  <a href="https://wa.me/5551992516345?text=Ol%C3%A1!%20Vim%20pelo%20site!" class="wa-btn" target="_blank" rel="noopener" aria-label="WhatsApp">
    <svg viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
  </a>
</div>

<div class="toast" id="toast"></div>

<script>
window.addEventListener('scroll',()=>{
  document.getElementById('nav').classList.toggle('scrolled',scrollY>40)
})
const hbg=document.getElementById('hbg'),mob=document.getElementById('mob')
hbg.addEventListener('click',()=>{hbg.classList.toggle('open');mob.classList.toggle('open')})
mob.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{
  hbg.classList.remove('open');mob.classList.remove('open')
}))
document.querySelectorAll('.faq-q').forEach(q=>{
  q.addEventListener('click',()=>{
    const it=q.parentElement,was=it.classList.contains('open')
    document.querySelectorAll('.faq-item').forEach(i=>i.classList.remove('open'))
    if(!was) it.classList.add('open')
  })
})
const obs=new IntersectionObserver(e=>{
  e.forEach(x=>{if(x.isIntersecting) x.target.classList.add('on')})
},{threshold:.12})
document.querySelectorAll('.rv').forEach(el=>obs.observe(el))
function showToast(msg){
  const t=document.getElementById('toast')
  t.textContent=msg;t.classList.add('show')
  setTimeout(()=>t.classList.remove('show'),3000)
}
document.getElementById('cForm').addEventListener('submit',async function(e){
  e.preventDefault()
  const fd=new FormData(this)
  const btn=this.querySelector('button[type=submit]')
  btn.textContent='Enviando...'
  btn.disabled=true
  try{
    const r=await fetch('https://formspree.io/f/mzdkpyyl',{
      method:'POST',
      body:fd,
      headers:{'Accept':'application/json'}
    })
    const d=await r.json()
    if(d.ok){
      document.getElementById('fWrap').style.display='none'
      document.getElementById('fOk').classList.add('show')
    } else {
      showToast('Erro ao enviar. Tente pelo WhatsApp!')
      btn.textContent='Enviar solicitação →'
      btn.disabled=false
    }
  }catch{
    showToast('Erro de conexão. Tente pelo WhatsApp!')
    btn.textContent='Enviar solicitação →'
    btn.disabled=false
  }
})
</script>
</body>
</html>"""


class JetLiveryHandler(BaseHTTPRequestHandler):

    def log_message(self, format, *args):
        print(f"[JetLivery] {self.address_string()} - {format % args}")

    def do_GET(self):
        if self.path in ('/', '/index.html'):
            self._serve_html()
        elif self.path.startswith('/static/'):
            self._serve_static()
        else:
            self._not_found()

    def _serve_static(self):
        base = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(base, self.path.lstrip('/'))
        if os.path.exists(path) and os.path.isfile(path):
            ext = path.split('.')[-1].lower()
            tipos = {'png':'image/png','jpg':'image/jpeg','jpeg':'image/jpeg','svg':'image/svg+xml','webp':'image/webp'}
            ct = tipos.get(ext, 'application/octet-stream')
            with open(path, 'rb') as f:
                b = f.read()
            self.send_response(200)
            self.send_header('Content-Type', ct)
            self.send_header('Content-Length', str(len(b)))
            self.end_headers()
            self.wfile.write(b)
        else:
            self._not_found()

    def do_POST(self):
        if self.path == '/contato':
            self._handle_contato()
        else:
            self._not_found()

    def _serve_html(self):
        content = HTML.encode('utf-8')
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.send_header('Content-Length', str(len(content)))
        self.end_headers()
        self.wfile.write(content)

    def _handle_contato(self):
        length = int(self.headers.get('Content-Length', 0))
        raw = self.rfile.read(length).decode('utf-8')
        dados = urllib.parse.parse_qs(raw)
        nome = dados.get('nome', [''])[0].strip()
        whats = dados.get('whatsapp', [''])[0].strip()
        email = dados.get('email', [''])[0].strip()
        cidade = dados.get('cidade', [''])[0].strip()
        plano = dados.get('plano', [''])[0].strip()
        if not all([nome, whats, email, cidade, plano]):
            self._json({'ok': False, 'erro': 'Campos obrigatórios faltando'}, 400)
            return
        self._salvar_lead(nome, whats, email, cidade, plano)
        print("\n" + "="*50)
        print("📩 NOVO LEAD RECEBIDO!")
        print(f"   Nome:    {nome}")
        print(f"   WhatsApp:{whats}")
        print(f"   E-mail:  {email}")
        print(f"   Cidade:  {cidade}")
        print(f"   Plano:   {plano}")
        print("="*50 + "\n")
        self._json({'ok': True, 'mensagem': 'Lead salvo com sucesso!'})

    def _salvar_lead(self, nome, whats, email, cidade, plano):
        linha = (
            f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')} | "
            f"Nome: {nome} | WhatsApp: {whats} | "
            f"Email: {email} | Cidade: {cidade} | Plano: {plano}\n"
        )
        with open('leads.txt', 'a', encoding='utf-8') as f:
            f.write(linha)

    def _json(self, data, status=200):
        body = json.dumps(data, ensure_ascii=False).encode('utf-8')
        self.send_response(status)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _not_found(self):
        self._json({'ok': False, 'erro': 'Rota não encontrada'}, 404)


def main():
    HOST = '0.0.0.0'
    PORT = int(os.environ.get('PORT', 8000))
    server = HTTPServer((HOST, PORT), JetLiveryHandler)
    print("=" * 50)
    print("🏍️  JET LIVERY — Servidor iniciado!")
    print(f"🌐  Acesse: http://{HOST}:{PORT}")
    print("📩  Leads salvos em: leads.txt")
    print("⛔  Para parar: Ctrl + C")
    print("=" * 50)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n\n⛔ Servidor encerrado.")
        server.server_close()


if __name__ == '__main__':
    main()