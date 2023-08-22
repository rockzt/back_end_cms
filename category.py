import db
#name_cate, descrip_cate


# Función para crear una nueva categoría
def create_category(columns,values):
  table="categoría"
  return db.insert(columns, table, values)

# Función para modificar los datos de una categoría
def modify_categoria(id,columns, values ):
    where = "categoria_id", "=", int(id)
    return db.update(columns, "categoría", values ,(where))

# Función para obtener una lista de categorías
def get_all_categorias():
    columns = ["nom_cat", "descrip_cate"]
    return db.select(columns, "categoría")

