from json import loads, dumps, dump
from os import getenv
from subprocess import run, CalledProcessError

import pandas as pd
from pybreaker import STATE_CLOSED, CircuitBreaker, CircuitMemoryStorage
from requests import get

from kernel import ManifestPath, DataDirectory, NotbookDirectory, JsonDirectory, ExcelDirectory

http_breaker = CircuitBreaker(
    fail_max=5,
    reset_timeout=10,
    state_storage=CircuitMemoryStorage(STATE_CLOSED), name="http_breaker")


@http_breaker
def download_manifest():
    with get("https://www.bungie.net/Platform/Destiny2/Manifest/", stream=True, allow_redirects=True,
             headers={'x-api-key': getenv("APIKEY")}) as response:
        response.raise_for_status()
        return response.json()


def get_manifest() -> dict:
    if not ManifestPath.exists():
        with open(ManifestPath, "w", encoding='utf-8') as file:
            response = download_manifest()
            file.write(dumps(response.json(), indent=2))

    with open(ManifestPath, "r", encoding='utf-8') as file:
        return loads(file.read())


def run_docker():
    try:
        run(["docker-compose", "up", "-d"], check=True)
        print("Docker container started")
    except CalledProcessError as e:
        print(f"Error starting docker container: {e}")
        exit(1)


def get_filename(url: str) -> str:
    return url.split('/')[-1].split('-')[0]


@http_breaker
def download_file(url: str) -> dict:
    with get(f'https://www.bungie.net{url}', stream=True, allow_redirects=True, headers={'x-api-key': getenv("APIKEY")}) as response:
        response.raise_for_status()
        return response.json()


def get_json_data(url: str) -> None:
    if not DataDirectory.exists():
        DataDirectory.mkdir(parents=True, exist_ok=True)
    filename = get_filename(url)
    with open(DataDirectory / f'{filename}.json', "w", encoding="utf-8") as file:
        response = download_file(url)
        file.write(dumps(response, indent=2))


def get_json_data1(url: str) -> None:
    if not NotbookDirectory.exists():
        NotbookDirectory.mkdir(parents=True, exist_ok=True)
    filename = get_filename(url)
    with open(NotbookDirectory / f'{filename}.json', "w", encoding="utf-8") as file:
        response = download_file(url)
        file.write(dumps(response, indent=2))


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