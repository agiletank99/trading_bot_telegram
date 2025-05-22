# web.py
import asyncio
import scheduler  # questo importa e avvia scheduler + bot
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "✅ Trading bot attivo su Render (via Web Service)."

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
