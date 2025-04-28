from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/welcome")
def welcome_user(name:Optional[str]= None):
    if name:
        return {"message":f"welcome,{name}!"}
    else:
        return {"message":"welcome, greet!"}
    