from json import loads, dumps
from os import getenv
from subprocess import run, CalledProcessError

from requests import get

from kernel import ManifestPath


def get_manifest() -> dict:
    if not ManifestPath.exists():
        with open(ManifestPath, "w", encoding='utf-8') as file:
            with get("https://www.bungie.net/Platform/Destiny2/Manifest/", stream=True, allow_redirects=True,
                     headers={'x-api-key': getenv("APIKEY")}) as response:
                response.raise_for_status()
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
