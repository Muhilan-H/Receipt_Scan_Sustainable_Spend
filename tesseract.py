import pytesseract
from PIL import Image
import re

def extract_text_without_numbers(image_path):
    """
    Extract text from an image using Tesseract OCR and remove words containing numeric characters.

    Parameters:
    - image_path: Path to the image file.

    Returns:
    - A list of words extracted from the image without words containing numeric characters.
    """

    img = Image.open(image_path)

    # Use Tesseract OCR to extract text
    text = pytesseract.image_to_string(img)

    # Define a regular expression pattern to match words containing numeric characters
    pattern = r'\b[\d.]+\b'

    # Split the text without numbers into phrases based on numbers
    phrases = re.split(pattern, text)

    # Remove empty strings from the phrases list and split on consecutive newline characters
    final_phrases = []
    for phrase in phrases:
        # Split the phrase into smaller phrases whenever two consecutive newline characters occur
        smaller_phrases = [p.strip() for p in phrase.split('\n') if p.strip()]
        final_phrases.extend(smaller_phrases)

    return final_phrases

# Example usage:
if __name__ == "__main__":
    image_path = 'grocery_reciept.png'
    extracted_words = extract_text_without_numbers(image_path)
    for word in extracted_words:
        print(word)
