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

#Things that needs to be installed: 

pip install fastapi

pip install uvicorn

pip install python-multipart

pip install openai

pip install generativeai

pip install IPython 

pip install pydantic 

pip install

