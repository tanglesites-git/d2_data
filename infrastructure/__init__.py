from concurrent.futures import ThreadPoolExecutor
from json import dumps, loads
from typing import Type

from requests import get

from application.Interfaces.func_interfaces import irequest, iopenIO, iopenIOBinary2, irequest2
from application.dtos.WeaponDTO import WeaponDTO
from kernel import Files, URI, Dir

manifest_irequest = irequest("https://www.bungie.net/Platform/Destiny2/Manifest/")
manifest_disk_write = iopenIO(Files.ManifestJson)
enumerate_dict_read_diid = iopenIO(Files.DestinyInventoryItemDefinitionJson, "r")
create_weapon_file_write = iopenIO(Files.WeaponsJson)
download_json_world_component_content_paths_write = iopenIOBinary2(Dir.Definitions)
download_json_world_component_content_paths_get = irequest2(URI.BaseUrl)


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


# f'{Dir.Data}/{partial_filename}.json', "w", encoding="utf-8"
def download_json_world_component_content_paths(partial_filename: str, url: str):
    with open(**download_json_world_component_content_paths_write(f'{partial_filename}.json')) as file:
        with get(**download_json_world_component_content_paths_get(url)) as response:
            if response.raise_for_status():
                return {'error': response.raise_for_status(), 'url': url, 'filepath': partial_filename, 'status_code': response.status_code}
            file.write(response.text)


def download_json_files_multi_threaded(manifest_dict: dict, uri: Type[URI]):
    a, b = uri.init_JsonWorldComponentContentPaths(manifest_dict)

    with ThreadPoolExecutor() as executor:
        executor.map(download_json_world_component_content_paths, a, b)


def enumerate_dict():
    with open(**enumerate_dict_read_diid) as file1:
        data = loads(file1.read())
        for k, v in data.items():
            if "itemType" in v:
                if v["itemType"] == 3:
                    yield k, v


def create_weapons_file():
    weapons = {}
    for key, value in enumerate_dict():
        weapon = WeaponDTO.From(value)
        weapons[key] = weapon.__dict__()
    with open(**create_weapon_file_write) as file:
        file.write(dumps(weapons, indent=2))


if __name__ == '__main__':
    pass
