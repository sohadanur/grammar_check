# grammar_check
Grammar check using Gemini's model: gemini pro and fastapi. 
Worked on vscode.

To get gemini_api_key: https://www.youtube.com/watch?v=ywPDnh4T2TA&t=1s 

JSOn format to be written in the post request for grammar_correction.py: 
{
    "sentences":[
         {"line": "This is apples"},
         {"line": "birds flies over sky!"}
    ]
}

JSOn format to be written in the post request for gram_check.py: 

{
  "text": "The bird are flies. Skies is blue. She do likes you."
}

JSOn format to be written in the post request for gram_paraphrase_spelling_check.py:

http://127.0.0.1:8000/process-text
{
  "sentences": [
    {"line": "She is going to the store. I hav a speling mistake. She like shoping. She radiate positeev energi"}
  ]
}

http://127.0.0.1:8000/grammar-check

{
  "sentences": [
    {"line": "She are going to the store."}
  ]
}


#Things that needs to be installed: 

pip install fastapi

pip install uvicorn

pip install python-multipart

pip install openai

pip install generativeai

pip install IPython 

pip install pydantic 

pip install

