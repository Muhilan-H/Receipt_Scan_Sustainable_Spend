import google.generativeai as genai
from dotenv import load_dotenv
import os

def generate_content_with_genai(input_text):
    """
    Generates content using the Google Generative AI (GenAI) API.

    Parameters:
    - input_text: Text to be processed by the Generative AI model.

    Returns:
    - Generated content based on the input text.
    """
    # Load environment variables from .env file
    load_dotenv()

    # Get Google API key from environment variable
    google_api_key = os.getenv("SAP_GOOGLE_API_KEY")

    # Configure GenAI with the Google API key
    genai.configure(api_key=google_api_key)

    # Initialize the GenerativeModel
    model = genai.GenerativeModel('gemini-pro')

    # Generate content based on the input text
    response = model.generate_content(input_text)

    return response.text

# Example usage:
if __name__ == "__main__":
    input_text = "I will give you some product names classify whether they come under sustainable or non sustainable output should be of the form productname - sustainable / Non sustanable nothing else , the products are as follows soap, wooden tooth brush, chocolate"
    generated_content = generate_content_with_genai(input_text)
    print(generated_content)
