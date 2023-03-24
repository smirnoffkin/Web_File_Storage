from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    postgres_dealect_driver: str
    postgres_user: str
    postgres_password: str
    postgres_host: str
    postgres_port: str
    postgres_db: str

    @property
    def database_url(self):
        return PostgresDsn.build(
            scheme=self.postgres_dealect_driver,
            user=self.postgres_user,
            password=self.postgres_password,
            host=self.postgres_host,
            port=self.postgres_port,
            path=f"/{self.postgres_db}"
        )

    @property
    def async_database_url(self):
        return PostgresDsn.build(
            scheme=f"{self.postgres_dealect_driver}+asyncpg",
            user=self.postgres_user,
            password=self.postgres_password,
            host=self.postgres_host,
            port=self.postgres_port,
            path=f"/{self.postgres_db}"
        )

    class Config:
        env_file = ".env"


settings = Settings()
