from contexts import ConnectionPool, create_table, get_all_rows, insert_all_rows

context = ConnectionPool()

def create_sockets_table():
    create_table("sockets", context)


def get_all_sockets_rows() -> list[tuple[int, str]]:
    return get_all_rows("sockets", context)


def insert_all_sockets_rows(rows: list[tuple[int, str]]) -> None:
    insert_query = """
    INSERT INTO sockets (hash, name, description, displayname, tiertype, icon) VALUES (%s, %s, %s,%s, %s, %s);
    """
    return insert_all_rows(rows, insert_query, context)