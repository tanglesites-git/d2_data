from os import getenv
from time import perf_counter_ns
from concurrent.futures import ThreadPoolExecutor

from memory_profiler import memory_usage
from requests import get

from infrastructure import get_manifest, ManifestRoot, run_docker
from kernel import DataDirectory


def get_filename(url: str) -> str:
    return url.split('/')[-1].split('-')[0]


def get_json_data(url: str) -> None:
    if not DataDirectory.exists():
        DataDirectory.mkdir(parents=True, exist_ok=True)
    filename = get_filename(url)
    with open(DataDirectory / f'{filename}.json', "w", encoding="utf-8") as file:
        with get(f'https://www.bungie.net{url}', stream=True, allow_redirects=True, headers={'x-api-key': getenv("APIKEY")}) as response:
            response.raise_for_status()
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk.decode("utf-8"))


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

    mem_usage_end = memory_usage(include_children=True, multiprocess=True)
    print(f"Memory usage (After): {mem_usage_end[0]}MiB")
    end = perf_counter_ns()
    print(f"Memory usage (Difference): {mem_usage_end[0][0] - mem_usage_start[0][0]}MiB")
    print(f"Time taken: {(end - start) / 1_000_000_000}s")
