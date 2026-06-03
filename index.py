from fastapi import FastAPI
from pydantic import BaseModel
import google.generativeai as genai

# Configure Gemini
genai.configure(api_key="AIzaSyBswUaSs098sqjXWEBpqrzBbW0jnqszSGQ")

model = genai.GenerativeModel("gemini-2.5-flash")

app = FastAPI(
    title="AI Code Assistant API",
    description="Generate code using Gemini",
    version="1.0.0"
)

class QuestionRequest(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(data: QuestionRequest):

    response = model.generate_content(data.question)

    return {
        "question": data.question,
        "answer": response.text
    }