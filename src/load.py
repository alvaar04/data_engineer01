import pandas as pd
import sqlalchemy
from dotenv import load_dotenv

import config

load_dotenv()
db_config = config.get_db_config()


def create_engine():
    """
    Funcion que crea el motor a la base de datos
    """

    connection_string = (
        f"postgresql://{db_config['db_user']}:"
        f"{db_config['db_password']}@"
        f"{db_config['db_host']}:"
        f"{db_config['db_port']}/"
        f"{db_config['db_name']}"
    )
    engine = sqlalchemy.create_engine(connection_string)

    return engine


def load_data(clean_data: pd.DataFrame):
    # Creamos el motor, y usando pandas volcamos los datos en la base de datos de una forma eficiente
    engine = create_engine()
    clean_data.to_sql(
        name="precios_crypto",
        con=engine,
        schema="crypto",
        if_exists="append",
        index=False,
    )

    print("Datos cargados de forma existosa en la base de datos: crypto.precios_crypto")
