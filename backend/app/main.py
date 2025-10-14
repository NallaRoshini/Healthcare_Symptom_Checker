from fastapi import FastAPI, HTTPException
from .schemas import SymptomRequest, SymptomResponse
from .llm_client import query_llm
from .utils import build_prompt
from .database import engine, SessionLocal
from .models import Base, QueryHistory
import os
from fastapi.middleware.cors import CORSMiddleware
import json


app = FastAPI(title="Healthcare Symptom Checker")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or ["http://localhost:5173"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Create DB tables
Base.metadata.create_all(bind=engine)

@app.post("/api/check", response_model=SymptomResponse)
async def check_symptoms(request: SymptomRequest):
    text = request.text.strip()
    if not text:
        raise HTTPException(status_code=400, detail="Please provide symptom text.")

    messages = build_prompt(text)

    try:
        content = await query_llm(messages)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"LLM Error: {str(e)}")

    # --- JSON parsing block ---
    try:
        data = json.loads(content)
        probable = data.get("probable_conditions", "N/A")
        recs = data.get("recommendations", "N/A")
        disclaimer = data.get("disclaimer", "Educational purposes only.")
    except Exception as e:
        print("⚠️ JSON Parse Error:", e)
        probable, recs, disclaimer = "N/A", "N/A", "Educational purposes only."

    # Save in DB (optional)
    db = SessionLocal()
    entry = QueryHistory(input_text=text, response_text=content)
    db.add(entry)
    db.commit()
    db.close()

    return SymptomResponse(
        probable_conditions=probable,
        recommendations=recs,
        disclaimer=disclaimer,
    )

@app.get("/")
def home():
    return {"message": "Healthcare Symptom Checker API is running ✅"}
