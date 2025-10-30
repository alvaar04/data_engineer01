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
