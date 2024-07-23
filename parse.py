from concurrent.futures import ProcessPoolExecutor
from time import perf_counter_ns
from typing import Callable

from memory_profiler import memory_usage

from infrastructure import parse_stat_definitions, parse_inventory_item_definitions, parse_collectible_definitions, parse_damage_type_definitions, \
    parse_socket_category_definitions, parse_plug_set_definitions, parse_lore_definitions, parse_weapon_stats


def execute_func(func: Callable):
    func()


def main():
    start = perf_counter_ns()
    mem_usage_start = memory_usage(include_children=True, multiprocess=True)
    print(f"Memory usage (Before): {mem_usage_start[0]}MiB")

    with ProcessPoolExecutor() as executor:
        executor.map(execute_func, [parse_stat_definitions, parse_inventory_item_definitions, parse_collectible_definitions, parse_damage_type_definitions,
                                    parse_socket_category_definitions, parse_plug_set_definitions, parse_lore_definitions, parse_weapon_stats])

    mem_usage_end = memory_usage(include_children=True, multiprocess=True)
    print(f"Memory usage (After): {mem_usage_end[0]}MiB")
    end = perf_counter_ns()
    print(f"Memory usage (Difference): {mem_usage_end[0][0] - mem_usage_start[0][0]}MiB")
    print(f"Time taken: {(end - start) / 1_000_000_000}s")


if __name__ == '__main__':
    main()
