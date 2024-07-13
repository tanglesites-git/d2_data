from pathlib import Path


class Dir:
    Root = Path(__file__).parent.parent
    Data = Root / 'data'

    @staticmethod
    def create_dirs():
        Dir.Root.mkdir(exist_ok=True, parents=True)
        Dir.Data.mkdir(exist_ok=True, parents=True)

