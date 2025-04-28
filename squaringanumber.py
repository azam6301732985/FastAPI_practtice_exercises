from fastapi import FastAPI

app= FastAPI()

@app.get("/square/{number}")
def square_number(number: int):
    result= number * number
    return {"number":number, "square": result}

         