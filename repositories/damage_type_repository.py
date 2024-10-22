from contexts import ConnectionPool, create_table, get_all_rows, insert_all_rows

context = ConnectionPool()

def create_damage_type_table():
    create_table("damage_type", context)


def get_all_damage_type_rows() -> list[tuple[int, str]]:
    return get_all_rows("damage_type", context)


def insert_all_damage_type_rows(rows: list[tuple[int, str]]) -> None:
    insert_query = """
    INSERT INTO damage_type (hash, name, description, icon) VALUES (%s, %s, %s, %s);
    """
    return insert_all_rows(rows, insert_query, context)