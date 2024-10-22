from features import process
from models import StatModel, DamageTypeModel, CollectiblesModel
from repositories import get_all_stats_rows, create_stats_table, insert_all_stats_rows, get_all_collectibles_rows, \
    create_collectibles_table, insert_all_collectibles_rows
from repositories import get_all_damage_type_rows, create_damage_type_table, insert_all_damage_type_rows

stat_rows = get_all_stats_rows()
damage_type_rows = get_all_damage_type_rows()
collectible_rows = get_all_collectibles_rows()

stat_keys = ('hash', 'name', 'description')
damage_keys = ('hash', 'name', 'description', 'icon')
collectible_keys = ('hash', "sourcestring")

if __name__ == '__main__':
    process(stat_rows, stat_keys, StatModel, create_stats_table, insert_all_stats_rows, 'stats')
    process(damage_type_rows, damage_keys, DamageTypeModel, create_damage_type_table, insert_all_damage_type_rows, 'damage_type')
    process(collectible_rows, collectible_keys, CollectiblesModel, create_collectibles_table, insert_all_collectibles_rows, 'collectibles')