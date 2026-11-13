import os # Import the os module to access environment variables
from dotenv import load_dotenv 
from google import genai
from google.genai.errors import APIError

load_dotenv() # read the .env file 

api_key = os.getenv("GEMINI_API_KEY")

# print(f"Your Gemini API Key is: {api_key[0:4]}...")  # Print only the first  4 characters for security

client = genai.Client(api_key=api_key) # Create a Gemini client using the API key


try:
    response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain why the sky is blue in one sentence."
    )

    # Print generated text
    print(response.text)
    
except APIError as e:
    if e.status_code == 401:
        print("Error: Unauthorized. Please check your API key.")
    elif e.status_code == 403:
        print("Error: Forbidden. You do not have permission to access this resource.")
    else:
        print(f"An error occurred: {e}")        