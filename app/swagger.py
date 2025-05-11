from fastapi.openapi.utils import get_openapi
from fastapi import FastAPI, Request
from app.core.config import settings


def custom_openapi(app: FastAPI):
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title=settings.PROJECT_NAME,
        version="1.0.0",
        description="This is the API documentation for the E-commerce backend with AI and RBAC.",
        routes=app.routes,
    )

    # Enable Bearer token globally in Swagger UI
    openapi_schema["components"]["securitySchemes"] = {
        "bearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }

    for path in openapi_schema["paths"].values():
        for method in path.values():
            method["security"] = [{"bearerAuth": []}]

    app.openapi_schema = openapi_schema
    return app.openapi_schema
