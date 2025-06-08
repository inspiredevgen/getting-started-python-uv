from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    email: str
    country: str = "Canada"

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True


p1 = Product(id=1, name="Laptop", price=999.99)
p2 = Product(id=2, name="iPhone", price=860.75, in_stock=False)

print(p1)
print(p2.model_dump())