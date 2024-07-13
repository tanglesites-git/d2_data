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


def iopenIO(filepath: Union[str, Path]):
    return {
        'file': filepath,
        'mode': 'w',
        'encoding': 'utf-8'
    }