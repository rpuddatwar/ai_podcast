# backend/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pydantic import BaseModel
import requests
import os
from dotenv import load_dotenv

load_dotenv()   

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    # allow_origins=["http://localhost:3001"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
HF_API_KEY = os.getenv("HF_API_KEY")  # <-- Make sure your .env has HF_API_KEY

class Topic(BaseModel):
    text: str

@app.post("/generate-podcast/")
def generate_podcast(topic: Topic):

    prompt = f"Generate a short podcast script about: {topic.text}"
    # prompt = f"Generate a detailed podcast script for a beginner audience about: {topic.text}. Include an engaging introduction, key concepts explained in simple terms, and a conclusion that wraps up the topic."
    # prompt = f"""
    # Generate a professional, engaging, and informative podcast script on the following topic: "{topic.text}".
    # The script should include an introduction, main points, and a conclusion. 
    # Make the tone conversational, friendly, and suitable for a general audience.
    # Include any relevant facts, insights, or anecdotes related to the topic.
    # """
    # prompt = (
    #     f"Generate a professional, engaging, and informative podcast script about: {topic.text}. "
    #     "The script should include an introduction, key points explained in simple terms, and a conclusion. "
    #     "Keep the tone friendly and conversational, suitable for a general audience."
    # )


    gpt_response = requests.post(
        "https://api-inference.huggingface.co/models/google/flan-t5-small",
        headers={"Authorization": f"Bearer {HF_API_KEY}"},
        json={"inputs": prompt}
    )

    # gpt_response = requests.post(
    #     "https://api-inference.huggingface.co/models/EleutherAI/gpt-neo-1.3B",
    #     headers={"Authorization": f"Bearer {HF_API_KEY}"},
    #     json={"inputs": prompt}
    # )
    print("response Code", gpt_response)


    try:
        script = gpt_response.json()[0]['generated_text']
        print("response text", script)
    except Exception:
        return {"error": "Failed to generate script from Hugging Face."}

# Convert Script
    voice_id = "21m00Tcm4TlvDq8ikWAM"  # Replace with valid voice ID if needed
    tts_response = requests.post(
        f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}",
        headers={
            "xi-api-key": ELEVENLABS_API_KEY,
            "Content-Type": "application/json"
        },
        json={
            "text": script,
            "voice_settings": {"stability": 0.5, "similarity_boost": 0.5}
        }
    )

    # if tts_response.status_code != 200:
    #     return {"error": "Failed to generate audio with ElevenLabs."}

    if tts_response.status_code != 200:
        return {
            "error": "Failed to generate audio with ElevenLabs.",
            "status_code": tts_response.status_code,
            "details": tts_response.json()
    }

    with open("podcast.mp3", "wb") as f:
        f.write(tts_response.content)

    return {"script": script, "audio_url": "http://localhost:8000/audio"}

@app.get("/audio")
def get_audio():
    return FileResponse("podcast.mp3", media_type="audio/mpeg")
