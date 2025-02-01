from pydantic import BaseModel, Field
from pydantic_settings import (
    BaseSettings,
    SettingsConfigDict,
)


class DatabaseConfig(BaseModel):
    """Backend database configuration parameters.

    Attributes:
        dsn:
            DSN for target database.
    """

    user: str
    password: str
    db: str
    port: int
    url: str


class CORSConfig(BaseSettings):
    allow_origins: list[str] = ["http://localhost:3001"]  # Frontend URL
    allow_methods: list[str] = ["*"]
    allow_headers: list[str] = ["*"]


class Config(BaseSettings):
    """API configuration parameters.

    Automatically read modifications to the configuration parameters
    from environment variables and ``.env`` file.

    Attributes:
        database:
            Database configuration settings.
            Instance of :class:`app.backend.config.DatabaseConfig`.
        token_key:
            Random secret key used to sign JWT tokens.
        cors:
            CORS configuration settings.
            Instance of :class:`app.backend.config.CORSConfig`.
    """

    database: DatabaseConfig = Field()
    token_key: str
    cors: CORSConfig = CORSConfig()

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter="__",
        case_sensitive=False,
    )


config = Config()  # type: ignore[call-arg]
