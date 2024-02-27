from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class Item(BaseModel):
    x: float
    y: float


app = FastAPI()

@app.post("/add")
async def create_item(item: Item):
    result = item.x + item.y
    return {"result" : result}

@app.post("/sub/")
async def create_item(item: Item):
    result = item.x - item.y
    return {"result" : result}

@app.post("/multi/")
async def create_item(item: Item):
    result = item.x * item.y
    return {"result" : result}

@app.post("/divide/")
async def create_item(item: Item):
    if item.y== 0: 
        raise HTTPException(status_code=422, detail="you can not divide over zero")  
    result = item.x / item.y
    return {"result" : result}

