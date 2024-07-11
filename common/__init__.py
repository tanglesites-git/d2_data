from .DirectoryPaths import DirectoryPaths
from .FilePaths import FilePaths
from .Settings import settings

config = settings()

__all__ = [
    DirectoryPaths,
    FilePaths,
    config,
]

if __name__ == '__main__':
    pass
