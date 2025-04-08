from fastapi import FastAPI
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

Sirine_API_KEY = os.getenv("Sirine_API_KEY")

@app.get("/nasa")
def get_nasa_image():
    url = f"https://api.nasa.gov/planetary/apod?api_key={Sirine_API_KEY}"
    response = requests.get(url)
    return response.json()
