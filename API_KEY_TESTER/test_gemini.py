import os
from google import genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def test_connection():
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key or api_key == "your_api_key_here":
        print("Error: Please set your GEMINI_API_KEY in the .env file.")
        return

    # Initialize the client
    client = genai.Client(api_key=api_key)

    print("Testing connection to Gemini 2.5 Flash...")
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents="Hello! If you can read this, the API test is successful. Please reply with a short greeting."
        )
        print("\n--- Response from Gemini ---")
        print(response.text)
        print("----------------------------\n")
        print("API test completed successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    test_connection()
