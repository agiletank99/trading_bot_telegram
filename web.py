import os
from flask import Flask
import scheduler  # Importa per avviare scheduler + bot

app = Flask(__name__)

@app.route('/')
def index():
    return "✅ Trading bot attivo su Render."

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Render passa la porta dinamicamente
    app.run(host='0.0.0.0', port=port)
