from configuration import PathsIO
from contexts import ConnectionPool, create_table, get_all_rows, insert_all_rows

context = ConnectionPool()

def create_stats_table():
    create_table("stats", context)


def get_all_stats_rows() -> list[tuple[int, str]]:
    return get_all_rows('stats', context)


def insert_all_stats_rows(rows: list[tuple[int, str]]) -> None:
    insert_query = """
    INSERT INTO stats (hash, name, description) VALUES (%s, %s, %s);
    """
    return insert_all_rows(rows, insert_query, context)





