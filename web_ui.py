from flask import Flask, render_template_string
import database

app = Flask(__name__)

@app.route('/')
def home():
    status = database.get_account_summary()
    return render_template_string("""
        <h1>Trading Dashboard</h1>
        <p>{{status}}</p>
    """, status=status)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)