import db


'''ARTICLE SECTION'''
def get_all_articles():
    columns = ["titulo", "conten", "autor_id", "categoria_id", "pub_date", "last_update", "active"]
    return db.select(columns, "articulo")


def get_article(id):
    columns = ["titulo", "conten", "autor_id", "categoria_id", "pub_date", "last_update", "active"]
    where = "art_id", "=", (id)
    return db.select(columns, "articulo", (where))


def get_article_by_category(id):
  columns = ["titulo", "conten", "autor_id", "categoria_id", "pub_date", "last_update", "active"]
  where = "categoria_id", "=", (id)
  return db.select(columns, "articulo", (where))

def get_activated_articles():
  columns = ["titulo", "conten", "autor_id", "categoria_id", "pub_date", "last_update", "active"]
  where = "active", "=", (1)
  return db.select(columns, "articulo", (where))


def get_article_by_author(id):
  columns = ["titulo", "conten", "autor_id", "categoria_id", "pub_date", "last_update", "active"]
  where = "autor_id", "=", (id)
  return db.select(columns, "articulo", (where))


def deactivate_article(id):
  columns = ["active"]
  values = ("0")
  where = "art_id", "=", int(id)
  return db.update(columns, "articulo", values ,(where))


def modify_article(id,columns, values ):
    where = "art_id", "=", int(id)
    return db.update(columns, "articulo", values ,(where))


def create_artticle(columns,values):
  table="articulo"
  return db.insert(columns, table, values)



dict_val = {
  "titulo":"Los drones",
  "conten":"Nuestro compañeros autónomos!!!.",
  "autor_id":1,
  "categoria_id":3,
  "pub_date":"20230423 11:42:35.173",
  "last_update":"20230423 11:42:35.173",
  "active":1
}

values = ("Los drones 2.3", "Nuestro compañeros autónomos o enemigos?????!!!!!!.")
columns = ['titulo', 'conten']

#print(get_all_articles())
#print(get_article(2))
#print(deactivate_article(2))
#print(get_article_by_category(3))
#print(get_activated_articles())
#print(get_article_by_author(1))
#print(modify_article(2, columns, values))
#print(create_artticle(values))

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