from concurrent.futures import ProcessPoolExecutor
from time import perf_counter_ns
from typing import Callable

from memory_profiler import memory_usage

from infrastructure import parse_stat_definitions, parse_inventory_item_definitions, parse_collectible_definitions
from infrastructure.damage_type_definitions import parse_damage_type_definitions


# def parse_inner_json(value, dict_list: list):
#     for k, v in value.items():
#         if isinstance(v, dict):
#             parse_inner_json(v, dict_list)
#         elif isinstance(v, list) and all(isinstance(i, dict) for i in v):
#             [parse_inner_json(i, dict_list) for i in v]
#         else:
#             dict_list.append({k: v})
#
#
# def parse_json(filename: str, predicate: Callable = None) -> list:
#     dict_list = []
#     with open(DataDirectory / filename, "r", encoding="utf-8") as f:
#         data = json.load(f)
#         for key, value in data.items():
#             if predicate is not None and predicate(value):
#                 parse_inner_json(value, dict_list)
#
#     return dict_list
#
#
# def check_is_weapon(value: dict) -> bool:
#     return value["itemType"] == 3
#
#
def execute_func(func: Callable):
    func()


def main():
    start = perf_counter_ns()
    mem_usage_start = memory_usage(include_children=True, multiprocess=True)
    print(f"Memory usage (Before): {mem_usage_start[0]}MiB")

    with ProcessPoolExecutor() as executor:
        executor.map(execute_func, [parse_stat_definitions, parse_inventory_item_definitions, parse_collectible_definitions, parse_damage_type_definitions])

    mem_usage_end = memory_usage(include_children=True, multiprocess=True)
    print(f"Memory usage (After): {mem_usage_end[0]}MiB")
    end = perf_counter_ns()
    print(f"Memory usage (Difference): {mem_usage_end[0][0] - mem_usage_start[0][0]}MiB")
    print(f"Time taken: {(end - start) / 1_000_000_000}s")


if __name__ == '__main__':
    main()
