import os
from dotenv import load_dotenv


def get_env_variable(var_name):
    """
    Retrieve the environment variable specified by var_name or raise an error if it is not set.
    """
    value = os.environ.get(var_name)
    if value is None:
        raise ValueError(f"Environment variable {var_name} is not set. Please set this variable in the .env file.")
    return value


# Load environment variables from .env file
env_path = os.environ.get('ENV_PATH')

if env_path:
    load_dotenv(dotenv_path="../" + env_path)
else:
    load_dotenv()

# Required environment variables (raise error if not set)
OPENAI_API_KEY = get_env_variable('OPENAI_API_KEY')
HUGGINGFACEHUB_API_TOKEN = get_env_variable('HUGGINGFACEHUB_API_TOKEN')
ACCESSIBILITY_REPORTER_API = get_env_variable('ACCESSIBILITY_REPORTER_API')

# Optional environment variables (with defaults)
LLM_MODEL_NAME = os.environ.get('LLM_MODEL_NAME', 'text-davinci-003')
REPORTS_DIR = '../reports'
PERSONA_NAME = os.environ.get('PERSONA_NAME', 'Claudia')
PARAGRAPH_LIMIT = int(os.getenv('PARAGRAPH_LIMIT', default=3))
MAX_REPORTS_TO_PROCESS = int(os.getenv("MAX_REPORTS_TO_PROCESS", 10))
