from json import dumps

from application.dto.JsonPathsDto import JsonPathsDto
from application.dto.MobileGearAssetsDto import MobileGearAssetsDto
from application.dto.MobileGearDto import MobileGearDto
from application.dto.MobilePathsDto import MobilePathsDto


class ManifestResponseDto:

    def __init__(
            self,
            version: str,
            mobileAssetContentPath: str,
            mobileGearAssetDataBases: list[dict[str, str]],
            mobileWorldContentPaths: dict[str, str],
            jsonWorldContentPaths: dict[str, str],
            jsonWorldComponentContentPaths: dict[str, str],
            mobileClanBannerDatabasePath: str,
            mobileGearCDN: dict[str, str],
            iconImagePyramidInfo: dict[str, str]):
        self.version = version
        self.mobileAssetContentPath = mobileAssetContentPath
        self.mobileGearAssetDataBases = [MobileGearAssetsDto.From(x) for x in mobileGearAssetDataBases]
        self.mobileWorldContentPaths = MobilePathsDto.From(mobileWorldContentPaths)
        self.jsonWorldContentPaths = MobilePathsDto.From(jsonWorldContentPaths)
        self.jsonWorldComponentContentPaths = JsonPathsDto.From(jsonWorldComponentContentPaths)
        self.mobileClanBannerDatabasePath = mobileClanBannerDatabasePath
        self.mobileGearCDN = MobileGearDto.From(mobileGearCDN)
        self.iconImagePyramidInfo = iconImagePyramidInfo

    @classmethod
    def From(cls, value: dict):
        return cls(
            value['version'],
            value['mobileAssetContentPath'],
            value['mobileGearAssetDataBases'],
            value['mobileWorldContentPaths'],
            value['jsonWorldContentPaths'],
            value['jsonWorldComponentContentPaths'],
            value['mobileClanBannerDatabasePath'],
            value['mobileGearCDN'],
            value['iconImagePyramidInfo']
        )

    def __dict__(self):
        return {
            "version": self.version,
            "mobileAssetContentPath": self.mobileAssetContentPath,
            "mobileGearAssetDataBases": [x.__dict__() for x in self.mobileGearAssetDataBases],
            "mobileWorldContentPaths": self.mobileWorldContentPaths.__dict__(),
            "jsonWorldContentPaths": self.jsonWorldContentPaths.__dict__(),
            "jsonWorldComponentContentPaths": self.jsonWorldComponentContentPaths.__dict__(),
            "mobileClanBannerDatabasePath": self.mobileClanBannerDatabasePath,
            "mobileGearCDN": self.mobileGearCDN.__dict__(),
            "iconImagePyramidInfo": self.iconImagePyramidInfo
        }

    def __str__(self):
        return dumps(self.__dict__())

    def __iter__(self):
        return iter([self.version, self.mobileAssetContentPath, self.mobileGearAssetDataBases, self.mobileWorldContentPaths, self.jsonWorldContentPaths,
                     self.jsonWorldComponentContentPaths, self.mobileClanBannerDatabasePath, self.mobileGearCDN, self.iconImagePyramidInfo])

    def __repr__(self):
        return dumps(self.__dict__(), indent=4)