from pathlib import Path

Root = Path(__file__).parent.parent
ManifestPath = Root / "manifest.json"
DataDirectory = Root / "data"
NotbookDirectory = Root / "notebooks" / "data"
ExcelDirectory = DataDirectory / "excel"
JsonDirectory = DataDirectory / "json"
FooDirectory = DataDirectory / "foo"
