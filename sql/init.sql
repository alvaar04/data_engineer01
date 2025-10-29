CREATE TABLE IF NOT EXISTS precios_cripto (
    id SERIAL PRIMARY KEY, -- Serial hace que cada fila tenga un valor +1 al anterior
    id_moneda VARCHAR(50) NOT NULL,
    nombre VARCHAR(100),
    precio_actual FLOAT,
    max_24h FLOAT,
    min_24h FLOAT,
    cambio_porcentaje_24h FLOAT,
    api_last_updated TIMESTAMP,
    fecha_insercion TIMESTAMP DEFAULT NOW() -- Por defecto se rellena con la fecha actual
);