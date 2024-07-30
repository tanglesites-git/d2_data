from time import perf_counter_ns
from concurrent.futures import ThreadPoolExecutor

from memory_profiler import memory_usage

from infrastructure import get_manifest, ManifestRoot, get_json_data
from infrastructure.io import get_json_data1

if __name__ == '__main__':
    start = perf_counter_ns()
    mem_usage_start = memory_usage(include_children=True, multiprocess=True)
    print(f"Memory usage (Before): {mem_usage_start[0]}MiB")

    manifest_dict = get_manifest()
    manifest_root = ManifestRoot(**manifest_dict)
    files = manifest_root.Response.jsonWorldComponentContentPaths.en
    json_world_comp_content_urls = [
        files.DestinyInventoryItemDefinition,
        files.DestinyDamageTypeDefinition,
        files.DestinyStatDefinition,
        files.DestinyPlugSetDefinition,
        files.DestinyEquipmentSlotDefinition,
        files.DestinyCollectibleDefinition,
        files.DestinyLoreDefinition,
        files.DestinySocketCategoryDefinition
    ]
    with ThreadPoolExecutor() as executor:
        executor.map(get_json_data, json_world_comp_content_urls)

    with ThreadPoolExecutor() as executor:
        executor.map(get_json_data1, json_world_comp_content_urls)

    mem_usage_end = memory_usage(include_children=True, multiprocess=True)
    print(f"Memory usage (After): {mem_usage_end[0]}MiB")
    end = perf_counter_ns()
    print(f"Memory usage (Difference): {mem_usage_end[0][0] - mem_usage_start[0][0]}MiB")
    print(f"Time taken: {(end - start) / 1_000_000_000}s")
