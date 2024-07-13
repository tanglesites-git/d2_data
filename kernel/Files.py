from pathlib import Path


class Files:
    Root = Path(__file__).parent.parent
    ManifestJson = Root / 'manifest.json'
