from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")  # Use environment variable

app = FastAPI()

class MathRequest(BaseModel):
    question: str

@app.post("/solve")
async def solve_math(req: MathRequest):
    prompt = f"Solve this math problem step by step: {req.question}"
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2
        )
        return {"solution": response['choices'][0]['message']['content']}
    except Exception as e:
        return {"error": str(e)}
