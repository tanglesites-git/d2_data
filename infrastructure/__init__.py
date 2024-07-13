from concurrent.futures import ThreadPoolExecutor
from json import dumps, loads
from typing import Type

from requests import get

from application.Interfaces.func_interfaces import irequest, iopenIO
from kernel import Files, URI

manifest_irequest = irequest("https://www.bungie.net/Platform/Destiny2/Manifest/")
manifest_disk_write = iopenIO(Files.ManifestJson)


class ManifestService:

    @staticmethod
    def get_manifest():
        if Files.ManifestJson.exists():
            with open(Files.ManifestJson) as file:
                return loads(file.read())
        manifest_dict = download_manifest()
        write_manifest_to_disk(manifest_dict)
        return manifest_dict


def irequest_json_world_component_content_paths_wrapper(url: str):
    return irequest(f'{URI.BaseUrl}{url}')


def irequest_wrapper(url: str):
    return irequest(url)


def iopenIO_wrapper(filepath: str):
    return iopenIO(filepath)


def download_manifest():
    with get(**manifest_irequest) as response:
        if response.raise_for_status():
            return None
        return response.json()


def write_manifest_to_disk(response: dict):
    with open(**manifest_disk_write) as file:
        file.write(dumps(response, indent=2))


def download_json_world_component_content_paths(partial_filename: str, url: str):
    with open(f'{Dir.Data}/{partial_filename}.json', "w", encoding="utf-8") as file:
        with get(f'{URI.BaseUrl}{url}') as response:
            if response.raise_for_status():
                return {'error': response.raise_for_status(), 'url': url, 'filepath': partial_filename, 'status_code': response.status_code}
            file.write(response.text)


def download_json_files_multi_threaded(manifest_dict: dict, uri: Type[URI]):
    a, b = uri.init_JsonWorldComponentContentPaths(manifest_dict)

    with ThreadPoolExecutor() as executor:
        executor.map(download_json_world_component_content_paths, a, b)


if __name__ == '__main__':
    pass
