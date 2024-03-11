from flask import Flask, jsonify
from gemini import generate_content_with_genai
from s3 import upload_file_to_s3
from tesseract import extract_text_without_numbers

app = Flask(__name__)

# Define routes
@app.route('/')
def index():
    return "Welcome to the Reciept Scan Sustainable Spend!"


@app.route('/generate_content')
def generate_content_api():
    input_text = "I will give you some product names classify whether they come under sustainable or non sustainable output should be of the form productname - sustainable / Non sustanable nothing else , the products are "
    generated_content = generate_content_with_genai(input_text)
    return jsonify({"generated_content": generated_content})


@app.route('/upload_to_s3')
def upload_to_s3_api():
    PATH_IN_COMPUTER = '/Users/nithylesh/Downloads/check.png'
    BUCKET_NAME = 'recieptscanner'
    KEY = 'check.png'
    upload_file_to_s3(PATH_IN_COMPUTER, BUCKET_NAME, KEY)
    return jsonify({"message": "File uploaded to S3 successfully!"})


@app.route('/extract_text')
def extract_text_api():
    image_path = 'grocery_reciept.png'
    extracted_words = extract_text_without_numbers(image_path)
    return jsonify({"extracted_words": extracted_words})


@app.route('/classify_bill')
def receipt_details():
    image_path = 'grocery_reciept.png'
    
    # Extract text from the image
    extracted_words = extract_text_without_numbers(image_path)

    # Generate content using extracted text
    input_text = "I will give you some product names classify whether they come under sustainable or non sustainable output should be of the form productname - sustainable / Non sustainable nothing else , classify them based on  the environmental impact of the product over its entire life cycle, the products are "
    final_text = input_text.join(extracted_words)
    generated_content = generate_content_with_genai(final_text)

    return generated_content

    


if __name__ == '__main__':
    app.run(debug=True)
