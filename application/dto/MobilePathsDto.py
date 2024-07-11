from json import dumps


class MobilePathsDto:

    def __init__(self,
                 en: str,
                 fr: str,
                 es: str,
                 esmx: str,
                 de: str,
                 it: str,
                 ja: str,
                 ptbr: str,
                 ru: str,
                 pl: str,
                 ko: str,
                 zhcht: str,
                 zhchs: str):
        self.en = en
        self.fr = fr
        self.es = es
        self.esmx = esmx
        self.de = de
        self.it = it
        self.ja = ja
        self.ptbr = ptbr
        self.ru = ru
        self.pl = pl
        self.ko = ko
        self.zhcht = zhcht
        self.zhchs = zhchs

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