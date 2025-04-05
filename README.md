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

## 📌 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Installation](#-installation)
- [Usage](#-usage)
- [Future Scope](#-future-scope)
- [Contact](#-contact)

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
3. **Install required dependencies**
```
pip install -r requirements.txt
```
4. **Add your API key to the .env file**
```
GOOGLE_API_KEY='your_google_gemini_api_key'
```
5. **Run the application**
```
python app.py
```
6. **Visit the local server in your browser**
```
http://127.0.0.1:5000
```


## 🧪 Usage
Queska AI can be used by:

- 🧑‍🎓 Students — For practicing question papers
- 👩‍🏫 Tuition teachers & coaching institutes — To auto-generate test series
- 🏛️ Educational institutions — For creating question banks and mocks

*Usage Steps:-*

- Upload your syllabus (in .txt or .pdf format)
- Select your desired difficulty level
- Click "Generate"
- Instantly receive a complete question paper

## 🔮 Future Scope
- 📦 Export to PDF/Doc
- 📚 Support for predefined exam patterns (e.g., CBSE, UPSC, NEET, GATE)
- 🧩 Ability to choose between MCQs, short/long questions
- 🧑‍💼 User authentication & dashboards
- 🔎 Keyword-based or concept-based paper generation
- 🌐 Multilingual generation support

## 📬 Contact
*For queries, suggestions or collaboration:-*
- 📧 Email: dravin.ksharma@gmail.com
