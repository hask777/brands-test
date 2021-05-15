from fastapi import FastAPI
from src.brands import *

app = FastAPI()

@app.get("/")
def hello_world():
    return parse_brands()