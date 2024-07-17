class JsonWorldContentPaths:

    def __init__(self, en: str, fr: str, es: str, de: str, it: str, ja: str, pt_br: str, es_mx: str, ru: str, pl: str, ko: str, zh_cht: str, zh_chs: str):
        self.en = en
        self.fr = fr
        self.es = es
        self.de = de
        self.it = it
        self.ja = ja
        self.pt_br = pt_br
        self.es_mx = es_mx
        self.ru = ru
        self.pl = pl
        self.ko = ko
        self.zh_cht = zh_cht
        self.zh_chs = zh_chs

    @classmethod
    def From(cls, data: dict) -> "JsonWorldContentPaths":
        return cls(
            data["en"],
            data["fr"],
            data["es"],
            data["de"],
            data["it"],
            data["ja"],
            data["pt-br"],
            data["es-mx"],
            data["ru"],
            data["pl"],
            data["ko"],
            data["zh-cht"],
            data["zh-chs"]
        )

    def as_dict(self):
        return {
            "en": self.en,
            "fr": self.fr,
            "es": self.es,
            "es-mx": self.es_mx,
            "de": self.de,
            "it": self.it,
            "ja": self.ja,
            "pt-br": self.pt_br,
            "ru": self.ru,
            "pl": self.pl,
            "ko": self.ko,
            "zh-cht": self.zh_cht,
            "zh-chs": self.zh_chs
        }

    def __len__(self):
        return len(self.as_dict())