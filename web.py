# web.py
import asyncio
import os
import scheduler  # questo avvia bot + scheduler
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "✅ Trading bot attivo su Render (via Web Service)."

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))  # Render imposta questa variabile
    app.run(host='0.0.0.0', port=port)
