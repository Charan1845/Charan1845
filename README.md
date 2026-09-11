<h1 align="center">Hi, I'm Charan 👋</h1>

<h3 align="center">Python · Data Visualisation · Interactive Dashboards</h3>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com/?font=Fira+Code&weight=500&size=22&pause=1200&color=38BDAE&center=true&vCenter=true&width=620&lines=Building+data-driven+web+applications;Turning+messy+datasets+into+decisions;Solving+DSA+problems;Learning+system+design" alt="Typing SVG" />
</p>

---

## 👨‍💻 About Me

```yaml
Name:      Charan
Focus:     DSA, System Design
Building:  AI agents, interactive dashboards, and analytics tools
Learning:  DSA, System Design, backend development
Approach:  Fewer projects, finished properly
```

- 📊 I build **data-driven web applications** — mostly turning unstructured public datasets into interfaces people can explore and make decisions with.
- 🗺️ Recent work is **geospatial**: mapping drought risk across Telangana and healthcare capacity across India.
- 🔬 Completed the **Infosys Springboard Virtual Internship 6.0**, delivering a healthcare operations analytics platform as the capstone.
- 🧠 Currently going deeper on **DSA** and **system design**.
- 🎯 Focused on shipping fewer, more complete projects rather than many partial ones.

---

## 🛠️ Tech Stack

**Languages**  
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white) ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black) ![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge) ![C](https://img.shields.io/badge/C-A8B9CC?style=for-the-badge&logo=c&logoColor=black)

**Data & Visualisation**  
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white) ![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white) ![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white) ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge) ![Seaborn](https://img.shields.io/badge/Seaborn-4C72B0?style=for-the-badge) ![GeoPandas](https://img.shields.io/badge/GeoPandas-139C5A?style=for-the-badge&logo=geopandas&logoColor=white)

**Web & Machine Learning**  
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white) ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white) ![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white) ![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white) ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

