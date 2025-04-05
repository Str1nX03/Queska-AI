# 🧠 Queska AI - AI-Powered Question Paper Generator

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.12-blue.svg)
![Flask](https://img.shields.io/badge/flask-%5E2.3-lightgrey)
![Status](https://img.shields.io/badge/status-Production-green)
![Deployment](https://img.shields.io/badge/deployed%20on-Vercel-black)

---

> Queska AI is a Flask-based web application that enables users to upload a syllabus and generate question papers powered by Google's Gemini API. It allows customization of difficulty levels and will soon support various exam patterns.

---

## 🌐 Live Demo

🔗 **Deployed Link**: [https://queska-ai.vercel.app](https://queska-ai.vercel.app)

---

## 🖼️ Screenshots

> _Note: Dark and Light theme users can both experience a clean UI — the design adapts responsively._

![Home Page](https://via.placeholder.com/800x400?text=Queska+AI+Home+Page)
![Generated Paper](https://via.placeholder.com/800x400?text=Generated+Question+Paper)

---

## 📌 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Installation](#-installation)
- [Usage](#-usage)
- [Architecture](#-architecture)
- [API Integration](#-api-integration)
- [Future Scope](#-future-scope)
- [Contributing](#-contributing)
- [Contact](#-contact)
- [License](#-license)

---

## 🚀 Features

- 📝 Upload a syllabus file (PDF or text) and generate questions.
- 🎚 Choose difficulty level (easy, medium, hard).
- 📚 Supports usage across education sectors: students, tutors, institutions.
- 🧠 AI-generated content using Google Gemini API for natural and intelligent question creation.
- 📐 Upcoming support for exam pattern formats (CBSE, ICSE, NEET, etc.)
- 💾 Simple, minimal UI with focus on functionality and extensibility.
- ⚙️ Backend AI model interaction abstracted for seamless use.

---

## 🧰 Tech Stack

| Layer       | Technology             |
|-------------|------------------------|
| Frontend    | HTML, CSS              |
| Backend     | Python (Flask)         |
| AI Model    | Google Gemini API      |
| Deployment  | Vercel                 |
| Others      | dotenv, Requests, Flask-CORS |

---

## 💻 Installation

> Follow these steps to run the project locally:

### ✅ Prerequisites:
- Python 3.12+
- Google Gemini API key from: [https://aistudio.google.com/apikey](https://aistudio.google.com/apikey)

---

### 🔧 Setup Instructions:

1. **Clone the repository**
```
git clone https://github.com/Str1nX03/Queska-AI.git
cd Queska-AI
```
2. **Create a virtual environment**
```
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```
