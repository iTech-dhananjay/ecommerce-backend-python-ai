from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import users, products, orders, payments, ai
from app.core.config import settings
from app.swagger import custom_openapi

app = FastAPI(title=settings.PROJECT_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(products.router, prefix="/products", tags=["Products"])
app.include_router(orders.router, prefix="/orders", tags=["Orders"])
app.include_router(payments.router, prefix="/payments", tags=["Payments"])
app.include_router(ai.router, prefix="/ai", tags=["AI"])

# Attach custom Swagger UI with JWT Bearer
app.openapi = lambda: custom_openapi(app)

@app.get("/")
def read_root():
    return {"message": "E-commerce Backend with AI Ready"}