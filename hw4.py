import keyword
from typing import Any


class Dict:
    def __init__(self, json: dict, is_keyword=lambda x: keyword.iskeyword(x)):
        self._json = json
        self._is_keyword = is_keyword

    def __underlying(self, attrname: str):
        if attrname[-1] == "_" and self._is_keyword(attrname[:-1]):
            return attrname[:-1]

        return attrname

    def __getattr__(self, attrname: str) -> Any:
        underlying = self.__underlying(attrname)
        attr = self._json.get(underlying)
        if attr is None:
            return attr

        value = Dict(attr) if isinstance(attr, dict) else attr
        setattr(self, attrname, value)
        return getattr(self, attrname)


class ColorizeMixin:
    """returns name and price in chosen colour"""
    def __repr__(self, text):
        return f"\033[1;{self.repr_color_code};40m {text}\n"


class Advert(ColorizeMixin, Dict):
    repr_color_code = 33

    def __init__(self, json: dict):
        super().__init__(json, lambda x: x == "price")
        if self.price is None:
            self.price = 0

    def __repr__(self):
        advert = f"{self.title} | {self.price} ₽"
        return super().__repr__(advert)

    @property
    def price(self):
        """checks if price is valid"""
        if self.price_ < 0:
            raise ValueError("must be >= 0")
        return self.price_


if __name__ == '__main__':
    a = {"title": "Вельш-корги", "price": 1000, "class": "dogs", "location": {"address":
        "сельское поселение Ельдигинское, поселок санатория Тишково, 25"}}
    corgi = Advert(a)
    print(corgi)
    print(corgi.price)
    print(corgi.location)
    print(corgi.location.address)
    print(corgi.class_)
