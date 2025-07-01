from fastapi import FastAPI, Request
import openai
import os

app = FastAPI()

@app.get("/")
def root():
    return {"message": "SceneCraft API is running"}

@app.post("/analyze")
async def analyze_scene(request: Request):
    body = await request.json()
    scene_text = body.get("scene_text", "")

    prompt = f"""Analyze the following movie scene in terms of:
1. Beat Structure
2. Emotional Arc
3. Scene Tone and Genre
4. Character Motivation
5. Realism Score
6. Subtext vs. Spoken Intent

Scene:
{scene_text}
"""

    openai.api_key = os.getenv("OPENAI_API_KEY")

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return {"analysis": response.choices[0].message["content"]}