import sqlite3

from utils import write_to_json, write_to_excel

d2_data_connection = sqlite3.connect('d2_data.db')
world_content_connection = sqlite3.connect('world_content.db')


def drop_tables(conn: sqlite3.Connection):
    cursor = conn.cursor()
    cursor.execute('''
        DROP TABLE IF EXISTS ItemType;
    ''')


def create_item_type_display_name_table(conn: sqlite3.Connection):
    cursor = conn.cursor()
    cursor.executescript('''
        CREATE TABLE IF NOT EXISTS ItemType (
            Id INTEGER PRIMARY KEY,
            DisplayName TEXT NOT NULL
        );
        CREATE UNIQUE INDEX IF NOT EXISTS ItemType_DisplayName_Index ON ItemType (DisplayName);
    ''')


def select_item_type_display_names(conn: sqlite3.Connection) -> list:
    cursor = conn.cursor()
    cursor.execute('''
        select
            distinct
            json ->> 'itemTypeDisplayName' as itemTypeDisplayName
        from DestinyInventoryItemDefinition where itemTypeDisplayName != '';
    ''')
    return cursor.fetchall()


def insert_item_type_display_name(conn: sqlite3.Connection, display_names: list[tuple[str]]):
    cursor = conn.cursor()
    cursor.executemany('''
        INSERT INTO ItemType (DisplayName) VALUES (?);
    ''', display_names)


def create_dataframe(conn: sqlite3.Connection):
    df = {
        'id': [],
        'displayname': []
    }
    cursor = conn.cursor()
    cursor.execute('''
        select
            distinct id, displayname
        from ItemType;
    ''')
    for item in cursor.fetchall():
        df['id'].append(item[0])
        df['displayname'].append(item[1])
    write_to_json(df, 'ItemTypeDisplayNames.json')
    write_to_excel(df,  'ItemTypeDisplayNames.xlsx')


def commit(conn: sqlite3.Connection):
    conn.commit()


def item_type_display_name():
    drop_tables(d2_data_connection)
    create_item_type_display_name_table(d2_data_connection)
    item_type_display_names = select_item_type_display_names(world_content_connection)
    insert_item_type_display_name(d2_data_connection, item_type_display_names)
    create_dataframe(d2_data_connection)
    commit(d2_data_connection)


if __name__ == '__main__':
    pass

