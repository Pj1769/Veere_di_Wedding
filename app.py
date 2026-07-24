#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Our Wedding Story", layout="wide")

st.markdown("""
<style>
.block-container {padding-top: 1rem; padding-bottom: 1rem;}
</style>
""", unsafe_allow_html=True)

st.title("🟩 A Journey Through Life — Wedding Invitation")
st.caption("Scroll down after the animation to see your invite ✨")

BRIDE_NAME = st.sidebar.text_input("Bride's Name", "Pratiksha")
GROOM_NAME = st.sidebar.text_input("Groom's Name", "Sankalp")
WEDDING_DATE = st.sidebar.text_input("Wedding Date", "26th February 2027")
WEDDING_TIME = st.sidebar.text_input("Muhurat / Time", "6:30 PM onwards")
VENUE = st.sidebar.text_input("Venue", "Our Residence, Bhawanipatna")
FAMILY_LINE = st.sidebar.text_input("Awaiting your Grqacious Presence", "Sahoo Family")

html_code = f"""
<!DOCTYPE html>
<html>
<head>
<style>
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0;
    background: #7ec850;
    font-family: 'Courier New', monospace;
    overflow: hidden;
  }}
  #wrap {{
    position: relative;
    width: 100%;
    max-width: 900px;
    margin: 0 auto;
  }}
  canvas {{
    display: block;
    width: 100%;
    background: #7ec0de;
    image-rendering: pixelated;
    border: 6px solid #4a3418;
    border-radius: 4px;
  }}
  #caption {{
    text-align: center;
    color: #2b2b2b;
    background: rgba(255,255,255,0.85);
    font-weight: bold;
    font-size: 18px;
    padding: 8px;
    border: 3px solid #4a3418;
    margin-top: -6px;
    letter-spacing: 1px;
  }}
  #skipBtn {{
    position: absolute;
    top: 10px; right: 10px;
    background: #8b5a2b;
    color: #fff;
    border: 3px solid #4a3418;
    padding: 6px 12px;
    font-family: 'Courier New', monospace;
    font-weight: bold;
    cursor: pointer;
    z-index: 5;
  }}
  #invite {{
    display: none;
    max-width: 900px;
    margin: 20px auto;
    background: linear-gradient(#fff6e0, #ffe9b3);
    border: 8px solid #8b5a2b;
    box-shadow: 0 0 0 4px #4a3418 inset;
    padding: 30px;
    text-align: center;
    font-family: 'Courier New', monospace;
    color: #4a2e0a;
    image-rendering: pixelated;
    animation: fadeIn 1.5s ease-in;
  }}
  @keyframes fadeIn {{
    from {{opacity:0; transform: scale(0.9);}}
    to {{opacity:1; transform: scale(1);}}
  }}
  .block-divider {{
    display: flex;
    justify-content: center;
    gap: 6px;
    margin: 14px 0;
  }}
  .block-divider div {{
    width: 18px; height: 18px;
  }}
  .om {{ font-size: 40px; margin-bottom: 6px; }}
  .names {{
    font-size: 34px;
    font-weight: bold;
    letter-spacing: 2px;
    text-shadow: 2px 2px 0 #d9a441;
  }}
  .sub {{ font-size: 15px; margin: 6px 0; }}
  .details {{
    margin-top: 18px;
    font-size: 16px;
    line-height: 1.8;
  }}
  .pixel-heart {{
    font-size: 22px;
    margin: 10px 0;
  }}
</style>
</head>
<body>
<div id="wrap">
  <button id="skipBtn" onclick="skipToInvite()">Skip ▶</button>
  <canvas id="game" width="900" height="500"></canvas>
  <div id="caption">Loading story...</div>

  <div id="invite">
    <div class="om">🕉️</div>
    <div class="sub">{FAMILY_LINE}</div>
    <div class="block-divider">
      <div style="background:#3a7d1e;"></div><div style="background:#c9302c;"></div>
      <div style="background:#f0c419;"></div><div style="background:#3a7d1e;"></div>
      <div style="background:#c9302c;"></div>
    </div>
    <div class="names">{BRIDE_NAME} <span style="color:#c9302c;">&</span> {GROOM_NAME}</div>
    <div class="pixel-heart">💚🟥🟨 request the honor of your presence 🟨🟥💚</div>
    <div class="details">
      🗓️ <b>Date:</b> {WEDDING_DATE}<br>
      🕰️ <b>Time:</b> {WEDDING_TIME}<br>
      📍 <b>Venue:</b> {VENUE}
    </div>
    <div class="block-divider">
      <div style="background:#8b5a2b;"></div><div style="background:#4a3418;"></div>
      <div style="background:#8b5a2b;"></div><div style="background:#4a3418;"></div>
      <div style="background:#8b5a2b;"></div>
    </div>
    <div class="sub">Craft your blessings — build our forever 🧱💍</div>
  </div>
</div>

<script>
const canvas = document.getElementById('game');
const ctx = canvas.getContext('2d');
const caption = document.getElementById('caption');
const invite = document.getElementById('invite');
const W = canvas.width, H = canvas.height;

let t = 0;               // global frame timer
let sceneIndex = 0;
let sceneTimer = 0;
let animActive = true;

// ---------- helper: draw a blocky pixel character ----------
function drawChar(x, y, skinColor, shirtColor, pantColor, scale, walkPhase, faceRight) {{
  const s = scale;
  ctx.save();
  ctx.translate(x, y);
  if (!faceRight) {{ ctx.scale(-1,1); }}

  // legs (walk cycle)
  const legOffset = Math.sin(walkPhase) * 4 * s;
  ctx.fillStyle = pantColor;
  ctx.fillRect(-6*s, 20*s + legOffset, 5*s, 12*s);
  ctx.fillRect(1*s, 20*s - legOffset, 5*s, 12*s);

  // body
  ctx.fillStyle = shirtColor;
  ctx.fillRect(-7*s, 4*s, 14*s, 18*s);

  // arms
  ctx.fillStyle = skinColor;
  ctx.fillRect(-10*s, 6*s + Math.cos(walkPhase)*3*s, 4*s, 12*s);
  ctx.fillRect(6*s, 6*s - Math.cos(walkPhase)*3*s, 4*s, 12*s);

  // head
  ctx.fillStyle = skinColor;
  ctx.fillRect(-7*s, -12*s, 14*s, 14*s);

  // hair
  ctx.fillStyle = '#3b2314';
  ctx.fillRect(-7*s, -14*s, 14*s, 4*s);

  // eyes
  ctx.fillStyle = '#1a1a1a';
  ctx.fillRect(-3*s, -6*s, 2*s, 2*s);
  ctx.fillRect(2*s, -6*s, 2*s, 2*s);

  ctx.restore();
}}

function drawGroundBlocks(color1, color2, yBase) {{
  const size = 40;
  for (let i = -1; i < W/size + 1; i++) {{
    ctx.fillStyle = (i % 2 === 0) ? color1 : color2;
    ctx.fillRect(i*size, yBase, size, H - yBase);
  }}
}}

function drawSky(color) {{
  ctx.fillStyle = color;
  ctx.fillRect(0,0,W,H);
}}

function drawCloud(x,y) {{
  ctx.fillStyle = '#ffffff';
  ctx.fillRect(x, y, 60, 20);
  ctx.fillRect(x+15, y-12, 40, 15);
}}

function drawSun() {{
  ctx.fillStyle = '#f9d71c';
  ctx.fillRect(780, 40, 40, 40);
}}

function drawTree(x, y) {{
  ctx.fillStyle = '#6b4423';
  ctx.fillRect(x, y, 16, 40);
  ctx.fillStyle = '#3a7d1e';
  ctx.fillRect(x-16, y-40, 48, 40);
}}

function drawClassroomBG() {{
  ctx.fillStyle = '#d9c199';
  ctx.fillRect(0,0,W,H);
  ctx.fillStyle = '#8b5a2b';
  ctx.fillRect(0, H-80, W, 80); // floor
  // blackboard
  ctx.fillStyle = '#1b3a2f';
  ctx.fillRect(340, 60, 220, 100);
  ctx.fillStyle = '#fff';
  ctx.font = '16px monospace';
  ctx.fillText('A + B = ❤', 400, 115);
  // desks
  for (let i=0;i<3;i++) {{
    ctx.fillStyle = '#a9744f';
    ctx.fillRect(120 + i*250, 300, 60, 30);
  }}
}}

function drawMandap() {{
  // pillars
  ctx.fillStyle = '#e0b04c';
  ctx.fillRect(250, 150, 20, 280);
  ctx.fillRect(630, 150, 20, 280);
  // roof
  ctx.fillStyle = '#c9302c';
  ctx.fillRect(230, 130, 440, 30);
  // flowers on pillars
  for (let i=0;i<8;i++) {{
    ctx.fillStyle = i%2===0 ? '#f0c419':'#c9302c';
    ctx.fillRect(248, 160+i*30, 24, 10);
    ctx.fillRect(628, 160+i*30, 24, 10);
  }}
  // fire (agni)
  ctx.fillStyle = '#ff7300';
  ctx.fillRect(430, 380, 30, 20);
  ctx.fillStyle = '#ffcf40';
  ctx.fillRect(438, 365, 14, 20);
}}

// ---------- SCENES ----------
// Each scene: duration (frames), draw function(progress 0..1)
const scenes = [
  {{
    duration: 260,
    caption: "Once upon a time, in Block Elementary School... 🏫",
    draw: (p) => {{
      drawClassroomBG();
      const walk = t*0.15;
      drawChar(300 + Math.sin(t*0.02)*10, 260, '#e8b98c', '#3399ff', '#264a8b', 1.6, walk, true);
      drawChar(480 + Math.cos(t*0.02)*10, 260, '#f2c9a1', '#ff66aa', '#7a2b5e', 1.6, walk+1, false);
    }}
  }},
  {{
    duration: 260,
    caption: "They played together every single day 🧱⚒️",
    draw: (p) => {{
      drawSky('#7ec0de');
      drawCloud(80 + (t%400), 50);
      drawCloud(400 + (t%300), 90);
      drawSun();
      drawGroundBlocks('#5fae2f','#4f9a26', 380);
      drawTree(80, 380);
      drawTree(760, 380);
      const bx = 300 + Math.sin(t*0.08)*80;
      const gx = 550 + Math.cos(t*0.08)*80;
      drawChar(bx, 330, '#e8b98c', '#3399ff', '#264a8b', 1.8, t*0.2, bx < gx);
      drawChar(gx, 330, '#f2c9a1', '#ff66aa', '#7a2b5e', 1.8, t*0.2+1, gx < bx ? false: true);
    }}
  }},
  {{
    duration: 220,
    caption: "Years passed... they grew up, and grew apart ⏳",
    draw: (p) => {{
      drawSky('#b6d8e0');
      drawGroundBlocks('#5fae2f','#4f9a26', 380);
      // fading silhouettes moving apart
      const spread = p*250;
      ctx.globalAlpha = 1 - p*0.6;
      drawChar(450 - spread, 330, '#e8b98c', '#3399ff', '#264a8b', 1.8, t*0.15, false);
      drawChar(450 + spread, 330, '#f2c9a1', '#ff66aa', '#7a2b5e', 1.8, t*0.15+1, true);
      ctx.globalAlpha = 1;
    }}
  }},
  {{
    duration: 260,
    caption: "Until one day, fate brought them together again 🌆",
    draw: (p) => {{
      drawSky('#9fbfd8');
      drawGroundBlocks('#8a8a8a','#7a7a7a', 380);
      // buildings
      for (let i=0;i<5;i++) {{
        ctx.fillStyle = i%2===0 ? '#5c5c5c':'#707070';
        ctx.fillRect(60+i*170, 380-(120+i*20), 100, 120+i*20);
      }}
      const bx = 300 + Math.min(p*2,1)*100;
      const gx = 600 - Math.min(p*2,1)*100;
      drawChar(bx, 330, '#e8b98c', '#274690', '#1c2f57', 1.9, t*0.18, true);
      drawChar(gx, 330, '#f2c9a1', '#c23c76', '#6d1f4a', 1.9, t*0.18+1, false);
    }}
  }},
  {{
    duration: 260,
    caption: "They fell in love, block by block 💚",
    draw: (p) => {{
      drawSky('#ffd6a5');
      drawGroundBlocks('#5fae2f','#4f9a26', 380);
      drawTree(700, 380);
      drawChar(400, 330, '#e8b98c', '#274690', '#1c2f57', 1.9, t*0.1, true);
      drawChar(470, 330, '#f2c9a1', '#c23c76', '#6d1f4a', 1.9, t*0.1+1, false);
      // floating hearts
      for (let i=0;i<3;i++) {{
        const hy = 300 - ((t*2 + i*60) % 200);
        ctx.fillStyle = '#ff4d6d';
        ctx.fillRect(420 + i*15, hy, 10, 10);
        ctx.fillRect(415 + i*15, hy-5, 5,5);
        ctx.fillRect(430 + i*15, hy-5, 5,5);
      }}
    }}
  }},
  {{
    duration: 260,
    caption: "Adventures & trips followed — building memories together 🚂🏔️",
    draw: (p) => {{
      drawSky('#a7d8f0');
      drawGroundBlocks('#c2b280','#b0a070', 380);
      // mountains
      ctx.fillStyle = '#8899aa';
      ctx.beginPath();
      ctx.moveTo(0,380); ctx.lineTo(150,200); ctx.lineTo(300,380); ctx.fill();
      ctx.beginPath();
      ctx.moveTo(250,380); ctx.lineTo(430,150); ctx.lineTo(600,380); ctx.fill();
      const bx = 380 + Math.sin(t*0.1)*20;
      const gx = 440 + Math.sin(t*0.1+1)*20;
      drawChar(bx, 330, '#e8b98c', '#274690', '#1c2f57', 1.8, t*0.2, true);
      drawChar(gx, 330, '#f2c9a1', '#c23c76', '#6d1f4a', 1.8, t*0.2+1, false);
    }}
  }},
  {{
    duration: 300,
    caption: "And so, under the mandap, two blocks became one 🕉️💍",
    draw: (p) => {{
      drawSky('#f7d9a0');
      drawGroundBlocks('#c9a25a','#b8914e', 380);
      drawMandap();
      drawChar(400, 340, '#e8b98c', '#d4af37', '#3b2314', 1.7, 0, true);
      drawChar(500, 340, '#f2c9a1', '#c23c76', '#7a1f4a', 1.7, 0, false);
      // confetti
      for (let i=0;i<12;i++) {{
        const cx = (i*77 + t*3) % W;
        const cy = (i*53 + t*4) % H;
        ctx.fillStyle = ['#f0c419','#c9302c','#3a7d1e','#e0b04c'][i%4];
        ctx.fillRect(cx, cy, 6, 6);
      }}
    }}
  }},
];

function totalDuration() {{
  return scenes.reduce((a,s)=>a+s.duration, 0);
}}

function skipToInvite() {{
  animActive = false;
  canvas.style.display = 'none';
  caption.style.display = 'none';
  document.getElementById('skipBtn').style.display = 'none';
  invite.style.display = 'block';
}}

function loop() {{
  if (!animActive) return;
  t++;

  let scene = scenes[sceneIndex];
  sceneTimer++;
  const progress = sceneTimer / scene.duration;

  ctx.clearRect(0,0,W,H);
  scene.draw(progress);
  caption.innerText = scene.caption;

  if (sceneTimer >= scene.duration) {{
    sceneIndex++;
    sceneTimer = 0;
    if (sceneIndex >= scenes.length) {{
      skipToInvite();
      return;
    }}
  }}

  requestAnimationFrame(loop);
}}

loop();
</script>
</body>
</html>
"""

components.html(html_code, height=650, scrolling=False)

st.markdown("---")
st.info("💡 Tip: Use the sidebar to customize names, date, time and venue. The animation auto-plays through all scenes and then reveals the invitation. You can also click **Skip ▶** to jump straight to the invite.")

