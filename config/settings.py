import os
from dotenv import load_dotenv

load_dotenv()

MAX_ITERATIONS = int(os.getenv("MAX_ITERATIONS", 5))

GROQ_MODEL = os.getenv(
    "GROQ_MODEL",
    "llama-3.1-8b-instant"
)
