from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models import TextInput 
import openai
from dotenv import load_dotenv
import os


# FastAPI-App
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Erlaubt Anfragen von allen Ursprüngen
    allow_methods=["*"],  # Erlaubt alle HTTP-Methoden
    allow_headers=["*"],  # Erlaubt alle Header
)

# load the OpenAI-API-Key from the .env-file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")  

# check if you have the key
if not openai.api_key:
    raise ValueError("Der API-Schlüssel fehlt. Bitte füge ihn zur .env-Datei hinzu.")


# Endpoint for emotion Classification    
@app.post("/classify")
async def classify_emotion(input: TextInput):
    try:
        print("Vor Aufruf von openai.ChatCompletion.create")
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",  
            messages=[
                {"role": "system", "content": "You are a helpful assistant that analyzes emotions from text You will be given a text input and you should classify emotion form that. Only one emotion should be classified and your answer should be a one word emotion."},
                {"role": "user", "content": f"Classify the following emotion: {input.text}"}
            ],
            max_tokens=10,
        )
        print(f"OpenAI-Antwort: {response}")

        emotion = response.choices[0].message.content.strip()   #openAI will also send us a json file as response
        return {"emotion": emotion} 
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



