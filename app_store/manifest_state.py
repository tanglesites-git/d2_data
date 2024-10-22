class ManifestState:

    def __init__(self, manifest=None, manifest_json=None):
        self._manifest = manifest
        self._manifest_json = manifest_json

    @property
    def manifest(self):
        return self._manifest

    @manifest.setter
    def manifest(self, value):
        self._manifest = value

    @property
    def manifest_json(self):
        return self._manifest_json

    @manifest_json.setter
    def manifest_json(self, value):
        self._manifest_json = value

global_state = ManifestState()