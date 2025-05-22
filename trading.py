import alpaca_trade_api as tradeapi
import database
import requests
import os

# ✅ Variabili d'ambiente corrette
API_KEY = os.getenv("APCA_API_KEY_ID")
SECRET_KEY = os.getenv("APCA_API_SECRET_KEY")
BASE_URL = os.getenv("APCA_API_BASE_URL", "https://paper-api.alpaca.markets")

api = tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL)

def scalping_strategy():
    try:
        last_trade = api.get_last_trade("BTC/USD")
        price = float(last_trade.price)
        print(f"[INFO] Prezzo BTC/USD: {price}")

        if price < 68000:
            api.submit_order(symbol="BTC/USD", qty=0.001, side="buy", type="market", time_in_force="gtc")
            database.log_trade("BUY", "BTC", price)
            print("[TRADE] Ordine BUY eseguito.")
    except Exception as e:
        print(f"[ERRORE] scalping_strategy: {e}")

def check_news():
    try:
        # ⚠️ Attenzione: questa è una simulazione
        r = requests.get("https://cryptopanic.com/news")  # Meglio usare API vera con key
        if "ETF" in r.text or "regulation" in r.text:
            api.submit_order(symbol="BTC/USD", qty=0.001, side="sell", type="market", time_in_force="gtc")
            database.log_trade("SELL", "BTC", "news")
            print("[TRADE] Ordine SELL per notizia.")
    except Exception as e:
        print(f"[ERRORE] check_news: {e}")
