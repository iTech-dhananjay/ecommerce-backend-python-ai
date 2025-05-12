from fastapi import APIRouter

router = APIRouter()

# Define your endpoints below
@router.get("/")
def get_payments():
    return {"message": "Payments route working"}
