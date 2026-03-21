import os
import certifi
from dotenv import load_dotenv
from google import genai

load_dotenv()
os.environ["SSL_CERT_FILE"] = certifi.where()

print("GEMINI KEY FOUND:", os.getenv("GEMINI_API_KEY") is not None)
print("GEMINI KEY LENGTH:", len(os.getenv("GEMINI_API_KEY") or ""))
print("SSL_CERT_FILE =", os.getenv("SSL_CERT_FILE"))

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Say hello in one sentence."
)

print(response.text)