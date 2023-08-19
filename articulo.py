import db


'''ARTICLE SECTION'''


def get_all_articles():
    columns = ["titulo", "conten", "autor_id",
               "categoria_id", "pub_date", "last_update", "active"]
    return db.select(columns, "articulo")


def get_article(id):
    columns = ["titulo", "conten", "autor_id",
               "categoria_id", "pub_date", "last_update", "active"]
    where = "art_id", "=", (id)
    return db.select(columns, "articulo", (where))


def get_article_by_category(id):
    columns = ["titulo", "conten", "autor_id",
               "categoria_id", "pub_date", "last_update", "active"]
    where = "categoria_id", "=", (id)
    return db.select(columns, "articulo", (where))


def get_deactivated_articles(active):
    columns = ["titulo", "conten", "autor_id",
               "categoria_id", "pub_date", "last_update", "active"]
    where = "active", "=", (active)
    return db.select(columns, "articulo", (where))


def get_article_by_author(id):
    columns = ["titulo", "conten", "autor_id",
               "categoria_id", "pub_date", "last_update", "active"]
    where = "autor_id", "=", (id)
    return db.select(columns, "articulo", (where))


def deactivate_article(id):
    where = "art_id", "=", int(id)
    return db.update({"active": 0}, "articulo", (where))


def modify_article(id, column_values):
    dict_vals = column_values
    where = "art_id", "=", int(id)
    return db.update(dict_vals, "articulo", (where))


def create_artticle(column_values):
    dict_vals = column_values
    return db.insert(dict_vals, "articulo")


dict_val = {"titulo": "Los drones", "conten": "Nuestro compañeros autónomos!!!.", "autor_id": 1,
            "categoria_id": "3", "pub_date": "20230423 11:42:35.173", "last_update": "20230423 11:42:35.173", "active": 1}

# print(get_all_articles())
# print(get_article(2))
# print(deactivate_article(2))
# print(get_article_by_category(3))
# print(get_deactivated_articles(1))
# print(get_article_by_author(1))
# print(modify_article(2, dict_val))
print(create_artticle(dict_val))

'''
- Crear nuevos artículos
- Modificar artículos existentes
- Desactivar artículos
- Obtener la lista de todos los artículos
- Obtener los datos de un artículo
- Obtener los artículos de una categoría
- Obtener los artículos activos/publicados
- Obtener los artículos de un autor
'''
'''
titulo
conten
autor_id
categoria_id
pub_date
last_update
active'''
