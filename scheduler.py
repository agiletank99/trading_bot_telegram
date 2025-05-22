import asyncio
import threading
import schedule
import time

from trading import scalping_strategy, check_news
from bot import run_bot  # run_bot è una coroutine async

def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    # Programma gli eventi dello scheduler
    schedule.every(10).minutes.do(scalping_strategy)
    schedule.every(30).minutes.do(check_news)

    # Avvia scheduler in thread separato (daemon = chiude con il main)
    threading.Thread(target=run_schedule, daemon=True).start()

    # Avvia il bot Telegram nel main thread, correttamente con asyncio.run()
    asyncio.run(run_bot())
