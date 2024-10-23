from contexts import ConnectionPool, create_table, insert_all_rows, get_all_rows

context = ConnectionPool()

def create_weaponstats_temp_table():
    create_table("weaponstats_temp", context)


def get_all_weaponstats_temp_rows() -> list[tuple[int, str]]:
    return get_all_rows('weaponstats_temp', context)


def insert_all_weaponstats_temp_rows(rows: list[tuple[int, str]]) -> None:
    insert_query = """
    INSERT INTO weaponstats_temp (weapon_id, stat_id, value) VALUES (%s, %s, %s);
    """
    return insert_all_rows(rows, insert_query, context)