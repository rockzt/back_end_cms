import psycopg2
from psycopg2 import sql

# Conexión a la base de datos PostgreSQL
conn = psycopg2.connect(
    database="back_end_cms",
    user="postgres",
    password="mamita",
    host="localhost",  # Cambia esto a la ubicación de tu base de datos
    port="5432"  # Cambia esto al puerto de tu base de datos
)

# Crear un cursor para interactuar con la base de datos
cursor = conn.cursor()

# Función para crear una nueva categoría
def create_category(name, description):
    insert_query = sql.SQL("INSERT INTO category (name_cate, descrip_cate) VALUES ({}, {}) RETURNING category_id").format(
        sql.Literal(name),
        sql.Literal(description)
    )
    cursor.execute(insert_query)
    category_id = cursor.fetchone()[0]
    conn.commit()
    return category_id

# Función para modificar los datos de una categoría
def update_category(category_id, name, description):
    update_query = sql.SQL("UPDATE category SET name_cate = {}, descrip_cate = {} WHERE category_id = {}").format(
        sql.Literal(name),
        sql.Literal(description),
        sql.Literal(category_id)
    )
    cursor.execute(update_query)
    conn.commit()

# Función para obtener una lista de categorías
def get_all_categories():
    select_query = sql.SQL("SELECT * FROM category")
    cursor.execute(select_query)
    return cursor.fetchall()

# Cerrar la conexión cuando hayas terminado
def close_connection():
    cursor.close()
    conn.close()
