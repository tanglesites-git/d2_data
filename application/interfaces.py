from common import settings, FilePaths, DirectoryPaths


def imanifestIO(filename: str, mode: str, encoding: str):
    return {
        'file': filename,
        'mode': mode,
        'encoding': encoding
    }


def irequests(stream: bool, allow_redirects: bool, headers: dict):
    def get(url: str):
        return {
            "url": f'{FilePaths.Bungie_Base_Url}{url}',
            "stream": stream,
            "allow_redirects": allow_redirects,
            "headers": headers
        }
    return get


def iopenIO(mode: str, encoding: str):
    def get(file_path: str):
        return {
            'file': DirectoryPaths.Data / f'{file_path}.json',
            'mode': mode,
            'encoding': encoding
        }
    return get
