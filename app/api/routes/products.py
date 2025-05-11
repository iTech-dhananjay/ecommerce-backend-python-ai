from fastapi import APIRouter, Depends, HTTPException
from app.core.security import require_role

router = APIRouter()

@router.get("/", dependencies=[Depends(require_role(["admin", "superadmin", "user"]))])
def get_all_products():
    return ["Product 1", "Product 2"]

@router.post("/", dependencies=[Depends(require_role(["admin", "superadmin"]))])
def create_product():
    return {"message": "Product created"}

@router.delete("/{product_id}", dependencies=[Depends(require_role(["superadmin"]))])
def delete_product(product_id: int):
    return {"message": f"Product {product_id} deleted"}