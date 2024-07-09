import json


def create_destiny_tables_class_params():
    with open("manifest.json", "r") as file:
        data = json.load(file)
        jwccp = data["Response"]["jsonWorldComponentContentPaths"]["en"].items()

        items = [f'{x[0]}: str, \n' for x in jwccp]

        print(''.join(items))


def create_destiny_tables_attributes():
    with open("manifest.json", "r") as file:
        data = json.load(file)
        jwccp = data["Response"]["jsonWorldComponentContentPaths"]["en"].items()

        items = [f'self.{x[0]} = {x[0]}\n' for x in jwccp]

        print(''.join(items))


def create_destiny_tables_from_values():
    with open("manifest.json", "r") as file:
        data = json.load(file)
        jwccp = data["Response"]["jsonWorldComponentContentPaths"]["en"].items()

        items = [f'value["{x[0]}"],\n' for x in jwccp]

        print(''.join(items))


def create_attributes_for_dict_dunder_method():
    with open("manifest.json", "r") as file:
        data = json.load(file)
        jwccp = data["Response"]["jsonWorldComponentContentPaths"]["en"].items()

        items = [f'"{x[0]}": self.{x[0]},\n' for x in jwccp]

        print(''.join(items))


def create_json_world_component_content_paths_list():
    with open("manifest.json", "r") as file:
        data = json.load(file)
        jwccp = data["Response"]["jsonWorldComponentContentPaths"]["en"].items()

        items = [f'self.{x[0]}' for x in jwccp]

        print(','.join(items))