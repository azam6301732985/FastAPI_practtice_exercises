from fastapi import FastAPI,status
from pydantic import BaseModel

app= FastAPI()

class Data(BaseModel):
    name: str
@app.post("/submit", status_code=status.HTTP_201_CREATED)

def submit_data(data: Data):
    return {"message":f"Data received for {data.name}"}

            
