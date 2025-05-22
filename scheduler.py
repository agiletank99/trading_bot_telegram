import os
import schedule
import time
import threading
import asyncio

from trading import scalping_strategy, check_news
from bot import run_bot  # <-- run_bot ora è una coroutine async

# ✅ Controlla le variabili d'ambiente
required_vars = ["TOKEN", "APCA_API_KEY_ID", "APCA_API_SECRET_KEY", "APCA_API_BASE_URL"]
for var in required_vars:
    if not os.getenv(var):
        raise Exception(f"❌ Variabile '{var}' non trovata nell'ambiente!")

# ✅ Pianifica le funzioni
schedule.every(10).minutes.do(scalping_strategy)
schedule.every(30).minutes.do(check_news)

def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)

def start_bot():
    asyncio.run(run_bot())  # <-- Esegui la coroutine nel thread

if __name__ == '__main__':
    threading.Thread(target=start_bot).start()
    run_schedule()
