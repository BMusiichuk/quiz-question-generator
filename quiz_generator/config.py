import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

def get_openai_api_key() -> str:
    """
    Retrieve the OpenAI API key from an environment variable.
    If not found, fall back to reading it from 'openai_key.txt'.
    Raises an exception if the API key is not available.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if api_key:
        return api_key.strip()

    # Use openai_key.txt if the environment variable is not set
    try:
        with open("openai_key.txt", "r") as key_file:
            return key_file.read().strip()
    except FileNotFoundError:
        raise Exception("OpenAI API key not found. Please set it in the .env file or in openai_key.txt.")
