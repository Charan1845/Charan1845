<h1 align="center">Hi, I'm Charan 👋</h1>

<h3 align="center">Python · Data Visualisation · Interactive Dashboards</h3>

<p align="center">
  <img src="https://readme-typing-svg.demolab.com/?font=Fira+Code&weight=500&size=22&pause=1200&color=38BDAE&center=true&vCenter=true&width=620&lines=Building+data-driven+web+applications;Turning+messy+datasets+into+decisions;Solving+DSA+problems;Learning+system+design" alt="Typing SVG" />
</p>

---

## 👨‍💻 About Me

```yaml
name:      Charan
focus:     DSA, System Design
building:  AI agents, interactive dashboards, and analytics tools
learning:  DSA, System Design, backend development
approach:  Fewer projects, finished properly
```

- 📊 I build **data-driven web applications** — mostly turning unstructured public datasets into interfaces people can explore and make decisions with.
- 🗺️ Recent work is **geospatial**: mapping drought risk across Telangana and healthcare capacity across India.
- 🔬 Completed the **Infosys Springboard Virtual Internship 6.0**, delivering a healthcare operations analytics platform as the capstone.
- 🧠 Currently going deeper on **DSA** and **system design**.
- 🎯 Focused on shipping fewer, more complete projects rather than many partial ones.

---

## 🛠️ Tech Stack

**Languages**  
`Python` · `Java` · `JavaScript` · `SQL` · `C`

**Data & Visualisation**  
`Pandas` · `NumPy` · `Plotly` · `Matplotlib` · `Seaborn` · `GeoPandas`

**Web & Frameworks**  
`Streamlit` · `Flask` · `TensorFlow` · `OpenCV` · `HTML5` · `CSS3`

**Tools**  
`Git` · `GitHub` · `VS Code` · `Jupyter`

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

### 🛒 [E-Commerce UI](https://github.com/Charan1845/ecommerce-website) — *in progress*

> *Front-end storefront built from scratch without a framework*

`HTML5` · `CSS3` · `JavaScript`

Authentication screens complete. Catalogue, product pages and cart are next.

---

## 🎓 Experience

**Infosys Springboard — Virtual Internship 6.0**  
<sub>Applied software development · Mentor: Mousami Shrivastava</sub>

Built the Healthcare Operations Analytics Dashboard as the capstone deliverable, covering data cleaning, metric design and interactive visualisation.

---

## 📈 Roadmap

```text
MILESTONE 1  ████████████████████  Python & web fundamentals          ✅
MILESTONE 2  ████████████████████  Data analysis & visualisation      ✅
MILESTONE 3  ████████████████████  Professional internship            ✅
MILESTONE 4  ███████████████░░░░░  Full-stack applications            🚧
MILESTONE 5  ████████░░░░░░░░░░░░  DSA & System Design                🚧
MILESTONE 6  ████░░░░░░░░░░░░░░░░  Production-level products          ⏳
```

---

## 📚 Currently Learning

| Area | Focus |
|:---|:---|
| 🧮 **DSA** | Data structures, algorithms, problem solving |
| 🏗️ **System Design** | Scalability, architecture patterns, trade-offs |
| ⚙️ **Backend** | REST API design, databases, application architecture |
| 🚢 **Shipping** | Taking projects through to a deployable, documented state |
