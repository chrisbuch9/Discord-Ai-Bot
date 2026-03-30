import os
import certifi
from dotenv import load_dotenv

load_dotenv() #reads .env file
os.environ["SSL_CERT_FILE"] = certifi.where() #sets SSL certificate file path for secure API requests

DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN") #grabs discord token from environment variables
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") #grabs Gemini API key from environment variables
