from fastapi import FastAPI

app= FastAPI()

@app.get("/add")
def add_numbers(a: int,b: int):
    return {"sum": a+b}

