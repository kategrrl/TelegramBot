import json
import requests
from config1 import keys


class ConvertionException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert(quote, base, amount):
        try:
            quote_key = keys[quote.lower()]
        except KeyError:
            raise ConvertionException(f' Валюта {quote} не найдена!')

        try:
            base_key = keys[base.lower()]
        except KeyError:
            raise ConvertionException(f'Валюта {base} не найдена!')
        if quote_key == base_key:
            raise ConvertionException(f'Невозможно перевести одинаковые валюты {base}!')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}!')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_key}&tsyms={base_key}')
        resp = json.loads(r.content)
        new_price = resp[base_key] * amount
        convert = round(new_price, 3)
        message = f"Цена {amount} {quote} в {base} : {convert}"
        return message



