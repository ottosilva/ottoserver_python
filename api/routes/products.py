from fastapi import APIRouter, HTTPException
from typing import List
from api.database.database import collection
from api.models.products import Product
from pydantic_mongo import PydanticObjectId
from ..__common_deps import QueryParamsDependency, QueryParams

router = APIRouter()

@router.post("/products", response_model=Product)
async def create_product(product: Product):
    product_dict = product.model_dump()
    collection.insert_one(product_dict)
    return product

@router.post("/manyproducts", response_model=List[Product])
async def create_products(products: List[Product]):
    product_dicts = [product.model_dump() for product in products]
    result = collection.insert_many(product_dicts)

    if result.inserted_ids:
        return products
    else:
        raise HTTPException(status_code=500, detail="Error inserting books")

@router.get("/products")
async def get_products():
    products = []
    for product in collection.find():
        products.append(Product(**product))
    return products

@router.get("/productsQuery")
async def get_products(query_params: QueryParams = QueryParamsDependency):
    cursor = query_params.query_collection(collection)
    products = list(cursor)
    return products

@router.get("/products/{product_id}", response_model=Product)
async def get_product(product_id: str):
    product = collection.find_one({"_id": PydanticObjectId(product_id)})
    if product:
        return Product(**product)
    else:
        raise HTTPException(status_code=404, detail="product not found")
