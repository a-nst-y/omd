import json
a = """{
"title": "Вельш-корги",
"price": 1000,
"class": "dogs",
"location": {
"address": "сельское поселение Ельдигинское, поселок санатория Тишково, 25"
}
}"""


class Advert():
    """Shows advert (price and title) and checks if it's price exists and is right """
    repr_color_code = 32

    def __init__(self, ad):
        self.__dict__ = json.loads(ad)
        try:
            self.price = self.price
            if self.price < 0:
                self.price = 'ValueError: must be >= 0'
        except:
            self.price = 0

    def __repr__(self):
        return f'{self.title} | {self.price} ₽'


aa = Advert(a)
print(f'\033[1;33;40m{aa}')
