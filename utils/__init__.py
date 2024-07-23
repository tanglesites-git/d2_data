from json import dump

import pandas as pd

from kernel import JsonDirectory, ExcelDirectory


def write_to_json(dictionary: dict, filename: str) -> None:
    with open(JsonDirectory / filename, "w", encoding="utf-8") as f:
        dump(dictionary, f, indent=4)


def write_to_excel(dictionary: dict, filename: str) -> None:
    df = pd.DataFrame(dictionary)
    df.to_excel(ExcelDirectory / filename, index=False)