import json

from configuration import PathsIO
from models import StatModel

from psycopg2 import pool


def dict_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}


connection_pool = pool.SimpleConnectionPool(1, 100, "dbname=world_content user=postgres password=postgres port=5432")

select_diid_query = """
SELECT json -> 'hash'                                        AS hash,
       json -> 'displayProperties' ->> 'name'                AS name,
       json -> 'itemTypeDisplayName'                         AS displayname,
       json -> 'inventory' ->> 'tierTypeName'                AS tiertypename,
       json -> 'flavorText'                                  AS flavortext,
       json -> 'equippingBlock' ->> 'equipmentSlotTypeHash'  AS slottype,
       json -> 'equippingBlock' ->> 'ammoType'               AS ammotype,
       json -> 'defaultDamageTypeHash'                       AS damagetypehash,
       CASE json -> 'equippingBlock' ->> 'ammoType'
           WHEN '1' THEN 'Primary'
           WHEN '2' THEN 'Special'
           WHEN '3' THEN 'Heavy'
           END                                               AS ammoname,
       json -> 'displayProperties' ->> 'icon'                AS icon,
       SUBSTRING(json -> 'displayProperties' ->> 'icon', 32) AS clienticonurl,
       json ->> 'iconWatermark'                              AS watermark,
       SUBSTRING(json ->> 'iconWatermark', 32)               AS clientwatermarkurl,
       json ->> 'screenshot'                                 AS screenshot,
       SUBSTRING(json ->> 'screenshot', 38)                  AS clientscreenshoturl,
       json -> 'investmentStats'                             AS stats,
       json -> 'sockets'                                     AS sockets

FROM destinyinventoryitemdefinition
WHERE (json ->> 'itemType')::INTEGER = 3;
"""
select_stats_query = """
SELECT
    json -> 'hash' AS hash,
    json -> 'displayProperties' ->> 'name' AS name,
    json -> 'displayProperties' ->> 'description' AS description
FROM destinystatdefinition WHERE (json ->> 'statCategory')::INTEGER = 1 AND json -> 'displayProperties' ->> 'description' != '';
"""
select_collectible_query = """
select
    json -> 'hash' as Hash,
    json -> 'displayProperties' ->> 'name' as Name,
    json ->> 'sourceString' as SourceString
from DestinyCollectibleDefinition where json -> 'displayProperties' ->> 'name' != '' or json -> 'displayProperties' ->> 'name' is not NULL;
"""
select_damage_query = """
SELECT
    json -> 'hash' AS hash,
    json -> 'displayProperties' ->> 'name' AS name,
    json -> 'displayProperties' ->> 'description' AS description ,
    json -> 'displayProperties' ->> 'icon' AS icon
FROM destinydamagetypedefinition WHERE json -> 'displayProperties' ->> 'icon' IS NOT NULL;
"""

connection = connection_pool.getconn()

diid_cursor = connection.cursor()
stats_cursor = connection.cursor()
collectible_cursor = connection.cursor()
damage_cursor = connection.cursor()

diid_cursor.execute(select_diid_query)
stats_cursor.execute(select_stats_query)
collectible_cursor.execute(select_collectible_query)
damage_cursor.execute(select_damage_query)

diid_rows = diid_cursor.fetchall()
print("Fetching rows for DestinyInventoryItemDefinition")
stats_rows = stats_cursor.fetchall()
print("Fetching rows for DestinyStatDefinition")
collectible_rows = collectible_cursor.fetchall()
print("Fetching rows for DestinyCollectibleDefinition")
damage_rows = damage_cursor.fetchall()
print("Fetching rows for DestinyDamageTypeDefinition")

# Do something with all this data:
diid_keys = (
'hash', 'name', 'displayName', 'tierTypeName', 'flavorText', 'slotType', 'ammoType', 'damageTypeHash', 'ammoName',
'icon', 'clientIconUrl', 'watermark', 'clientWatermarkUrl', 'screenshot', 'clientScreenshotUrl', 'stats', 'sockets')
# stats_keys = ('hash', 'name', 'description')
collectible_keys = ('hash', 'name', 'sourceString')
damage_keys = ('hash', 'name', 'description', 'icon')

# stat_dictionary = {}
# stat_data_frame = {}
#
# for item in stats_rows:
#     dictionary = dict(zip(stats_keys, item))
#     stat_model = StatModel.from_dict(dictionary)
#     stat_dictionary[stat_model.id] = dictionary
#
#     for key, value in dictionary.items():
#         if key not in stat_data_frame:
#             stat_data_frame[key] = [value]
#             continue
#         stat_data_frame[key].append(value)
#
# with open(PathsIO.DATAFRAME_DIRECTORY / 'stats.json', 'w', encoding='utf-8') as f:
#     json.dump(stat_data_frame, f, ensure_ascii=False, indent=4)
#     print(f"Creating Dataframe: {PathsIO.DATAFRAME_DIRECTORY / 'stats.json'}")
#
# with open(PathsIO.DICTIONARIES_DIRECTORY / 'stats.json', 'w', encoding='utf-8') as f:
#     json.dump(stat_dictionary, f, ensure_ascii=False, indent=4)
#     print(f"Creating Dictionary: {PathsIO.DICTIONARIES_DIRECTORY / 'stats.json'}")

# for item in collectible_rows:
#     dictionary = dict(zip(collectible_keys, item))
#     print(dictionary)
#     break
#
# for item in damage_rows:
#     dictionary = dict(zip(damage_keys, item))
#     print(dictionary)
#     break
#
# diid_dict = {}
# diid_df = {}
#
# for item in diid_rows:
#     dictionary = dict(zip(diid_keys, item))
#     print(dictionary)
#     break

print("Closing cursors")
diid_cursor.close()
stats_cursor.close()
collectible_cursor.close()
damage_cursor.close()

print("Putting connection back in the pool")
connection_pool.putconn(connection)

print()
print(f'Diid: {len(diid_rows)}')
print(f'Stats: {len(stats_rows)}')
print(f'Collectibles: {len(collectible_rows)}')
print(f'Damage: {len(damage_rows)}')

if __name__ == '__main__':
    pass
    # initialize_manifest_data()
    # create_postgres_tables()
    # migrate_to_postgres()
