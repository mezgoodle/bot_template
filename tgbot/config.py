from typing import List

from pydantic import BaseSettings, SecretStr


class Settings(BaseSettings):
    bot_token: SecretStr
    admins: List[str] = ["353057906"]

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


config = Settings()
