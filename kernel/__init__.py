from pathlib import Path

Root = Path(__file__).parent.parent
ManifestPath = Root / "manifest.json"
DataDirectory = Root / "data"
NotbookDirectory = Root / "notebooks" / "data"
ExcelDirectory = DataDirectory / "excel"
JsonDirectory = DataDirectory / "json"
MasterDirectory = DataDirectory / "master"

IconsUrl = "/common/destiny2_content/icons/"
ScreenshotsUrl = "/common/destiny2_content/screenshots/"
