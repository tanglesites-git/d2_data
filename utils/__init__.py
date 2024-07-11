from json import load

from application.dto.ManifestDto import ManifestDto
from infrastructure import gm_implemntation


def get_manifest() -> ManifestDto:
    with open(**gm_implemntation) as file:
        data = load(file)
        return ManifestDto.From(data)
