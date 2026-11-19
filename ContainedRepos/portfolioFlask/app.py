import socket, logging
from flask import Flask, render_template, request, jsonify, Blueprint
from modules import stonks, methods
from modules.keys import EnviKeys
from modules.blueprints import errors_bp, projects_bp


logging.basicConfig(level=logging.INFO)
app = Flask(__name__)
app.register_blueprint(errors_bp)
app.register_blueprint(projects_bp)
keys = EnviKeys()
keys._validate_keys()
# update on py files under app.py
last_updated = methods.get_last_updated() # 13:23:45, 12 December 2024 example

@app.context_processor  # Global variable
def inject_now():
    return {'last_updated': last_updated}

@app.route('/get_emailJS_pub_key')
def get_key():
    return keys.emailjs_pub_key

@app.route('/', methods=['GET', 'POST']) 
def home():
    """Main Route + set ticker every 15 seconds."""
    
    if request.method == 'POST':
        user_ticker = request.form.get('ticker')
        price = stonks.get_stock_price(user_ticker)
        if price is None:
            price = "No data"
        return render_template('index.html', price=price, ticker=user_ticker)
    else:
        ticker, price = stonks.get_ticker_price()
        return render_template('index.html', price=price, ticker=ticker)

@app.route('/random_ticker') # called by JavaScript intervall 15s
def random_ticker():
    ticker, price = stonks.get_ticker_price()
    return jsonify({'ticker': ticker, 'price': price})


# app.py
if __name__ == '__main__':
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    app.run(host='0.0.0.0', port=5000, debug=True)

