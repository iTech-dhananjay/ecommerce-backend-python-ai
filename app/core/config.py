class Settings(BaseSettings):
    PROJECT_NAME: str = "ecommerce-backend-python"
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    OPENAI_API_KEY: str
    STRIPE_SECRET_KEY: str

    class Config:
        env_file = ".env"

settings = Settings()