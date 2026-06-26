# indicators.py

import pandas as pd
from ta.trend import EMAIndicator, MACD
from ta.momentum import RSIIndicator

def ema(close, period=20):
    return EMAIndicator(close=close, window=period).ema_indicator()

def rsi(close, period=14):
    return RSIIndicator(close=close, window=period).rsi()

def macd(close):
    m = MACD(close=close)
    return m.macd(), m.macd_signal(), m.macd_diff()
