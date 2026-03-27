from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

MODEL_NAME = "llama-3.1-8b-instant"

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)