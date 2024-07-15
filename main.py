from time import perf_counter_ns

from memory_profiler import memory_usage

from infrastructure import ManifestService, download_json_files_multi_threaded, create_weapons_file
from kernel import URI, Dir

if __name__ == '__main__':
    start = perf_counter_ns()
    mem_usage_start = memory_usage(include_children=True, multiprocess=True)
    print(f"Memory usage (Before): {mem_usage_start[0]}MiB")

    Dir.create_dirs()
    manifest = ManifestService.get_manifest()
    download_json_files_multi_threaded(manifest, URI)
    create_weapons_file()

    mem_usage_end = memory_usage(include_children=True, multiprocess=True)
    print(f"Memory usage (After): {mem_usage_end[0]}MiB")
    end = perf_counter_ns()
    print(f"Memory usage (Difference): {mem_usage_end[0][0] - mem_usage_start[0][0]}MiB")
    print(f"Time taken: {(end - start) / 1_000_000_000}s")
