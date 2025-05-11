from fastapi import APIRouter, Depends
from app.core.security import require_role

router = APIRouter()

@router.post("/", dependencies=[Depends(require_role(["user", "admin", "superadmin"]))])
def create_order():
    return {"message": "Order placed"}

@router.get("/admin", dependencies=[Depends(require_role(["admin", "superadmin"]))])
def list_all_orders():
    return ["Order 1", "Order 2"]
