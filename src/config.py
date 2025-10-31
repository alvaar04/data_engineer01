import os

from dotenv import load_dotenv

# Cargamos las variables de entorno
load_dotenv()


def get_api_config():
    config = {
        "API_URL": os.getenv("API_URL"),
        "API_CURRENCY": os.getenv("API_CURRENCY"),
        "API_COIN_IDS": os.getenv("API_COIN_IDS"),
    }

    return config


def get_data_path() -> str:
    return "./data/raw_data.json"


def get_db_config():
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_name = os.getenv("DB_NAME")
    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT")
    return {
        "db_user": db_user,
        "db_password": db_password,
        "db_name": db_name,
        "db_host": db_host,
        "db_port": db_port,
    }
