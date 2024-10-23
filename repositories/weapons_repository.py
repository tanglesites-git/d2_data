from contexts import ConnectionPool, create_table, insert_all_rows, get_all_rows_alt

context = ConnectionPool()

def create_weapons_table():
    create_table("weapons", context)


def get_all_weapons_rows() -> list[tuple[int, str]]:
    return get_all_rows_alt('weapons', context)


def insert_all_weapons_rows(rows: list[tuple[int, str]]) -> None:
    insert_query = """
    INSERT INTO weapons (hash, name, displayname, tiertype, ammotype, equipmentslot, damagetype_id, collectible_id, lore_id, flavortext, icon, watermark, screenshot) VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s);
    """
    return insert_all_rows(rows, insert_query, context)