from json import load


def settings():
    with open("settings.json", "r", encoding="utf-8") as file:
        return load(file)