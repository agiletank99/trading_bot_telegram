# web.py
import os
from flask import Flask
import scheduler  # importa solo per avviare lo scheduler e il bot

app = Flask(__name__)

@app.route('/')
def index():
    return "✅ Trading bot attivo su Render."

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Render imposta PORT dinamicamente
    app.run(host='0.0.0.0', port=port)

