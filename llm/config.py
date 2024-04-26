import os
from dotenv import load_dotenv
load_dotenv()

class Config:


    def get_gemini_api_endpoint(self):
        return os.environ.get('GOOGLE_API_KEY')
    
    def get_openai_api_endpoint(self):
        return os.environ.get('OPENAI_API_KEY')
