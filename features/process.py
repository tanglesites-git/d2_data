from json import dump
from typing import Any

from configuration import PathsIO


def process(rows: list[tuple[int, str]], keys: tuple, model: Any, create_table, insert_rows, filename: str):
    d = {}
    df = {}

    for item in rows:
        dictionary = dict(zip(keys, item))
        stat_model = model.from_dict(dictionary)
        d[stat_model.id] = dictionary

        for key, value in dictionary.items():
            if key not in df:
                df[key] = [value]
                continue
            df[key].append(value)

    with open(PathsIO.DATAFRAME_DIRECTORY / f'{filename}.json', 'w', encoding='utf-8') as f1:
        dump(df, f1, ensure_ascii=False, indent=4)
        print(f"Creating Dataframe: {PathsIO.DATAFRAME_DIRECTORY / f'{filename}.json'}")

    with open(PathsIO.DICTIONARIES_DIRECTORY / f'{filename}.json', 'w', encoding='utf-8') as f2:
        dump(d, f2, ensure_ascii=False, indent=4)
        print(f"Creating Dictionary: {PathsIO.DICTIONARIES_DIRECTORY / f'{filename}.json'}")

    create_table()
    insert_rows(rows)

