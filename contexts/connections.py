from psycopg2 import pool

from configuration import PathsIO

d2_app_connection_pool = pool.SimpleConnectionPool(1, 100, "dbname=d2_app user=postgres password=postgres port=5432")
world_content_connection_pool: pool.SimpleConnectionPool = pool.SimpleConnectionPool(1, 100,
                                                                                     "dbname=world_content user=postgres password=postgres port=5432")


class StatPools:
    D2_APP = pool.SimpleConnectionPool(1, 100, "dbname=d2_app user=postgres password=postgres port=5432")
    WORLD_CONTENT = pool.SimpleConnectionPool = pool.SimpleConnectionPool(1, 100,
                                                                          "dbname=world_content user=postgres password=postgres port=5432")

class ConnectionPool:

    def __init__(self):
        self._connection = None
        self._pool = None

    @property
    def connection(self):
        return self._connection

    @connection.setter
    def connection(self, value):
        self._connection = value

    @property
    def pool(self):
        return self._pool

    @pool.setter
    def pool(self, value):
        self._pool = value

    def set_connection(self, strategy):
        new_strat = strategy()
        self._pool = new_strat.pool
        self._connection = new_strat.connection

    def put_conn(self):
        self._pool.putconn(self._connection)


class D2AppConnection:

    def __init__(self):
        self.pool = StatPools.D2_APP
        self.connection = self.pool.getconn()

class WorldContentConnection:

    def __init__(self):
        self.pool = StatPools.WORLD_CONTENT
        self.connection = self.pool.getconn()


def create_table(filename: str, context):
    with open(PathsIO.D2APP_SQL_DIRECTORY / f'{filename}.sql', 'r', encoding='utf-8') as file:
        query = file.read()
        context.set_connection(D2AppConnection)
        cur = context.connection.cursor()
        cur.execute(query)
        context.connection.commit()
        cur.close()
        context.put_conn()

def get_all_rows(filename, context) -> list[tuple[int, str]]:
    with open(PathsIO.WORLD_CONTENT_SQL_DIRECTORY / f'{filename}.sql', 'r', encoding='utf-8') as file:
        query = file.read()
        context.set_connection(WorldContentConnection)
        cursor = context.connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        context.put_conn()
        return rows


def insert_all_rows(rows: list[tuple[int, str]], query, context) -> None:
    context.set_connection(D2AppConnection)
    cursor = context.connection.cursor()
    cursor.executemany(query, rows)
    context.connection.commit()
    cursor.close()
    context.put_conn()