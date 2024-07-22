from json import loads, dumps
from os import getenv
from subprocess import run, CalledProcessError

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


def write_to_json(dictionary: dict, filename: str) -> None:
    with open(JsonDirectory / filename, "w", encoding="utf-8") as f:
        dump(dictionary, f, indent=4)


def write_to_excel(dictionary: dict, filename: str) -> None:
    df = pd.DataFrame(dictionary)
    df.to_excel(ExcelDirectory / filename, index=False)
