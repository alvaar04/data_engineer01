import requests

from src import config


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

    return response


data = fetch_data_from_api().json()

print(data)
