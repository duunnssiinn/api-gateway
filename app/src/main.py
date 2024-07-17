from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def handler():
    """ This is the api docstring"""
    return {"status": "Healthy"}