"""Get stock price from Yahoo Finance API. Returns a random stock price from a list of tickers."""

import yfinance as yf
import random

tickers = [
    'AAPL',
    'MSFT',
    'NVDA',
    'BTC-USD',
    'ETH-USD',
    'KAS-USD',  # Kaspa
    'SREN.SW',  # Swiss Re
    'NOVN.SW',  # Novartis
    'ABBN.SW',  # Abb
    'RDDT',     # Reddit
    'GLEN.L',   # Glencore
    'UBSG.SW',  # UBS
    'ACLN.SW',  # Accelleron
    'PM',       # Philip Morris
    'TRX-USD',  # Tron
]


def get_stock_price(ticker):
    """Fetch the ticker of a chosen stock and return the ticker price with currency."""
    stock = yf.Ticker(ticker)
    todays_data = stock.history(period='1d')
    
    if not todays_data.empty:
        price = todays_data['Close'].iloc[0]
        currency = stock.info.get('currency', 'USD')
        # convert into format: 1'234.56
        price = "{:,.2f}".format(price)

        return f"{price} {currency}"
    else:
        return None  # Handle the absence of data

def get_ticker_price():
    """ Main method, gets ticker and sets Price in navbar """
    ticker = random.choice(tickers)
    price = get_stock_price(ticker)
    if price is None:
        price = "No data"  # Handle the case when there's no price

    return ticker, price