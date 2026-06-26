# strategy.py

from indicators import ema, rsi, macd, supertrend

def get_signal():
    return {
        "EMA": ema(),
        "RSI": rsi(),
        "MACD": macd(),
        "SuperTrend": supertrend(),
        "Signal": "WAIT"
    }
