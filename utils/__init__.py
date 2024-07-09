from json import load

from domain import Manifest
from infrastructure import gm_implemntation


def get_manifest() -> Manifest:
    with open(**gm_implemntation) as file:
        data = load(file)
        return Manifest.From(data)
