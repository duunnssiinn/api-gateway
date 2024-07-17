from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def handler():
    """ This base endpoint returns the application health status """
    return {"status": "Healthy"}