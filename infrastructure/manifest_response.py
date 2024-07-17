from typing import Union

from application.manifest_types.json_world_component_content_paths import JsonWorldComponentContentPaths
from application.manifest_types.json_world_content_paths import JsonWorldContentPaths
from application.manifest_types.mobile_gear_asset_databases import MobileGearAssetDataBases
from application.manifest_types.mobile_gear_cdn import MobileGearCDN
from application.manifest_types.mobile_world_content_paths import MobileWorldContentPaths


class ManifestResponse:

    def __init__(self,
                 version: str,
                 mobileAssetContentPath: str,
                 mobileGearAssetDataBases: list[dict[str, Union[str, int]]],
                 mobileWorldContentPaths: dict,
                 jsonWorldContentPaths: dict,
                 jsonWorldComponentContentPaths: dict[str, dict[str, str]],
                 mobileClanBannerDatabasePath: str,
                 mobileGearCDN: dict[str, str],
                 iconImagePyramidInfo: list):
        self.version = version
        self.mobileAssetContentPath = mobileAssetContentPath
        self.mobileGearAssetDataBases = MobileGearAssetDataBases.From(mobileGearAssetDataBases)
        self.mobileWorldContentPaths = MobileWorldContentPaths.From(mobileWorldContentPaths)
        self.jsonWorldContentPaths = JsonWorldContentPaths.From(jsonWorldContentPaths)
        self.jsonWorldComponentContentPaths = JsonWorldComponentContentPaths.From(jsonWorldComponentContentPaths)
        self.mobileClanBannerDatabasePath = mobileClanBannerDatabasePath
        self.mobileGearCDN = MobileGearCDN.From(mobileGearCDN)
        self.iconImagePyramidInfo = iconImagePyramidInfo

    @classmethod
    def From(cls, data: dict) -> "ManifestResponse":
        return cls(**data)

    def as_dict(self):
        return {
            "version": self.version,
            "mobileAssetContentPath": self.mobileAssetContentPath,
            "mobileGearAssetDataBases": [item.as_dict() for item in self.mobileGearAssetDataBases],
            "mobileWorldContentPaths": self.mobileWorldContentPaths.as_dict(),
            "jsonWorldContentPaths": self.jsonWorldContentPaths.as_dict(),
            "jsonWorldComponentContentPaths": self.jsonWorldComponentContentPaths.as_dict(),
            "mobileClanBannerDatabasePath": self.mobileClanBannerDatabasePath,
            "mobileGearCDN": self.mobileGearCDN.as_dict(),
            "iconImagePyramidInfo": self.iconImagePyramidInfo
        }