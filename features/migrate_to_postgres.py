from sqlite3 import connect as s_conn, Cursor
from psycopg2 import pool
from configuration import PathsIO
from re import sub, MULTILINE

connection_pool = pool.SimpleConnectionPool(1, 100, "dbname=world_content user=postgres password=postgres port=5432")

def dict_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}


def get_all_rows(cursor: Cursor, sql: str):
    cursor.execute(sql)
    return cursor.fetchall()


def generate_drop_command(table_name: str):
    return f"DROP TABLE IF EXISTS {table_name};\n"


def create_insert(name: str):
    return f'insert into {name} values (%s, %s) on conflict do nothing;'


def create_query(table_name):
    return f'select * from {table_name};\n'


def transform_query(table_sql: str) -> str:
    new_sql = table_sql.replace('TABLE', 'TABLE IF NOT EXISTS')
    new_sql = new_sql.replace('[', '')
    new_sql = new_sql.replace(']', '')
    new_sql = new_sql.replace('INTEGER', 'bigint')
    new_sql = new_sql.replace('BLOB', 'json')
    new_sql = new_sql.replace('\n', ' ')
    new_sql = new_sql.replace('\r', '')
    new_sql = new_sql.replace('\t\t', ' ')
    new_sql = sub(r'\s+', ' ', new_sql, 0, MULTILINE)
    new_sql += ';\n'
    return new_sql


def insert_all_rows(conn, query: str, rows_list: list[str]):
    cursor = conn.cursor()
    rows = cursor.execute(query)
    rows_list.append(rows)


def create_postgres_tables():
    sqlite_connection = s_conn(PathsIO.WORLD_CONTENT_FILENAME)
    sqlite_connection.row_factory = dict_factory
    sqlite_cursor = sqlite_connection.cursor()

    sql = """
    SELECT tbl_name, sql FROM sqlite_master;
    """

    rows = get_all_rows(sqlite_cursor, sql)
    sql_list = []
    drop_table_list = []
    for row in rows:
        table_sql = row['sql']
        table_name = row['tbl_name']
        drop_table_list.append(generate_drop_command(table_name))

        if table_sql is None:
            continue

        transformed_query = transform_query(table_sql)
        sql_list.append(transformed_query)

    create_all_tables_string = ''.join(sql_list)
    drop_all_tables_string = ''.join(drop_table_list)

    complete_query = drop_all_tables_string + '\n' + create_all_tables_string

    print(complete_query)

    postgres_connection = connection_pool.getconn()
    postgres_cursor = postgres_connection.cursor()
    postgres_cursor.execute(complete_query)
    postgres_connection.commit()

    postgres_cursor.close()
    connection_pool.putconn(postgres_connection)


def migrate_to_postgres():
    sqlite_connection = s_conn(PathsIO.WORLD_CONTENT_FILENAME)
    sqlite_connection.row_factory = dict_factory
    sqlite_cursor = sqlite_connection.cursor()

    postgres_connection = connection_pool.getconn()


    sql = """
        SELECT tbl_name FROM sqlite_master;
        """
    select_list = []
    rows_list = []
    sqlite_cursor.execute(sql)
    rows = sqlite_cursor.fetchall()
    for row in rows:
        select = f"""select * from {row['tbl_name']};"""
        sqlite_cursor.execute(select)
        rr = sqlite_cursor.fetchall()
        rows_list.append([row['tbl_name'], rr])

    for row in rows_list:
        name = row[0]
        value = row[1]
        list_of_tuples = [tuple(d.values()) for d in value]

        c = postgres_connection.cursor()
        c.executemany(create_insert(name), list_of_tuples)
        print(name)

        c.close()
    postgres_connection.commit()
    connection_pool.putconn(postgres_connection)


if __name__ == '__main__':
    pass