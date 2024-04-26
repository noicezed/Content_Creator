from fastapi import FastAPI, HTTPException, UploadFile, File
from pydantic import BaseModel, Field
from main import MarketContent
import asyncio
from PIL import Image
import requests
import io
import os
from os import getcwd
import uvicorn
import json

PATH_FILES = getcwd() + "/src" + "/"

app = FastAPI()

class Query(BaseModel):
    image_url:str


@app.get("/")
async def heartbeat():
    return {"Klister":"Welcome To Klister Market Agent"}


@app.post('/cotent_creator_using_image/', )
async def marketing(file: UploadFile = File()):

    try:
        with open(file.filename, "wb") as myfile:
            content = await file.read()
            myfile.write(content)
            myfile.close()
        # return {'message':uploaded_file.filename}
        # image_content = await file.read()
        market_crew = MarketContent(image_url=file.filename)
        response = market_crew.run()
        os.remove(file.filename)
        return {"detail":f"""{response}"""}
        # return {'message':pil_image}
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)

@app.post('/cotent_creator_using_url/' )
async def marketing(query: Query):

    try:

        img_data = requests.get(query.image_url).content
        with open('image.jpg', 'wb') as handler:
            handler.write(img_data)
        # return {'message':uploaded_file.filename}
        # image_content = await file.read()
        market_crew = MarketContent(image_url = 'image.jpg')
        response = market_crew.run()
        os.remove('image.jpg')
        return {"detail":f"""{(response)}"""}
        # return {'message':image}
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)
