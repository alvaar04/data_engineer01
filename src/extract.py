import json

import requests

import config

DATA_PATH = config.get_data_path()


def fetch_data_from_api():
    """
    Extrae los datos de la api usando la configuracion establecida.
    """

    config_profile = config.get_api_config()

    API_URL = config_profile["API_URL"]
    API_CURRENCY = config_profile["API_CURRENCY"]
    API_COIN_IDS = config_profile["API_COIN_IDS"]

    # En headers se escribe el metodo de autenticacion
    # headers = {"x-cg-pro-api-key": "<api-key>"} Asi en este caso
    params = {
        "ids": API_COIN_IDS,
        "order": "market_cap_desc",
        "precision": "2",
        "vs_currency": API_CURRENCY,
    }

    response = requests.get(API_URL, params=params)

    return response.json()


def extract_data(path=DATA_PATH):
    """
    Extrae los datos de la api y los almacena en formato json
    """
    raw_data = fetch_data_from_api()
    with open(DATA_PATH, mode="w", encoding="utf-8") as f:

        # Indent 4 mejora la legibilidad, y ensure_ascii=False hace que algunos caracteres no reconocidos si aparezcan.
        json.dump(raw_data, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    ...
