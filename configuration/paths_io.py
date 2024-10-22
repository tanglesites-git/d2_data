from pathlib import Path


class PathsIO:
    ROOT_DIRECTORY = Path.cwd()
    DATA_DIRECTORY = ROOT_DIRECTORY / 'data'
    MANIFEST_FILENAME = ROOT_DIRECTORY / 'manifest.json'
    WORLD_CONTENT_FILENAME = ROOT_DIRECTORY / 'world_content.db'
    WORLD_CONTENT_ZIP_FILENAME = ROOT_DIRECTORY / 'world_content.zip'
    DICTIONARIES_DIRECTORY = DATA_DIRECTORY / 'dictionaries'
    DATAFRAME_DIRECTORY = DATA_DIRECTORY / 'data_frames'
    SQL_DIRECTORY = ROOT_DIRECTORY / 'sql'
    D2APP_SQL_DIRECTORY = SQL_DIRECTORY / 'd2_app'
    WORLD_CONTENT_SQL_DIRECTORY = SQL_DIRECTORY / 'world_content'
    def __init__(self):
        pass