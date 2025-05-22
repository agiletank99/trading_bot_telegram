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

    # Evita asyncio.run() se già esiste un event loop attivo (Render o Jupyter)
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = None

    if loop and loop.is_running():
        # Se siamo in un event loop attivo (es. render.com), usa create_task
        asyncio.create_task(run_bot())
        # Mantieni il main thread attivo per non chiudere il programma
        # Qui puoi fare un loop infinito o simile
        print("Event loop già attivo, bot avviato come task.")
        while True:
            time.sleep(1)
    else:
        # Se non c'è un event loop, lo creiamo e facciamo partire il bot
        asyncio.run(run_bot())
