from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import google.generativeai as genai

# Initialize FastAPI app
app = FastAPI()

# Configure Gemini API Key
genai.configure(api_key="AIzaSyAmH0h_xuWsczg_O0QIcUlZpufLPwTYm58")

# Data Model for Request
class Sentence(BaseModel):
    line: str

class Paragraph(BaseModel):
    sentences: List[Sentence]

# In-memory storage for corrections
corrections = []

@app.post("/grammar-check")
async def check_grammar(paragraph: Paragraph):
    global corrections
    corrections = []

    # Load Gemini's model
    model = genai.GenerativeModel('gemini-pro')

    for sentence in paragraph.sentences:
        try:
            # Generate completion
            response = model.generate_content(f"Correct the grammar: {sentence.line}")
            corrected_text = response.text.strip()

            # Append to results
            corrections.append({
                "line": sentence.line,
                "correction": corrected_text
            })
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    return {"corrections": corrections}

@app.get("/get-corrections")
async def get_corrections():
    return {"corrections": corrections}
