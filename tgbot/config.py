import os
from dataclasses import dataclass


@dataclass
class DbConfig:
    host: str
    password: str
    user: str
    database: str


@dataclass
class TgBot:
    token: str


@dataclass
class Config:
    tg_bot: TgBot
    db: DbConfig


def load_config(path: str = None):

    return Config(
        tg_bot=TgBot(
            token=os.getenv('BOT_TOKEN', '5135575762:AAE76qg7AQNTFNwGKf67PHXpxYhip_7TEXI'),
        ),
        db=DbConfig(
            host=os.getenv('DB_HOST', 'localhost'),
            password=os.getenv('DB_PASSWORD', 'password'),
            user=os.getenv('DB_USER', 'user'),
            database=os.getenv('DB_NAME', 'database'),
        ),
    )
