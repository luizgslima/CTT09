from fastapi import FastAPI

app = FastAPI()

@app.get("/somar/{a}/{b}")
def somar(a: int, b: int):
    return {"resultado": a - b}