from concurrent.futures import ThreadPoolExecutor
from json import JSONDecodeError, dumps, loads
from os import cpu_count, rename
from zipfile import ZipFile

from requests import get, HTTPError

from app_store import global_state
from configuration import PathsIO, configuration


def dynamic_download_signature(url: str):
    return {
        'url': f'{configuration.base_address}/{url}',
        'stream': True,
        'allow_redirects': True,
        'headers': {'x-api-key': configuration.apikey}
    }


def dynamic_write_signature(filename: str):
    return {
        'file': f'data/{filename}.json',
        'mode': 'w',
        'encoding': 'utf-8',
    }


download_manifest_signature = {
    'url': 'https://www.bungie.net/Platform/Destiny2/Manifest',
    'stream': True,
    'allow_redirects': True,
    'headers': {'x-api-key': configuration.apikey}
}

read_signature = {
    'file': 'manifest.json',
    'mode': 'r',
    'encoding': 'utf-8',
}

write_signature = {
    'file': 'manifest.json',
    'mode': 'w',
    'encoding': 'utf-8',
}


def read_manifest():
    try:
        if PathsIO.MANIFEST_FILENAME.exists():
            with open(**read_signature) as read_file:
                data_string = read_file.read()
                global_state.manifest_json = loads(data_string)
                global_state.manifest = data_string
        else:
            raise FileNotFoundError("Manifest file not found")
    except FileNotFoundError as e:
        print(e)
    except JSONDecodeError as e:
        print(f"Error decoding manifest: {e}")


def write_manifest(manifest: dict):
    try:
        if not PathsIO.MANIFEST_FILENAME.exists():
            print("Manifest was not found...")
            print("Proceeding as if this is the first run")
            with open(**write_signature) as write_file:
                print(f"Created {PathsIO.MANIFEST_FILENAME}")
                if isinstance(global_state.manifest_json, dict) and isinstance(global_state.manifest, str):
                    write_file.write(dumps(manifest, indent=2))
                    print("Manifest was written to disk")
        else:
            with open(**read_signature) as read_file:
                manifest_text = read_file.read()
                manifest_json = loads(manifest_text)
                old_version = manifest_json['Response']['version']
                new_version = manifest['Response']['version']
                if new_version != old_version:
                    print("Manifests version mismatch...")
                    with open(**write_signature) as write_file:
                        write_file.write(dumps(manifest, indent=2))
                        print("Manifest has been updated")
                        print("Manifest was written to disk")
                        global_state.manifest = dumps(manifest)
                        global_state.manifest_json = manifest
                        print("Updated Global State")
                else:
                    print("Manifest file is already up-to-date")

    except Exception as e:
        print(f"Error writing manifest: {e}")
        tb = e.__traceback__
        print(e.with_traceback(tb))


def download_manifest():
    with get(**download_manifest_signature) as response:
        m_json = response.json()
        m_text = response.text
        print(f"Downloaded Manifest: Version: {response.json()['Response']['version']}")
        global_state.manifest = m_text
        global_state.manifest_json = m_json
        print("Updated Global State")


def download_jwccp(url: str, filename: str):
    http_signature = dynamic_download_signature(url)
    io_signature = dynamic_write_signature(filename)
    if configuration.environment == 'production':
        try:
            if (PathsIO.ROOT_DIRECTORY / 'data' / f'{filename}.json').exists():
                print(f'data/{filename}.json already exists')
                return
            else:
                with open(**io_signature) as write_file:
                    with get(**http_signature) as response:
                        response.raise_for_status()
                        write_file.write(response.text)
                        print(f'Downloading: {filename}')
        except HTTPError as e:
            print(f'Bad Request: 404 Not Found {e}')
            tb = e.__traceback__
            print(e.with_traceback(tb))
    else:
        with open(**io_signature) as write_file:
            with get(**http_signature) as response:
                response.raise_for_status()
                write_file.write(response.text)
                print(f'Downloading: {filename}')


def download_all_jwccp(lang: str = "en"):
    url_list = []
    name_list = []
    json_world_component_content_paths = global_state.manifest_json["Response"]["jsonWorldComponentContentPaths"][lang]
    for k, v in json_world_component_content_paths.items():
        url_list.append(v)
        name_list.append(k)

    with ThreadPoolExecutor(cpu_count() - 1) as executor:
        executor.map(download_jwccp, url_list, name_list)


def download_world_content(lang: str = "en"):
    url = global_state.manifest_json["Response"]["mobileWorldContentPaths"][lang]
    signature = dynamic_download_signature(url)

    zip_filename = PathsIO.WORLD_CONTENT_ZIP_FILENAME
    with open(zip_filename, "wb") as f:
        print(f"Creating file {zip_filename}")
        with get(**signature) as response:
            response.raise_for_status()
            print(f"Downloading: {signature["url"]}")
            f.write(response.content)

    with ZipFile(zip_filename, "r") as zip_ref:
        print(f"Extracting {zip_filename}")
        random_file_name = zip_ref.namelist()[0]
        zip_ref.extract(random_file_name)

    rename(random_file_name, PathsIO.WORLD_CONTENT_FILENAME)
    print(f"Renaming {random_file_name} => {PathsIO.WORLD_CONTENT_FILENAME}")
    PathsIO.WORLD_CONTENT_ZIP_FILENAME.unlink()
    print(f"Deleting file: {random_file_name}")
    print("File downloaded and saved as world_content.db")


def initialize_manifest_data(lang: str = 'en'):
    if configuration.environment == 'production':
        download_manifest()
        write_manifest(global_state.manifest_json)
        download_all_jwccp()
        download_world_content()
    else:
        with open(**read_signature) as read_file:
            print("Entering Development Mode...")
            print("Reading Manifest From Disk...")
            global_state.manifest = read_file.read()
            global_state.manifest_json = loads(global_state.manifest)
            print("Updated Global State")
            download_all_jwccp()
            download_world_content()

if __name__ == '__main__':
    pass