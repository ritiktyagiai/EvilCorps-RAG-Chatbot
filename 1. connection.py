import os # Import the os module to access environment variables
from dotenv import load_dotenv 

load_dotenv() # read the .env file 

api_key = os.getenv("GEMINI_API_KEY")

print(f"Your Gemini API Key is: {api_key[0:4]}...")  # Print only the first  4 characters for security



