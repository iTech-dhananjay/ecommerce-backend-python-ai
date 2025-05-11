from sqlalchemy.orm import Session
from app.db.session import SessionLocal
from app.db.models.user import User
from app.db.models.product import Product
from app.core.constants import Roles
from passlib.context import CryptContext
from faker import Faker

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
fake = Faker()

NUM_FAKE_USERS = 10
NUM_FAKE_PRODUCTS = 20

def seed_admins(db: Session):
    users = [
        User(email="admin@example.com", hashed_password=pwd_context.hash("admin123"), full_name="Admin User", user_role=Roles.ADMIN),
        User(email="user@example.com", hashed_password=pwd_context.hash("user123"), full_name="Normal User", user_role=Roles.USER),
        User(email="superadmin@example.com", hashed_password=pwd_context.hash("super123"), full_name="Super Admin", user_role=Roles.SUPERADMIN)
    ]
    db.add_all(users)
    db.commit()

def seed_fake_users(db: Session):
    users = []
    for _ in range(NUM_FAKE_USERS):
        users.append(User(
            email=fake.unique.email(),
            full_name=fake.name(),
            hashed_password=pwd_context.hash("password123"),
            user_role=Roles.USER,
            phone_number=fake.phone_number()
        ))
    db.add_all(users)
    db.commit()

def seed_fake_products(db: Session):
    products = []
    for _ in range(NUM_FAKE_PRODUCTS):
        products.append(Product(
            name=fake.unique.word().capitalize(),
            description=fake.sentence(),
            price=round(fake.pyfloat(left_digits=3, right_digits=2, positive=True), 2)
        ))
    db.add_all(products)
    db.commit()

def run():
    db = SessionLocal()
    try:
        seed_admins(db)
        seed_fake_users(db)
        seed_fake_products(db)
        print("✅ Admin + fake users/products seeded successfully")
    finally:
        db.close()

if __name__ == "__main__":
    run()