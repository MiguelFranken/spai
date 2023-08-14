import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
HUGGINGFACEHUB_API_TOKEN = os.environ.get('HUGGINGFACEHUB_API_TOKEN')
LLM_MODEL_NAME = os.environ.get('LLM_MODEL_NAME', 'text-davinci-003')
REPORTS_DIR = '../reports'
PERSONA_NAME = os.environ.get('PERSONA_NAME', 'Claudia')
PARAGRAPH_LIMIT = int(os.getenv('PARAGRAPH_LIMIT', default=3))
MAX_REPORTS_TO_PROCESS = int(os.getenv("MAX_REPORTS_TO_PROCESS", 10))
ACCESSIBILITY_REPORTER_API = os.environ.get('ACCESSIBILITY_REPORTER_API')


if not OPENAI_API_KEY:
    raise ValueError("Please set the OPENAI_API_KEY in the .env file.")
