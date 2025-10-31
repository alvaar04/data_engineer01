# Simple Crypto ETL Pipeline

Este proyecto es un pipeline ETL (Extract, Transform, Load) simple y contenedorizado. Su objetivo es extraer datos del mercado de criptomonedas desde la API pública de **CoinGecko**, realizar transformaciones básicas con **Pandas** y cargar los datos en una base de datos **PostgreSQL** para construir un **dataset histórico** de precios.

## 🛠️ Tech Stack

* **Contenerización:** Docker & Docker Compose
* **Lenguaje:** Python 3.10
* **Base de Datos:** PostgreSQL
* **Librerías de Python:**
    * `requests`: Para la extracción de datos de la API.
    * `pandas`: Para la transformación de datos.
    * `sqlalchemy`: Para la carga en la base de datos (junto con `psycopg2`).
    * `python-dotenv`: Para la gestión de secretos y configuración.

---

## 🚀 Cómo Empezar

Para ejecutar este pipeline en tu máquina local, solo necesitas tener **Git** y **Docker** instalados.

### 1. Clonar el Repositorio

```bash
git clone https://github.com/alvaar04/data_engineer01.git
cd data_engineering01
````

### 2\. Configuración del Entorno

Este proyecto necesita un fichero `.env` para gestionar las credenciales de la base de datos y las URLs de la API.

1.  Crea un fichero llamado `.env` en la raíz del proyecto.

2.  Copia y pega el contenido de `.env.example`y rellena los valores:

    ```text
    # Fichero .env
    DB_USER=postgres
    DB_PASSWORD=tu_password_secreto
    DB_HOST=db        # Nombre del servicio en docker-compose
    DB_PORT=5432
    DB_NAME=crypto_db

    # API de CoinGecko
    API_URL=[https://api.coingecko.com/api/v3/coins/markets](https://api.coingecko.com/api/v3/coins/markets)
    API_CURRENCY=eur
    API_COIN_IDS=bitcoin,ethereum,cardano
    ```

### 3\. Levantar los Contenedores

Este comando construirá la imagen de tu aplicación de Python, levantará el contenedor de la base de datos PostgreSQL y ejecutará el pipeline `run_pipeline.py` una vez.

```bash
docker-compose up --build
```

Si solo quieres levantar la base de datos para conectarte a ella:

```bash
docker-compose up -d db
```

-----

## 🌊 Flujo del Pipeline (ETL)

### 1\. Extract

  * **Origen:** API de CoinGecko (endpoint `.../coins/markets`).
  * **Acción:** Se realiza una petición GET para obtener un JSON con los datos de las monedas especificadas en las variables de entorno (`API_COIN_IDS`).

### 2\. Transform

  * **Herramienta:** `pandas`
  * **Acción:** Los datos crudos del JSON se cargan en un DataFrame.
  * **Limpieza:**
      * Se seleccionan solo las columnas de interés.
      * Se **renombran** las columnas para que coincidan con nuestro esquema de BBDD (ej. `id` -\> `id_moneda`, `high_24h` -\> `max_24h`).
      * Se asegura el tipo de dato correcto (ej. `last_updated` se convierte a `datetime`).

### 3\. Load

  * **Destino:** Base de datos PostgreSQL.
  * **Acción:** El DataFrame limpio se **añade** (append) a la tabla `precios_cripto`. Esto permite que, con cada ejecución, el historial de precios crezca.

#### Esquema de la Tabla (`precios_cripto`)

| Columna | Tipo de Dato | Descripción |
| :--- | :--- | :--- |
| `id` | `SERIAL PRIMARY KEY` | ID único del *registro* (auto-incremental). |
| `id_moneda` | `VARCHAR(50)` | ID de la moneda según la API (ej. "bitcoin"). |
| `nombre` | `VARCHAR(100)` | Nombre humano de la moneda (ej. "Bitcoin"). |
| `precio_actual` | `FLOAT` | Precio actual en la divisa configurada. |
| `max_24h` | `FLOAT` | Precio máximo en las últimas 24h. |
| `min_24h` | `FLOAT` | Precio mínimo en las últimas 24h. |
| `porcentaje_cambio_24h` | `FLOAT` | % de cambio de precio en las últimas 24h. |
| `api_last_updated` | `TIMESTAMP` | Fecha (UTC) de la última actualización del dato en la API. |
| `fecha_insercion` | `TIMESTAMP` | Fecha (UTC) en que *nuestro pipeline* insertó el dato (`DEFAULT NOW()`). |
