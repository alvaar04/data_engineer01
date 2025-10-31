from extract import extract_data
from load import load_data
from transform import transform_data

if __name__ == "__main__":
    # Extraemos los datos y los almacenamos
    extract_data()

    # Clean the data
    clean_data = transform_data()

    # Load the data into PostgreSQL DB
    load_data(clean_data)
