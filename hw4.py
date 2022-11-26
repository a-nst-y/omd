import keyword
import json


class CreateDict(object):
    """Динамически создает атрибуты из словаря
    и проверяет на совпадение с ключевыми словами"""

    def __init__(self, kwargs):
        for name in kwargs:
            val = kwargs[name]
            if isinstance(val, dict):
                val = CreateDict(val)
                if keyword.iskeyword(name):
                    name = 'aboba'
            if keyword.iskeyword(name):
                name = str(name) + "_"
            setattr(self, name, val)

    def __repr__(self):
        return f"{self.title} | {self.price} ₽"


class ColorizeMixin:
    """Возвращает название и цену в выбранном в классе цвете"""
    def __repr__(self):
        return f"\033[1;{self.repr_color_code};40m {self.title} | {self.price}\n"


class Advert(ColorizeMixin, CreateDict):
    """Работает с выбранным объявлением 
    и проверяет цену на корректность"""
    repr_color_code = 33

    def __init__(self, ad: dict):
        super().__init__(ad)
        if self.price is None:
            self.price = 0

    @property
    def price(self):
        if self.price_ < 0:
            raise ValueError("price must be >= 0")
        return self.price_

    @price.setter
    def price(self, ad_price):
        if ad_price < 0:
            raise ValueError("price must be >= 0")

        self.price_ = ad_price


if __name__ == '__main__':
    a = """{"title": "Вельш-корги", "price": 1000, "class": "dogs", "location": {"address":
        "сельское поселение Ельдигинское, поселок санатория Тишково, 25"}}"""
    corgi_ad = json.loads(a)
    corgi = Advert(corgi_ad)

