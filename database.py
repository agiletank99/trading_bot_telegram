import sqlite3

conn = sqlite3.connect("trading.db", check_same_thread=False)
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS trades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT,
    asset TEXT,
    price REAL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)""")
conn.commit()

def log_trade(trade_type, asset, price):
    c.execute("INSERT INTO trades (type, asset, price) VALUES (?, ?, ?)", (trade_type, asset, price))
    conn.commit()

def get_account_summary():
    c.execute("SELECT COUNT(*), SUM(price) FROM trades")
    total, value = c.fetchone()
    return f"Totale operazioni: {total}\nValore totale: {value:.2f} USD" if value else "Nessuna operazione ancora."