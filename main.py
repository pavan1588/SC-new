from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import openai
import os

app = FastAPI()

# ✅ CORS FIX
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.get("/")
def root():
    return {"message": "SceneCraft API is running"}

@app.post("/analyze")
async def analyze_scene(request: Request):
    body = await request.json()
    scene_text = body.get("scene_text", "")

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{
            "role": "user",
            "content": f"Analyze this movie scene for narrative beats, tone, emotion and cinematic structure:\n{scene_text}"
        }]
    )

    return {"analysis": response.choices[0].message.content}
