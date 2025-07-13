# 🎞️ PastForward

> *Blast From the Past: AI-powered memory playback with VHS nostalgia.*

**PastForward** is a smart video summarizer with a retro VCR-style interface. It analyzes long videos, extracts key moments using computer vision, and presents them in an 80s-inspired playback experience — complete with vintage scanlines, chunky buttons, and tape rewind effects.

---

## 🧠 Features

- 🎬 **AI-Powered Highlights** – Automatically detects key scenes (faces, motion, transitions).
- 📼 **VHS-Style UI** – VCR-style player with Rewind, Fast-Forward, and Play buttons.
- 🧪 **Scene Filtering** – Skips short/irrelevant scenes and focuses on real content.
- 💾 **Drag-and-Drop Upload** *(coming soon)* – Summarize your own memories.
- 🖥️ **Retro Visuals** – CRT-style flicker, scanlines, and timestamp overlays.

---

## 🛠️ Tech Stack

| Layer     | Technology                |
|-----------|---------------------------|
| Frontend  | React, Vite, Tailwind CSS |
| Backend   | Python, OpenCV, MoviePy   |
| Styling   | CSS + CRT FX              |
| Versioning| Git, GitHub               |

---

## ▶️ Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/niveaaa/PastForward.git
cd PastForward
```

### 2. Backend Setup

```bash
cd backend
python -m venv venv
# Windows
venv\\Scripts\\activate
# macOS/Linux
source venv/bin/activate

pip install -r requirements.txt
python summarizer.py
```

### 3. Frontend Setup

```bash
cd ../frontend
npm install
npm run dev
```

---

## 🧪 Upcoming Features

- Upload and summarize personal videos
- Scene timeline & chapter scrubber
- Export edited clip with VHS timestamp
- Voice-command navigation

---

### 🧑‍💻 Built With 💙 at OSDHack ‘25

