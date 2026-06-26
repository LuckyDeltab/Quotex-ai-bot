# strategy.py

from indicators import ema, rsi, macd

def get_signal(close_prices):
    ema20 = ema(close_prices, 20)
    rsi14 = rsi(close_prices, 14)
    macd_line, signal_line, histogram = macd(close_prices)

    last_ema = ema20.iloc[-1]
    last_price = close_prices.iloc[-1]
    last_rsi = rsi14.iloc[-1]
    last_macd = macd_line.iloc[-1]
    last_signal = signal_line.iloc[-1]

    if last_price > last_ema and last_rsi > 50 and last_macd > last_signal:
        return "BUY"

    elif last_price < last_ema and last_rsi < 50 and last_macd < last_signal:
        return "SELL"

    else:
        return "WAIT"
