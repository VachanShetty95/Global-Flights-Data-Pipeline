"""
Configuration management for the ETL pipeline.
Uses pydantic-settings for robust environment variable validation.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class PostgresSettings(BaseSettings):
    """PostgreSQL connection settings."""
    host: str = Field(alias="POSTGRES_HOST")
    port: int = Field(alias="POSTGRES_PORT", default=5432)
    db: str = Field(alias="POSTGRES_DB")
    user: str = Field(alias="POSTGRES_USER")
    password: str = Field(alias="POSTGRES_PASSWORD")

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    @property
    def database_url(self) -> str:
        """Construct the SQLAlchemy database URL."""
        return f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.db}"


class AppSettings(BaseSettings):
    """Application-wide settings including feature flags or paths."""
    datasets_dir: str = Field(default="datasets")

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")


def get_postgres_settings() -> PostgresSettings:
    """Retrieve PostgreSQL settings."""
    return PostgresSettings()


def get_app_settings() -> AppSettings:
    """Retrieve application settings."""
    return AppSettings()
