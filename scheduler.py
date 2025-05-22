import schedule
import time
from trading import scalping_strategy, check_news
from bot import run_bot
import threading

schedule.every(10).minutes.do(scalping_strategy)
schedule.every(30).minutes.do(check_news)

def run_schedule():
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    threading.Thread(target=run_bot).start()
    run_schedule()