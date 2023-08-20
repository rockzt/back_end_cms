import db
" modulo autor "
def get_all_autor():
    table="autor"
    columns = ["autor_id", "first_name", "last_name", "email", "passw"]
    return db.select(columns,table)

def get_autors(ids):
    table="autor"
    columns = ["autor_id", "first_name", "last_name", "email", "passw"]
    where = ("autor_id", "in", str(tuple(ids)))
    return db.select(columns, table, where)

def get_autor(autor_id):
    table="autor"
    columns = ["autor_id", "first_name", "last_name", "email", "passw"]
    where = ("autor_id", "=", autor_id)
    return db.select(columns, table, where)


def insert_autor(values):
    table="autor"
    columns = ["first_name", "last_name", "email","passw"]
    return db.insert(columns, table,values)

def update_autor(columns,values,autor_id):
    table="autor"
    #columns = ["first_name", "last_name", "email","passw"]
    where = ("autor_id", "=", autor_id)
    return db.update(columns, table, values,where)

  
def get_arts(autor_id):
    """hice un select join para los articulos de un autor con nombre"""
    table="articulo"
    table_2="autor"
    columns=["art_id","title","published_date","articulo.autor_id","first_name","last_name"]
    where = ("autor_id", "=", autor_id)
    return db.select_join(columns,table,table_2,where)