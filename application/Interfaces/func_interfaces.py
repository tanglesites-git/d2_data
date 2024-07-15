from os import getenv
from pathlib import Path
from typing import Union


def irequest(url: str):
    return {
        'url': url,
        'headers': {'x-api-key': getenv('APIKEY')},
        'stream': True,
        'allow_redirects': True
    }


def irequest2(base_url: str):

    def get(url: str):
        return {
            'url': f'{base_url}{url}',
            'headers': {'x-api-key': getenv('APIKEY')},
            'stream': True,
            'allow_redirects': True
        }

    return get


def iopenIO(filepath: Union[str, Path], mode: str = "w"):
    return {
        'file': filepath,
        'mode': mode,
        'encoding': 'utf-8'
    }


def iopenIOBinary(directory: Union[str, Path], file_path: Union[str, Path], mode: str = "w"):
    return {
        'file': directory / file_path,
        'mode': mode,
        'encoding': 'utf-8'
    }


def iopenIOBinary2(directory: Union[str, Path], mode: str = "w"):

    def get(file_path: Union[str, Path]):
        return {
            'file': directory / file_path,
            'mode': mode,
            'encoding': 'utf-8'
        }

    return get
