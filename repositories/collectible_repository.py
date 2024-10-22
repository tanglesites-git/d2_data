from contexts import ConnectionPool, create_table, get_all_rows, insert_all_rows

context = ConnectionPool()

def create_collectibles_table():
    create_table("collectibles", context)


def get_all_collectibles_rows() -> list[tuple[int, str]]:
    return get_all_rows("collectibles", context)


def insert_all_collectibles_rows(rows: list[tuple[int, str]]) -> None:
    insert_query = """
    INSERT INTO collectibles (hash, sourcestring) VALUES (%s, %s);
    """
    return insert_all_rows(rows, insert_query, context)