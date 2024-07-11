from json import dumps

from domain import DestinyTables


class JsonPathsDto:

    def __init__(self,
                 en: dict,
                 fr: dict,
                 es: dict,
                 esmx: dict,
                 de: dict,
                 it: dict,
                 ja: dict,
                 ptbr: dict,
                 ru: dict,
                 pl: dict,
                 ko: dict,
                 zhcht: dict,
                 zhchs: dict):
        self.en = DestinyTables.From(en)
        self.fr = DestinyTables.From(fr)
        self.es = DestinyTables.From(es)
        self.esmx = DestinyTables.From(esmx)
        self.de = DestinyTables.From(de)
        self.it = DestinyTables.From(it)
        self.ja = DestinyTables.From(ja)
        self.ptbr = DestinyTables.From(ptbr)
        self.ru = DestinyTables.From(ru)
        self.pl = DestinyTables.From(pl)
        self.ko = DestinyTables.From(ko)
        self.zhcht = DestinyTables.From(zhcht)
        self.zhchs = DestinyTables.From(zhchs)

    @classmethod
    def From(cls, value: dict):
        return cls(
            value['en'],
            value['fr'],
            value['es'],
            value['es-mx'],
            value['de'],
            value['it'],
            value['ja'],
            value['pt-br'],
            value['ru'],
            value['pl'],
            value['ko'],
            value['zh-cht'],
            value['zh-chs']
        )

    def __str__(self):
        return (f'{{"en": "{self.en}", "fr": "{self.fr}", "es": "{self.es}", "es-mx": "{self.esmx}", "de": "{self.de}", "it": "{self.it}", "ja": "{self.ja}", '
                f'"pt-br": "{self.ptbr}", "ru": "{self.ru}", "pl": "{self.pl}", "ko": "{self.ko}", "zh-cht": "{self.zhcht}", "zh-chs": "{self.zhch}" }}')

    def __dict__(self):
        return {
            "en": self.en,
            "fr": self.fr,
            "es": self.es,
            "es-mx": self.esmx,
            "de": self.de,
            "it": self.it,
            "ja": self.ja,
            "pt-br": self.ptbr,
            "ru": self.ru,
            "pl": self.pl,
            "ko": self.ko,
            "zh-cht": self.zhcht,
            "zh-chs": self.zhchs
        }

    def __iter__(self):
        return iter([self.en, self.fr, self.es, self.esmx, self.de, self.it, self.ja, self.ptbr, self.ru, self.pl, self.ko, self.zhcht, self.zhchs])

    def __repr__(self):
        return dumps(self.__dict__(), indent=4)