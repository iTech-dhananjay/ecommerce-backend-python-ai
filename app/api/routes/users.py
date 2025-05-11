from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserOut, UserLogin, UserUpdate
from app.crud.user import create_user, get_user_by_email, get_user_by_id, verify_password, update_user
from app.db.session import SessionLocal
from app.core.constants import Messages
from app.core.security import create_access_token

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    if get_user_by_email(db, user.email):
        raise HTTPException(status_code=400, detail=Messages.EMAIL_EXISTS)
    return create_user(db, user)

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, user.email)
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=Messages.LOGIN_FAILED)
    token = create_access_token({"sub": db_user.email, "role": db_user.user_role})
    return {"access_token": token, "token_type": "bearer"}

@router.get("/{user_id}", response_model=UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail=Messages.USER_NOT_FOUND)
    return user

@router.put("/{user_id}", response_model=UserOut)
def update_user_info(user_id: int, updates: UserUpdate, db: Session = Depends(get_db)):
    db_user = get_user_by_id(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail=Messages.USER_NOT_FOUND)
    return update_user(db, db_user, updates)

@router.get("/me", response_model=UserOut)
def get_my_profile(current_user: UserOut = Depends(get_user)):
    return current_user
