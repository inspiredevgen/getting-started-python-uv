from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str = None
    price: float
    in_stock: bool = True

app = FastAPI()
@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/is_odd")
async def is_odd(number: int):
    if number % 2 != 0:
        return {"result": f"{number} is odd"}
    return {"result": f"{number} is not odd"}

@app.get("/is_odd/{number}")
async def is_oddNumber(number: int):
    if number % 2 != 0:
        return {"result": f"{number} is odd"}
    return {"result": f"{number} is not odd"}


@app.post("/items/")
async def create_item(item: Item):
    return {"message": f"Item {item} was created successfully"}