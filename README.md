# AI Chatbot Assistant 🤖

An interactive AI Chatbot web application built with **Flask**, **JavaScript**, and **Google Gemini API**.

---

## 🚀 Features

- **Frontend**: Clean and responsive chat UI built with HTML5, CSS3, and Vanilla JavaScript.
- **Backend API**: Python Flask server handling API requests and CORS.
- **AI Integration**: Powered by Google's latest Gemini models via the official `google-genai` SDK with automatic model fallbacks (`gemini-2.5-flash`, `gemini-1.5-flash`, `gemini-2.0-flash`).
- **Real-time Interaction**: Chat in real-time with instant responses, enter-key message submission, and scrolling conversation history.

---

## 📁 Project Structure

```
aiagent/
├── app.py          # Flask backend server & Gemini API integration
├── index.html      # Frontend chat interface
├── script.js       # Client-side JavaScript handling chat requests
├── main.css        # Custom styles
├── 1.txt           # Detailed code documentation and architecture explanation
└── README.md       # Project overview and setup guide
```

---

## 🛠️ Getting Started

### 1. Prerequisites

- Python 3.9+
- A Google Gemini API Key (get one from [Google AI Studio](https://aistudio.google.com/))

### 2. Installation

Clone the repository:
```bash
git clone https://github.com/134push/ai-chatbot.git
cd ai-chatbot
```

Install required Python packages:
```bash
pip install flask google-genai
```

### 3. Set API Key

In PowerShell (Windows):
```powershell
$env:GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
```

In Bash (macOS/Linux):
```bash
export GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
```

### 4. Run the Server

```bash
python app.py
```

### 5. Launch the Chatbot

Open `index.html` in your browser and start chatting!
