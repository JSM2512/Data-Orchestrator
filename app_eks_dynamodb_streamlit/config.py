import os
from dotenv import load_dotenv

class Config:
    def __init__(self):
        load_dotenv()
        
        # AWS Configuration
        self.AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
        self.AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
        self.AWS_REGION = os.getenv('AWS_REGION', 'us-east-1')
        
        # DynamoDB Configuration
        self.DYNAMODB_TABLE_NAME = os.getenv('DYNAMODB_TABLE_NAME', 'TaxiTripData')
        
        # Redis Configuration
        self.REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
        self.REDIS_PORT = int(os.getenv('REDIS_PORT', 6379))
        self.REDIS_PASSWORD = os.getenv('REDIS_PASSWORD', '')
        
        # S3 Configuration
        self.S3_BUCKET_NAME = os.getenv('S3_BUCKET_NAME')
        
        # App Configuration
        self.DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'