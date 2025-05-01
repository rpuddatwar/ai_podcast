# 🎙️ AI Podcast Generator

A full-stack application that uses **AI to generate podcast scripts** from any topic and then converts those scripts into audio using **ElevenLabs Text-to-Speech**. Built using **React (Vite)** for the frontend and **FastAPI** for the backend.

---

## 📁 Folder Structure

```
ai-podcast/
├── backend/                # FastAPI backend
│   ├── main.py             # API logic
│   ├── requirements.txt    # Python dependencies
│   └── env/                # Virtual environment (excluded from Git)
├── frontend/               # React (Vite) frontend
│   ├── index.html
│   └── src/
│       ├── App.js
│       └── main.js
├── .env/                   # Environment variables (excluded)
└── .gitignore              # Git ignore rules
```

---

## 🚀 Features

- 🧠 Generate AI-based podcast scripts from any topic using Hugging Face models
- 🔊 Convert scripts into realistic speech using ElevenLabs TTS API
- ⚡ Fast, responsive React interface powered by Vite
- 🌐 RESTful API with FastAPI backend
- 🎧 Streamlined process from input to audio playback

---

## 🛠️ Tech Stack

**Frontend**:  
- React (Vite)  
- JavaScript  
- Tailwind CSS *(optional)*  

**Backend**:  
- FastAPI  
- Python  
- `pydub`, `requests` for audio processing

**APIs**:  
- Hugging Face (Text Generation)  
- ElevenLabs (Text-to-Speech)

---

## 🔧 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-podcast.git
cd ai-podcast
```

### 2. Backend Setup (FastAPI)

```bash
cd backend
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate
pip install -r requirements.txt
```

Create a `.env` file in the `backend/` directory with your API keys:

```
HUGGINGFACE_API_KEY=your_huggingface_key
ELEVENLABS_API_KEY=your_elevenlabs_key
```

Start the backend server:

```bash
uvicorn main:app --reload
```

### 3. Frontend Setup (React + Vite)

```bash
cd ../frontend
npm install
npm run dev
```

Open your browser and visit:  
`http://localhost:5173`

---

## 📡 API Endpoints

- `POST /generate-script`  
  **Input**: `{ "topic": "Climate Change" }`  
  **Output**: `{ "script": "Generated podcast content..." }`

- `POST /generate-audio`  
  **Input**: `{ "script": "Some script text" }`  
  **Output**: `{ "audio": "base64-encoded-audio" }`

---

## 🧪 Sample Workflow

1. Enter a topic like `"The Future of Renewable Energy"`.
2. Click **Generate Script**.
3. Review and edit the script (optional).
4. Click **Convert to Audio**.
5. 🎧 Listen to your custom podcast episode!

---

## 📄 Recommended `.gitignore`

```gitignore
.env
.env/
backend/env/
__pycache__/
*.pyc
node_modules/
dist/
```

---

## 📜 License

This project is licensed under the **MIT License**.  
Feel free to use, modify, and share it as needed.

---

## 🙋‍♂️ Author

Made with ❤️ by **[Your Name]**  
🔗 [LinkedIn](https://linkedin.com/in/your-profile)  
🌐 [Portfolio](https://your-portfolio.com)

---

Would you like a version with badges, deployment (Vercel / Render) steps, or Docker support included?