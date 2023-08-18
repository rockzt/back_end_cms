import psycopg

CONNECTION = "dbname=dvdrental user=postgres  host=localhost"  # cambiar el connet"


def insert(columns, table, values: list):
    """

    :param columns: param table:
    :param values: list:
    :param table: 
    :param values: list: 

    """
    with psycopg.connect(CONNECTION) as conn:
        with conn.cursor() as cur:
            columns = ", ".join(columns)
            data = ", ".join(
                [f"'{v}'" if isinstance(v, str) else f"{v}" for v in values]
            )
            query = f"INSERT INTO {table} ({columns}) VALUES ({data})"
            cur.execute(query)
    return "Dato insertado"
