import pytest

from infrastructure import get_manifest, ManifestResponse, ManifestRoot


@pytest.fixture
def manifest():
    return get_manifest()


@pytest.fixture()
def Response():
    manifest = get_manifest()
    return ManifestResponse(**manifest["Response"])


@pytest.fixture()
def Response_From():
    manifest = get_manifest()
    return ManifestResponse.From(manifest["Response"])


@pytest.fixture()
def Root():
    manifest = get_manifest()
    return ManifestRoot(**manifest)
