from features import process
from models import StatModel, DamageTypeModel, CollectiblesModel, LoreModel, SocketsModel, WeaponsModel, \
    WeaponStatsModel
from repositories import get_all_stats_rows, create_stats_table, insert_all_stats_rows
from repositories import get_all_damage_type_rows, create_damage_type_table, insert_all_damage_type_rows
from repositories import get_all_collectibles_rows, create_collectibles_table, insert_all_collectibles_rows
from repositories import get_all_lore_rows, create_lore_table, insert_all_lore_rows
from repositories import get_all_sockets_rows, create_sockets_table, insert_all_sockets_rows
from repositories import get_all_weapons_temp_rows, create_weapons_temp_table, insert_all_weapons_temp_rows
from repositories import get_all_weapons_rows, create_weapons_table, insert_all_weapons_rows
from repositories import get_all_weaponstats_temp_rows, insert_all_weaponstats_temp_rows, create_weaponstats_temp_table

stat_rows = get_all_stats_rows()
damage_type_rows = get_all_damage_type_rows()
collectible_rows = get_all_collectibles_rows()
lore_rows = get_all_lore_rows()
socket_rows = get_all_sockets_rows()
weapons_temp_rows = get_all_weapons_temp_rows()
weapons_rows = get_all_weapons_rows()
weaponstats_temp_rows = get_all_weaponstats_temp_rows()

stat_keys = ('hash', 'name', 'description')
damage_keys = ('hash', 'name', 'description', 'icon')
collectible_keys = ('hash', "sourcestring")
lore_keys = ('hash', 'description', 'subtitle')
socket_keys = ('hash', 'name', 'description', 'displayname', 'tiertype', 'icon')
weapons_temp_keys = (
    'hash', 'name', 'displayname', 'tiertype',
    'ammotype', 'equipmentslot', 'damagetype_id',
    'collectible_id', 'lore_id', 'flavortext',
    'icon', 'watermark', 'screenshot'
)
weaponstats_temp_keys = ('hash', 'stathash', 'value')

if __name__ == '__main__':
    process(stat_rows, stat_keys, StatModel, create_stats_table, insert_all_stats_rows, 'stats')
    process(damage_type_rows, damage_keys, DamageTypeModel, create_damage_type_table, insert_all_damage_type_rows, 'damage_type')
    process(collectible_rows, collectible_keys, CollectiblesModel, create_collectibles_table, insert_all_collectibles_rows, 'collectibles')
    process(lore_rows, lore_keys, LoreModel, create_lore_table, insert_all_lore_rows, 'lore')
    process(socket_rows, socket_keys, SocketsModel, create_sockets_table, insert_all_sockets_rows, 'sockets')
    process(weapons_temp_rows, weapons_temp_keys, WeaponsModel, create_weapons_temp_table, insert_all_weapons_temp_rows, 'weapons_temp')
    process(weapons_rows, weapons_temp_keys, WeaponsModel, create_weapons_table, insert_all_weapons_rows,
            'weapons')
    process(weaponstats_temp_rows, weaponstats_temp_keys, WeaponStatsModel, create_weaponstats_temp_table, insert_all_weaponstats_temp_rows, 'weaponstats_temp')
