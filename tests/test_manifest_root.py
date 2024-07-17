from .fixtures import manifest, Response, Response_From, Root


def test_manifest_response_version(Response, manifest):
    assert Response.version == manifest["Response"]["version"]


def test_manifest_response_version_from(Response_From, manifest):
    assert Response_From.version == manifest["Response"]["version"]


def test_manifest_response_mobile_asset_content_path(Response, manifest):
    assert Response.mobileAssetContentPath == manifest["Response"]["mobileAssetContentPath"]


def test_manifest_response_mobile_asset_content_path_from(Response_From, manifest):
    assert Response_From.mobileAssetContentPath == manifest["Response"]["mobileAssetContentPath"]


def test_manifest_response_mobile_gear_asset_databases(Response, manifest):
    assert len(Response.mobileGearAssetDataBases) == 3
    assert Response.mobileGearAssetDataBases[0].path == manifest["Response"]["mobileGearAssetDataBases"][0]["path"]


def test_manifest_response_mobile_gear_asset_databases_from(Response_From, manifest):
    assert len(Response_From.mobileGearAssetDataBases) == 3
    assert Response_From.mobileGearAssetDataBases[0].path == manifest["Response"]["mobileGearAssetDataBases"][0]["path"]


def test_manifest_response_mobile_world_content_paths(Response, Response_From):
    assert len(Response.mobileWorldContentPaths) == 13
    assert len(Response_From.mobileWorldContentPaths) == 13
    assert Response.mobileWorldContentPaths.en is not None
    assert Response.mobileWorldContentPaths.en == Response_From.mobileWorldContentPaths.en


def test_manifest_response_json_world_content_paths(Response, Response_From):
    assert len(Response.jsonWorldContentPaths) == 13
    assert len(Response_From.jsonWorldContentPaths) == 13
    assert Response.jsonWorldContentPaths.en is not None
    assert Response.jsonWorldContentPaths.en == Response_From.jsonWorldContentPaths.en


def test_manifest_response_json_world_component_content_paths(Response, Response_From):
    assert len(Response.jsonWorldComponentContentPaths) == 13
    assert len(Response_From.jsonWorldComponentContentPaths) == 13
    assert Response.jsonWorldComponentContentPaths.en is not None
    assert (Response.jsonWorldComponentContentPaths.en.DestinyEquipmentSlotDefinition ==
            Response_From.jsonWorldComponentContentPaths.en.DestinyEquipmentSlotDefinition)

    assert len(Response.jsonWorldComponentContentPaths.en) == 88


def test_manifest_response_mobile_clan_banner_database_path(Response, Response_From):
    assert Response.mobileClanBannerDatabasePath is not None
    assert Response.mobileClanBannerDatabasePath == Response_From.mobileClanBannerDatabasePath


def test_manifest_response_mobile_gear_cdn(Response, Response_From):
    assert Response.mobileGearCDN is not None
    assert Response.mobileGearCDN.Texture == Response_From.mobileGearCDN.Texture


def test_manifest_root_response(Root, Response):
    assert Root.Response is not None
    assert Root.Response.version == Response.version
