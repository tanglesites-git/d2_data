from contexts import ConnectionPool, create_table, insert_all_rows, get_all_rows_alt

context = ConnectionPool()

def create_weaponstats_table():
    create_table("weaponstats", context)


def get_all_weaponstats_rows() -> list[tuple[int, str]]:
    return get_all_rows_alt('weaponstats', context)


def insert_all_weaponstats_rows(rows: list[tuple[int, str]]) -> None:
    insert_query = """
    INSERT INTO weaponstats (weapon_id, stat_id, value) VALUES (%s, %s, %s);
    """
    return insert_all_rows(rows, insert_query, context)