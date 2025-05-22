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

def start_scheduler_and_bot():
    # Avvia scheduler
    schedule.every(10).minutes.do(scalping_strategy)
    schedule.every(30).minutes.do(check_news)
    threading.Thread(target=run_schedule, daemon=True).start()

    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = None

    if loop and loop.is_running():
        asyncio.create_task(run_bot())
        print("✅ Event loop già attivo, bot avviato come task.")
    else:
        # Crea un nuovo loop in un thread separato, così non blocchi il main thread
        def start_bot_loop():
            new_loop = asyncio.new_event_loop()
            asyncio.set_event_loop(new_loop)
            new_loop.run_until_complete(run_bot())
        threading.Thread(target=start_bot_loop, daemon=True).start()

# Se importato da web.py, avvia il tutto
start_scheduler_and_bot()
