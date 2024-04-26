import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from llm.config import Config
from PIL import Image

class Retreive:
    def __init__(self) -> None:
        self.gemini_api_key = Config().get_gemini_api_endpoint()
        self.openai_api_key = Config().get_openai_api_endpoint()

        genai.configure(api_key = self.gemini_api_key)
        self.model = genai.GenerativeModel('models/gemini-pro-vision')

    
    def retrieval_image_content(self, image_path):
        image = Image.open(image_path)
        response = self.model.generate_content(['Give me detail about image in breif', image])

        print(response.text)
        return response.text
    
    def gemini_llm(self):
        
        llm = ChatGoogleGenerativeAI(model='gemini-pro', google_api_key=self.gemini_api_key)
        return llm
    
    def openai_llm(self):
        
        llm = ChatOpenAI(model="gpt-3.5-turbo", api_key=self.openai_api_key)
        return llm
