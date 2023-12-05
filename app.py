from fastapi import FastAPI
import os

app = FastAPI()


@app.get("/")
def home():
    return {"web":"phuocsiuuu"}

@app.get("/train")
def train():
    os.system("python main.py")