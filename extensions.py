import requests
import json
from config import keys

class CatchExeption(Exception):
    pass
class SendRequest():
    @staticmethod
    def get_price(quote:str,base:str,amount:str):
        r=requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={keys[quote]}&tsyms={keys[base]}')
        single_base=json.loads(r.content)[keys[base]]
        return single_base
class CurrencyConverter(SendRequest):
    @staticmethod
    def convert(quote:str,base:str,amount:str):
        if quote==base:
            raise CatchExeption(f'Невозможно конвертировать одинаковые валюты {base}')
        try:
            base_ticker=keys[quote]
        except KeyError:
            raise CatchExeption(f'Не удалось обработать валюту {quote}')
        try:
            base_ticker=keys[base]
        except KeyError:
            raise CatchExeption(f'Не удалось обработать валюту {base}')  
        try:
            amount=float(amount)
        except ValueError:
            raise CatchExeption(f'Не удалось обработать количество {amount}')
        single_base=SendRequest.get_price(quote,base,amount)
        total_base=single_base*float(amount)   
        return total_base