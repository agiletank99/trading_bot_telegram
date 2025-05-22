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

    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = None

    if loop and loop.is_running():
        # Se event loop è già attivo (es. Render), crea un task e tieni vivo il main thread
        asyncio.create_task(run_bot())
        print("Event loop già attivo, bot avviato come task.")
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("Terminazione richiesta dall'utente.")
    else:
        # Se non c'è event loop, crea e avvia con asyncio.run()
        asyncio.run(run_bot())
