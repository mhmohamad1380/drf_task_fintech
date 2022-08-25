from .models import Crypto
from requests import Session
from app.settings import COINMARKETCAP_APIKEY
import json
from celery import shared_task

@shared_task
def get_btc_price_from_cbc():
    print("Start...")
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?&symbol=btc'

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': COINMARKETCAP_APIKEY,
    }
    session = Session()
    session.headers.update(headers)
    response = session.get(url)
    data = json.loads(response.text)
    btc_info = data["data"]['BTC']
    duplicate_price = Crypto.objects.filter(
        coin_price=btc_info["quote"]["USD"]["price"])

    if not duplicate_price.exists():
        Crypto.objects.create(coin_name=btc_info["name"], coin_price_source="CoinMarketCap",
                              coin_price=btc_info["quote"]["USD"]["price"])
        print("Data Created...")
        if Crypto.objects.all().count() > 5:
            Crypto.objects.all().order_by("id").first().delete()
    print("Done...")
            
