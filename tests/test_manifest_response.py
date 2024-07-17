from .fixtures import manifest, Response


def test_get_manifest(manifest):
    assert isinstance(manifest, dict)


def test_manifest_version(manifest):
    assert manifest["Response"]["version"] is not None


def test_manifest_mobile_asset_content(manifest):
    assert manifest["Response"]["mobileAssetContentPath"] is not None


def test_manifest_mobile_asset_databases(manifest):
    assert manifest["Response"]["mobileGearAssetDataBases"] is not None
    assert len(manifest["Response"]["mobileGearAssetDataBases"]) > 0


def test_manifest_mobile_world_content_paths(manifest):
    assert manifest["Response"]["mobileWorldContentPaths"] is not None
    assert manifest["Response"]["mobileWorldContentPaths"]["en"] is not None
    assert manifest["Response"]["mobileWorldContentPaths"]["fr"] is not None
    assert manifest["Response"]["mobileWorldContentPaths"]["es"] is not None
    assert manifest["Response"]["mobileWorldContentPaths"]["es-mx"] is not None
    assert manifest["Response"]["mobileWorldContentPaths"]["de"] is not None
    assert manifest["Response"]["mobileWorldContentPaths"]["it"] is not None
    assert manifest["Response"]["mobileWorldContentPaths"]["ja"] is not None
    assert manifest["Response"]["mobileWorldContentPaths"]["pt-br"] is not None
    assert manifest["Response"]["mobileWorldContentPaths"]["ru"] is not None
    assert manifest["Response"]["mobileWorldContentPaths"]["pl"] is not None
    assert manifest["Response"]["mobileWorldContentPaths"]["ko"] is not None
    assert manifest["Response"]["mobileWorldContentPaths"]["zh-cht"] is not None
    assert manifest["Response"]["mobileWorldContentPaths"]["zh-chs"] is not None


def test_manifest_json_world_content_paths(manifest):
    assert manifest["Response"]["jsonWorldContentPaths"] is not None
    assert manifest["Response"]["jsonWorldContentPaths"]["en"] is not None
    assert manifest["Response"]["jsonWorldContentPaths"]["fr"] is not None
    assert manifest["Response"]["jsonWorldContentPaths"]["es"] is not None
    assert manifest["Response"]["jsonWorldContentPaths"]["es-mx"] is not None
    assert manifest["Response"]["jsonWorldContentPaths"]["de"] is not None
    assert manifest["Response"]["jsonWorldContentPaths"]["it"] is not None
    assert manifest["Response"]["jsonWorldContentPaths"]["ja"] is not None
    assert manifest["Response"]["jsonWorldContentPaths"]["pt-br"] is not None
    assert manifest["Response"]["jsonWorldContentPaths"]["ru"] is not None
    assert manifest["Response"]["jsonWorldContentPaths"]["pl"] is not None
    assert manifest["Response"]["jsonWorldContentPaths"]["ko"] is not None
    assert manifest["Response"]["jsonWorldContentPaths"]["zh-cht"] is not None
    assert manifest["Response"]["jsonWorldContentPaths"]["zh-chs"] is not None


def test_manifest_json_world_component_content_paths(manifest):
    assert manifest["Response"]["jsonWorldComponentContentPaths"] is not None
    assert manifest["Response"]["jsonWorldComponentContentPaths"]["en"] is not None
    assert manifest["Response"]["jsonWorldComponentContentPaths"]["fr"] is not None
    assert manifest["Response"]["jsonWorldComponentContentPaths"]["es"] is not None
    assert manifest["Response"]["jsonWorldComponentContentPaths"]["es-mx"] is not None
    assert manifest["Response"]["jsonWorldComponentContentPaths"]["de"] is not None
    assert manifest["Response"]["jsonWorldComponentContentPaths"]["it"] is not None
    assert manifest["Response"]["jsonWorldComponentContentPaths"]["ja"] is not None
    assert manifest["Response"]["jsonWorldComponentContentPaths"]["pt-br"] is not None
    assert manifest["Response"]["jsonWorldComponentContentPaths"]["ru"] is not None
    assert manifest["Response"]["jsonWorldComponentContentPaths"]["pl"] is not None
    assert manifest["Response"]["jsonWorldComponentContentPaths"]["ko"] is not None
    assert manifest["Response"]["jsonWorldComponentContentPaths"]["zh-cht"] is not None
    assert manifest["Response"]["jsonWorldComponentContentPaths"]["zh-chs"] is not None


def test_manifest_mobile_clan_banner_database_path(manifest):
    assert manifest["Response"]["mobileClanBannerDatabasePath"] is not None


def test_manifest_mobile_gear_cdn(manifest):
    assert manifest["Response"]["mobileGearCDN"] is not None


def test_manifest_icon_image_pyramid_info(manifest):
    assert manifest["Response"]["iconImagePyramidInfo"] is not None
    assert len(manifest["Response"]["iconImagePyramidInfo"]) == 0


def test_manifest_response_as_dict(Response):
    res_dict = Response.as_dict()
    assert isinstance(res_dict, dict)
    assert res_dict["version"] == Response.version
    assert res_dict["mobileGearAssetDataBases"][0]['version'] == Response.mobileGearAssetDataBases[0].version
    assert res_dict["mobileWorldContentPaths"]["en"] == Response.mobileWorldContentPaths.en
    assert res_dict["jsonWorldContentPaths"]["en"] == Response.jsonWorldContentPaths.en
    assert (res_dict["jsonWorldComponentContentPaths"]["en"]["DestinyNodeStepSummaryDefinition"] ==
            Response.jsonWorldComponentContentPaths.en.DestinyNodeStepSummaryDefinition)
    assert res_dict["mobileClanBannerDatabasePath"] == Response.mobileClanBannerDatabasePath
    assert res_dict["mobileGearCDN"]["Texture"] == Response.mobileGearCDN.Texture