**Backend & Databases**  
![Node.js](https://img.shields.io/badge/Node.js-5FA04E?style=for-the-badge&logo=nodedotjs&logoColor=white) ![Express](https://img.shields.io/badge/Express-000000?style=for-the-badge&logo=express&logoColor=white) ![REST APIs](https://img.shields.io/badge/REST_APIs-85EA2D?style=for-the-badge&logo=swagger&logoColor=black) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white) ![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)

**Tools & Hosting**  
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white) ![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white) ![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge) ![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white) ![Render](https://img.shields.io/badge/Render-000000?style=for-the-badge&logo=render&logoColor=white) ![Neon](https://img.shields.io/badge/Neon-00E599?style=for-the-badge&logo=neon&logoColor=black)

---
## 🚀 Featured Work

### 🧾 [LEKHA](https://github.com/Charan1845/lekha)

> *AI finance controller for multi-source settlement reconciliation — built for Razorpay merchants*

`Python` · `Llama 3.2 via Ollama` · `JavaScript` · `pytest`

- **Problem** — Razorpay settles orders in bundled lump sums days later, net of fees and GST. A merchant's bank statement shows one credit with no indication of which orders it covers — someone reconciles that by hand, daily.
- **Approach** — Tested the AI on the actual matching first: asking an LLM which orders summed to a bank line scored 0/9, even with retries. Deterministic Python scored 3/3, instantly. So code does every calculation; the LLM only writes the explanation for lines it can't resolve.
- **Evaluation** — A sealed answer key the agent is never allowed to open. 93.1% settlement match rate on held-out months, 0 false positives, every duplicate charge and stray credit caught. A 248-run sensitivity analysis over the assumed parameters gives the honest range: 76.3%–98.1%.
- **Engineering** — 127 tests, including one that runs identical inputs through both the Python and browser reconciliation engines and fails on any disagreement. Zero third-party Python dependencies. CI on GitHub Actions.

---

### 🌊 [GeoWater Analysis](https://github.com/Charan1845/geowater-analysis)

> *Geospatial water resource monitoring for Telangana*

`Python` · `Streamlit` · `GeoPandas` · `Plotly`

- **Problem** — Rainfall alone is a misleading drought signal. A district with poor rainfall but large reservoirs may be secure, while one with good rainfall and no storage stays vulnerable.
- **Approach** — Normalised monsoon rainfall and dam storage capacity to a 0–100 scale and combined them into a single drought index, so districts can be ranked against each other.
- **Features** — Interactive Plotly choropleth over district boundaries, click-through drill-down per district, covering all 33 Telangana districts across 2024–2025.
- **Finding** — Districts around Hyderabad with negligible reservoir storage score worst consistently, leaving them wholly dependent on same-year rainfall.

### 🏥 [PulseScore](https://github.com/Charan1845/healthcare-analytics-dashboard)

> *Interactive analytics platform for healthcare infrastructure planning across India*

`Python` · `Streamlit` · `Pandas` · `Plotly`

- **Problem** — Healthcare planning data arrives unstructured and fragmented, making it hard to assess hospital capacity, workforce availability and emergency preparedness.
- **Approach** — Consolidated infrastructure metrics, workforce indicators and readiness assessments into a single interactive Streamlit application.
- **Features** — Bed capacity and hospital-type analysis, emergency readiness scoring, region-level geographic coverage comparison, interactive filtering, dataset export.
- **Context** — Capstone project for the Infosys Springboard Virtual Internship 6.0, mentored by Mousami Shrivastava.

### 🔬 [Age & Gender Detection](https://github.com/Charan1845/Age-and-Gender-Recognition)

> *Estimates age and gender from a photo or a live camera capture*

`Python` · `Flask` · `OpenCV` · `TensorFlow` · `JavaScript`

- **Pipeline** — YuNet locates faces and returns five landmarks, each face is rotated onto a level eye axis, then a fine-tuned MobileNetV2 predicts age as a number and gender.
- **Detector choice** — YuNet over RetinaFace and MTCNN: within a few points on accuracy, roughly 100× faster on CPU, 340 KB, and no extra dependency. Accuracy that cannot run in real time is not accuracy you have.
- **Train/serve consistency** — the training set is re-cropped with the same detector the app uses at inference, so the model does not learn on one distribution and predict on another.
- **Full-stack** — Flask JSON API with a plain HTML/CSS/JS frontend; camera capture runs in the browser via `getUserMedia` so it still works when hosted.

### 🛒 [DevGear](https://github.com/Charan1845/ecommerce-website) — [live](https://devgear.onrender.com)

> *An online shop where the last item in stock can only be sold once*

`Node.js` · `Express` · `PostgreSQL` · `JavaScript` · `REST`

- **Problem** — Most shopping-cart projects read the stock, check it is enough, then subtract it. Between the read and the write a second buyer does the same read: both see one left, both are told yes, and the shop sells an item it does not have. It only appears under load, which is why it usually ships.
- **Approach** — Checkout does the check and the subtraction in a single statement, so the database tests the condition at the moment it writes; zero rows changed is how the second buyer learns they lost. The whole checkout runs in one transaction, so an order that fails halfway puts back the stock it had already taken.
- **Evaluation** — A test fires two simultaneous checkouts at the same last item and asserts that exactly one succeeds, that stock lands on zero rather than minus one, and that one order exists. Against PostgreSQL those requests genuinely overlap rather than being serialised by the runtime. 37 tests in all, covering pricing rules, access control, login rate limiting and payment signature verification.
- **Engineering** — REST API behind a login, bcrypt hashing, JWT in an httpOnly cookie, role-separated owner dashboard, cart and order history. SQLite locally and PostgreSQL deployed, behind one interface, so a fresh clone runs with nothing installed. Deployed on Render with a Neon database; first boot creates and seeds its own schema.

---

## 🎓 Experience

**Infosys Springboard — Virtual Internship 6.0**  
<sub>Applied software development · Mentor: Mousami Shrivastava</sub>

Built the Healthcare Operations Analytics Dashboard as the capstone deliverable, covering data cleaning, metric design and interactive visualisation.

---

## 📈 Where this is going

<sub>Fewer projects, finished properly — so every line here is something that exists, not something I read about.</sub>

| | Stage | What it actually produced |
|:--:|:---|:---|
| ✅ | Python, data analysis, visualisation | Two interactive dashboards, and a drought index mapped across Telangana |
| ✅ | A professional internship | Infosys Springboard 6.0 — healthcare analytics capstone delivered |
| ✅ | Machine learning, actually served | Age & Gender — detector chosen on latency, not only accuracy, and it runs in a browser |
| ✅ | Full stack, deployed | [DevGear](https://devgear.onrender.com) — REST API, PostgreSQL, payments, 40 tests, live |
| 🚧 | DSA and system design | The gap between *it works* and *it holds up under load* |
| ⏳ | Production habits | CI, observability, load testing — applied to the projects that already exist rather than to new ones |

---

<p align="center">
  <sub>
    <a href="https://github.com/Charan1845?tab=repositories">Repositories</a> &nbsp;·&nbsp;
    <a href="https://devgear.onrender.com">DevGear, live</a>
  </sub>
</p>
