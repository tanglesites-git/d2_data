from memory_profiler import memory_usage
from requests import get

from infrastructure import requests_json_files, extract_data, map_to_stat, map_to_damage_type, map_to_lore, map_to_equipment_slot, map_to_plug_set, \
    map_to_weapon_dto, create_all_directories
from utils import get_manifest
from time import perf_counter_ns
import concurrent.futures


print("Memory usage (Before): %s (kb)" % memory_usage(include_children=True, multiprocess=True))
start = perf_counter_ns()

manifest = get_manifest()
url_base = manifest.Response.jsonWorldComponentContentPaths.en

create_all_directories()
extract_data(url_base.DestinyStatDefinition, map_to_stat)
extract_data(url_base.DestinyDamageTypeDefinition, map_to_damage_type)
extract_data(url_base.DestinyLoreDefinition, map_to_lore)
extract_data(url_base.DestinyEquipmentSlotDefinition, map_to_equipment_slot)
extract_data(url_base.DestinyPlugSetDefinition, map_to_plug_set)

with get(**requests_json_files(manifest.Response.jsonWorldComponentContentPaths.en.DestinyInventoryItemDefinition)) as response:
    data = (x for x in response.json().items())
    objs = (y for y in [x for x in data if x[1]['itemType'] == 3])
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(map_to_weapon_dto, objs)

end = perf_counter_ns()
print("Memory usage (After): %s (kb)" % memory_usage(include_children=True, multiprocess=True))

if __name__ == '__main__':
    print(f"Time: {(end - start) / 1_000_000_000} s")
