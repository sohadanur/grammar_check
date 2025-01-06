from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import re
import google.generativeai as genai

# Initialize FastAPI app
app = FastAPI()

# Configure Gemini API Key
genai.configure(api_key="AIzaSyB6J2IHYr8L2ih8pOXgVwwxoixWNZRCtWI")  # Add your API key here

# Data Model for Request
class Paragraph(BaseModel):
    text: str

# In-memory storage for corrections
corrections = []

def split_into_sentences(paragraph: str) ->list[str]:
    """
    Splits a paragraph into individual sentences using regex.
    """
    sentence_endings = r'[.!?]'
    sentences = re.split(sentence_endings, paragraph)
    sentences = [s.strip() for s in sentences if s.strip()]  # Remove empty strings
    return sentences

@app.post("/grammar-check")
async def check_grammar(paragraph: Paragraph):
    global corrections
    corrections = []

    # Split paragraph into sentences
    sentences = split_into_sentences(paragraph.text)

    # Load Gemini's model
    try:
        model = genai.GenerativeModel('gemini-pro')
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to load model: {str(e)}")

    # Process each sentence
    for sentence in sentences:
        try:
            # Generate correction
            response = model.generate_content(f"Correct the grammar: {sentence}")
            corrected_text = response.text.strip()

            # Append to results
            corrections.append({
                "original": sentence,
                "correction": corrected_text
            })
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error processing sentence: {str(e)}")

    return {"corrections": corrections}

@app.get("/get-corrections")
async def get_corrections():
    return {"corrections": corrections}
