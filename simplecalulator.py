from fastapi import FastAPI
from pydantic import BaseModel

app= FastAPI()

class Numbers(BaseModel):
    num1: float
    num2: float

@app.post("/multiply")
def multiply_numbers(numbers:Numbers):
    result = numbers.num1 * numbers.num2
    return {"result": result}

