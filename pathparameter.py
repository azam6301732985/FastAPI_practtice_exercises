from fastapi import FastAPI

app=FastAPI()

@app.get("/greet/{name}")
def greet_name(name:str):
    return {"greeting":f"hello,{name}!"}