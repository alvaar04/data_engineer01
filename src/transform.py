import pandas as pd

import config

DATA_PATH = config.get_data_path()


def fetch_data(path=DATA_PATH) -> pd.DataFrame:
    """
    Funcion que lee los datos en formato json
    """
    data_df = pd.read_json(path)

    return data_df


def map_columns(df: pd.DataFrame):
    mapping_schema = {
        "id": "id_moneda",
        "name": "nombre",
        "current_price": "precio_actual",
        "high_24h": "max_24h",
        "low_24h": "min_24h",
        "price_change_percentage_24h": "cambio_porcentaje_24h",
        "last_updated": "api_last_updated",
    }

    df.rename(columns=mapping_schema, inplace=True)

    print(df)

    return df


def clean_data(raw_data) -> pd.DataFrame:
    clean_df = raw_data[
        [
            "id",
            "name",
            "current_price",
            "high_24h",
            "low_24h",
            "price_change_percentage_24h",
            "last_updated",
        ]
    ]
    clean_df.loc[:, "last_updated"] = pd.to_datetime(clean_df["last_updated"])
    clean_df = map_columns(clean_df)
    return clean_df


def transform_data(path=DATA_PATH):
    raw_data = fetch_data()
    clean_df = clean_data(raw_data)
    return clean_df
