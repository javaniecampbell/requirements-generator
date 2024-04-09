# Create a Web API using FastAPI with route to products
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Product(BaseModel):
    name: str
    description: str
    price: float
    tax: float


@app.post("/products/")
async def create_product(product: Product):
    return product


@app.get("/products/")
async def get_products():
    return {
        "products": [
            {
                "name": "Product2",
                "description": "Description1",
                "price": 9.99,
                "tax": 1.99,
            }
        ]
    }
