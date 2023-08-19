import psycopg

CONN_STRING = "dbname=blog user=postgres password=postgres host=localhost port=5432"  #Cambiar el parametro dbname por el nombre de tu base de datos

def select(columns, table_name, where=None):
    with psycopg.connect(CONN_STRING) as conn:
        with conn.cursor() as cur:
            column_list = ", ".join(columns)
            #("_id", "in", "(1,2.3)")
            # "_id in (1,2,3)"
            where_string = f'WHERE {where[0]} {where[1]} {where[2]}' if where else ""
            query =f'SELECT {column_list} FROM {table_name} {where_string};'
            cur.execute(query)
            result = cur.fetchall()
    return result

'''
def update(column_value, table_name, where=None):
  with psycopg.connect(CONN_STRING) as conn:
      with conn.cursor() as cur:
          values = [f"{key} = '{value}'" if isinstance(value, str) else f"{key} = {str(value)}"  for key, value in column_value.items()]
          value_list = ', '.join(values) #Can concatenate not str values
          where_string = f'WHERE {where[0]} {where[1]} {where[2]}'
          query =f'UPDATE {table_name} SET {value_list} {where_string};'
          print(query)
          cur.execute(query)
  return f'Parametro Actualizado -> {select("*", table_name, where)}'
'''

def update(columns, table, values:tuple, where=None):
    with psycopg.connect(CONN_STRING) as conn:
        with conn.cursor() as cur:
            values = [f"'{v}'" if isinstance(v,str) else f"{v}" for v in values]
            where_string = f'WHERE {where[0]} {where[1]} {where[2]}'
            values_list = [f'{k}={v}' for k, v in zip(columns, values)]
            values_list_formatted = ", ".join(values_list)
            print(values_list_formatted)
            query =f'UPDATE {table} SET {values_list_formatted} {where_string};'
            print(query)
            cur.execute(query)
            result = f"Parametro Creardo -> {values}"
    return result


def insert(columns, table, values:tuple):
    with psycopg.connect(CONN_STRING) as conn:
        with conn.cursor() as cur:
            columns = ", ".join(columns)
            data=", ".join([f"'{v}'" if isinstance(v,str) else f"{v}" for v in values])
            query =(f"INSERT INTO {table} ({columns}) VALUES ({data})")
            cur.execute(query)
            result = f"Parametro Creardo -> {values}"
    return result


def delete(table_name, where):
  with psycopg.connect(CONN_STRING) as conn:
      with conn.cursor() as cur:
          where_string = f'WHERE {where[0]} {where[1]} {where[2]}'
          print(table_name)
          print(where_string)
          #("_id", "in", "(1,2.3)")
          # "_id in (1,2,3)"
          query =f'DELETE FROM {table_name} {where_string};'
          print(query)
          cur.execute(query)
          result = f"Parametro de la tabla {table_name} Eliminado | ID -> {where[2]}"
  return result