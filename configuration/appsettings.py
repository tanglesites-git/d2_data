from configparser import ConfigParser

c = ConfigParser()
c.read('appsettings.ini')

class DestinyConfiguration:

    def __init__(self, apikey: str, base_address: str, environment: str):
        self._apikey = apikey
        self._base_address = base_address
        self._environment = environment

    @property
    def apikey(self) -> str:
        return self._apikey

    @property
    def base_address(self) -> str:
        return self._base_address

    @property
    def environment(self) -> str:
        return self._environment


configuration = DestinyConfiguration(c["Destiny"]['apikey'], c["Destiny"]['base_address'], c["variables"]['environment'])