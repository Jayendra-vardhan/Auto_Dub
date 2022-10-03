from fastapi import FastAPI
from typing import Union
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi import Form
from pytube import YouTube
import os
import sys
from pytube_test import download_video


app = FastAPI()

templates = Jinja2Templates(directory="templates")

#by this function we are going to the root 
@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("landing_page.html", {"request": request})

#by this function we are requesting the server
@app.get("/form")
def form_post(request: Request): #function for get request
    result = "Enter a youtube link"
    return templates.TemplateResponse('landing_page.html', context={'request': request, 'result': result})


@app.post("/form")
def form_post(request: Request, linky: str = Form(...)):
    download_video(linky)
    result = linky + " Link is being downloaded"
    return templates.TemplateResponse('landing_page.html', context={'request': request, 'result': result})

@app.get("/linky")
def read_link(link: str = Form()):
    print(link)
    return {"link": link}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q":q}
