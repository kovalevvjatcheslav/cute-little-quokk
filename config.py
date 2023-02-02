from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    WEB_SERVICE_PORT: int = Field("8080", env="WEB_SERVICE_PORT")

    POSTGRES_HOST: str = Field("localhost", env="POSTGRES_HOST")
    POSTGRES_PORT: int = Field(5432, env="POSTGRES_PORT")
    POSTGRES_DB: str = Field("quokk_db", env="POSTGRES_DB")
    POSTGRES_USER: str = Field("user", env="POSTGRES_USER")
    POSTGRES_PASSWORD: str = Field("very_strong_password", env="POSTGRES_PASSWORD")

    SECRET: str = Field("top_secret", env="SECRET")


settings = Settings()
