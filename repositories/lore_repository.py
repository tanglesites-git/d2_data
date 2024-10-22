from contexts import ConnectionPool, create_table, get_all_rows, insert_all_rows

context = ConnectionPool()

def create_lore_table():
    create_table("lore", context)


def get_all_lore_rows() -> list[tuple[int, str]]:
    return get_all_rows("lore", context)


def insert_all_lore_rows(rows: list[tuple[int, str]]) -> None:
    insert_query = """
    INSERT INTO lore (hash, description, subtitle) VALUES (%s, %s, %s);
    """
    return insert_all_rows(rows, insert_query, context)