from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    LIBRARY_DB_URL: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()