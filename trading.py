import alpaca_trade_api as tradeapi
import database
import requests

API_KEY = "PKONC585CY600GY3GBIC"
SECRET_KEY = "VmbXNEjP4hqyDOyLDoCQN47p29i43KOIZIhBshFn"
URL = "https://paper-api.alpaca.markets"
api = tradeapi.REST(API_KEY, SECRET_KEY, URL)

def scalping_strategy():
    price = float(api.get_last_trade("BTC/USD").price)
    if price < 68000:
        api.submit_order("BTC/USD", 0.001, side="buy", type="market", time_in_force="gtc")
        database.log_trade("BUY", "BTC", price)

def check_news():
    r = requests.get("https://cryptopanic.com/news")
    if "ETF" in r.text or "regulation" in r.text:
        api.submit_order("BTC/USD", 0.001, side="sell", type="market", time_in_force="gtc")
        database.log_trade("SELL", "BTC", "news")