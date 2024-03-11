import boto3 
from dotenv import load_dotenv
import os

AWS_DEFAULT_ACL = None
REGION = os.getenv("S3_REGION") 
ACCESS_KEY_ID = os.getenv("S3_ACCESS_KEY_ID") 
SECRET_ACCESS_KEY = os.getenv("S3_SECRET_ACCESS_KEY") 
PATH_IN_COMPUTER = '/Users/nithylesh/Downloads/check.png' 
BUCKET_NAME = 'recieptscanner' 
KEY = 'check.png' # file path in S3 

def upload_file_to_s3(file_path, bucket_name, key):
    """
    Uploads a file to an S3 bucket using AWS credentials and region from environment variables.

    Parameters:
    - file_path: Local path to the file to be uploaded.
    - bucket_name: Name of the S3 bucket to upload the file to.
    - key: The key (file path) in the S3 bucket.

    Returns:
    - None
    """
    # Load environment variables from .env file
    load_dotenv()

    # Get AWS credentials and region from environment variables
    region = os.getenv("S3_REGION")
    access_key_id = os.getenv("S3_ACCESS_KEY_ID")
    secret_access_key = os.getenv("S3_SECRET_ACCESS_KEY")

    # Create an S3 resource object
    s3_resource = boto3.resource(
        's3',
        region_name=region,
        aws_access_key_id=access_key_id,
        aws_secret_access_key=secret_access_key
    )

    # Upload the file to S3
    s3_resource.Bucket(bucket_name).put_object(
        Key=key,
        Body=open(file_path, 'rb')
    )

# Example usage:
if __name__ == "__main__":
    PATH_IN_COMPUTER = '/Users/nithylesh/Downloads/check.png'
    BUCKET_NAME = 'recieptscanner'
    KEY = 'check.png'  # file path in S3

    upload_file_to_s3(PATH_IN_COMPUTER, BUCKET_NAME, KEY)

