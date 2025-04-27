# backend/utils/rag_handler.py

from vertexai.preview.generative_models import GenerativeModel
import vertexai
from dotenv import load_dotenv
import os

# Load environment
load_dotenv()

PROJECT_ID = os.getenv("GCP_PROJECT_ID")
LOCATION = "us-central1"  # ✅ Use supported region!

# Initialize Vertex AI
vertexai.init(project=PROJECT_ID, location=LOCATION)

from google.generativeai import GenerativeModel

def generate_rag_response(prompt):
    model = GenerativeModel("gemini-1.5-pro")  # Using free Gemini 1.5
    response = model.generate_content(f"HerKey Guidance: {prompt}")
    return response.text
