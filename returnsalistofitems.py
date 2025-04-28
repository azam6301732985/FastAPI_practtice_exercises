from fastapi import FastAPI

app= FastAPI()

@app.get("/items")
def get_items():
    items = ["apple","banana", "orange"]
    return {"items": items}

