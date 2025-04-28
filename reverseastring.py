from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class TextInput(BaseModel):
    text: str
@app.post("/reverse")
def reverse_text(input_text:TextInput):
    reversed_text=input_text.text[::-1]
    return {"reversed_text": reversed_text}

