import concurrent.futures
from json import dumps
from pathlib import Path

from requests import get

from application.dto.DamageTypeDto import DamageTypeDto
from application.dto.LoreDto import LoreDto
from application.dto.ManifestDto import ManifestDto
from application.dto.PlugSetDto import PlugSetTypeDto
from application.dto.SlotTypeDto import SlotTypeDto
from application.dto.StatsDto import StatsDto
from application.dto.WeaponDto import WeaponDto
from application.interfaces import imanifestIO, irequests, iopenIO
from common import config, DirectoryPaths

directory_list = [
    DirectoryPaths.DestinyInventoryItemDefinition,
    DirectoryPaths.DestinyStatDefinition,
    DirectoryPaths.DestinyDamageTypeDefinition,
    DirectoryPaths.DestinySlotTypeDefinition,
    DirectoryPaths.DestinyLoreDefinition,
    DirectoryPaths.DestinyPlugSetDefinition,
    DirectoryPaths.DestinyEquipmentSlotDefinition
]

gm_implemntation = imanifestIO("manifest.json", "r", "utf-8")

requests_json_files = irequests(stream=True, allow_redirects=True, headers={'x-api-key': config["x-api-key"]})

create_json_files_IO = iopenIO("w", "utf-8")

append_json_files_IO = iopenIO("a", "utf-8")


def get_json_component_content_path_destiny_inventory_item_definition(filepath_name: str, url: str):
    with open(**create_json_files_IO(filepath_name)) as file_zero:
        file_zero.write("")
    with open(**append_json_files_IO(filepath_name)) as file_one:
        with get(**requests_json_files(url)) as response:
            data = (x for x in response.json().items())
            objs = (y for y in [x for x in data if x[1]['itemType'] == 3])
            [file_one.write(str(y) + '\n') for y in [WeaponDto.From(x[1]) for x in objs]]


def get_json_component_content_path_destiny_stats(filepath_name: str, url: str):
    with open(**create_json_files_IO(filepath_name)) as file_zero:
        file_zero.write("")
    with open(**append_json_files_IO(filepath_name)) as file_one:
        with get(**requests_json_files(url)) as response:
            data = (x for x in response.json().items())
            objs = (y for y in [x for x in data])
            [file_one.write(str(y) + '\n') for y in [StatsDto.From(x[1]) for x in objs]]


def get_json_component_content_path_destiny_damage_types(filepath_name: str, url: str):
    with open(**create_json_files_IO(filepath_name)) as file_zero:
        file_zero.write("")
    with open(**append_json_files_IO(filepath_name)) as file_one:
        with get(**requests_json_files(url)) as response:
            data = (x for x in response.json().items())
            objs = (y for y in [x for x in data])
            [file_one.write(str(y) + '\n') for y in [DamageTypeDto.From(x[1]) for x in objs]]


def get_json_component_content_path_destiny_slot_type(filepath_name: str, url: str):
    with open(**create_json_files_IO(filepath_name)) as file_zero:
        file_zero.write("")
    with open(**append_json_files_IO(filepath_name)) as file_one:
        with get(**requests_json_files(url)) as response:
            data = (x for x in response.json().items())
            objs = (y for y in [x for x in data])
            [file_one.write(str(y) + '\n') for y in [SlotTypeDto.From(x[1]) for x in objs]]


def get_json_component_content_path_destiny_lore(filepath_name: str, url: str):
    with open(**create_json_files_IO(filepath_name)) as file_zero:
        file_zero.write("")
    with open(**append_json_files_IO(filepath_name)) as file_one:
        with get(**requests_json_files(url)) as response:
            data = (x for x in response.json().items())
            objs = (y for y in [x for x in data])
            [file_one.write(str(y) + '\n') for y in [LoreDto.From(x[1]) for x in objs]]


def create_json_files(manifest: ManifestDto):
    get_json_component_content_path_destiny_inventory_item_definition('DestinyInventoryItemDefinition', manifest.Response
                                                                      .jsonWorldComponentContentPaths.en.DestinyInventoryItemDefinition)
    get_json_component_content_path_destiny_stats('DestinyStatDefinition', manifest.Response.jsonWorldComponentContentPaths.en.DestinyStatDefinition)
    get_json_component_content_path_destiny_damage_types('DestinyDamageTypeDefinition', manifest.Response
                                                         .jsonWorldComponentContentPaths.en.DestinyDamageTypeDefinition)
    get_json_component_content_path_destiny_slot_type('DestinySlotTypeDefinition', manifest.Response
                                                      .jsonWorldComponentContentPaths.en.DestinyEquipmentSlotDefinition)
    get_json_component_content_path_destiny_lore('DestinyLoreDefinition', manifest.Response.jsonWorldComponentContentPaths.en.DestinyLoreDefinition)


def map_to_weapon_dto(x):
    with open(DirectoryPaths.DestinyInventoryItemDefinition / f"{x[0]}.json", 'w') as file:
        file.write(dumps(WeaponDto.From(x[1]).__dict__(), indent=2))


def map_to_stat(x):
    with open(DirectoryPaths.DestinyStatDefinition / f"{x[0]}.json", 'w') as file:
        file.write(dumps(StatsDto.From(x[1]).__dict__(), indent=2))


def map_to_damage_type(x):
    with open(DirectoryPaths.DestinyEquipmentSlotDefinition / f"{x[0]}.json", 'w') as file:
        file.write(dumps(DamageTypeDto.From(x[1]).__dict__(), indent=2))


def map_to_lore(x):
    with open(DirectoryPaths.DestinyLoreDefinition / f"{x[0]}.json", 'w') as file:
        file.write(dumps(LoreDto.From(x[1]).__dict__(), indent=2))


def map_to_equipment_slot(x):
    with open(DirectoryPaths.DestinyEquipmentSlotDefinition / f"{x[0]}.json", 'w') as file:
        file.write(dumps(SlotTypeDto.From(x[1]).__dict__(), indent=2))


def map_to_plug_set(x):
    with open(DirectoryPaths.DestinyPlugSetDefinition / f"{x[0]}.json", 'w') as file:
        file.write(dumps(PlugSetTypeDto.From(x[1]).__dict__(), indent=2))


def extract_data(url: Path, func: callable):
    with get(**requests_json_files(url)) as res:
        data = (x for x in res.json().items())
        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(func, data)


def create_all_directories():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(DirectoryPaths.create_data_directory, directory_list)
