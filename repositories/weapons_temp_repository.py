from contexts import ConnectionPool, create_table, get_all_rows, insert_all_rows

context = ConnectionPool()

def create_weapons_temp_table():
    create_table("weapons_temp", context)


def get_all_weapons_temp_rows() -> list[tuple[int, str]]:
    return get_all_rows('weapons_temp', context)


def insert_all_weapons_temp_rows(rows: list[tuple[int, str]]) -> None:
    insert_query = """
    INSERT INTO weapons_temp (hash, name, displayname, tiertype, ammotype, equipmentslot, damagetype_id, collectible_id, lore_id, flavortext, icon, watermark, screenshot) VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s,%s);
    """
    return insert_all_rows(rows, insert_query, context)