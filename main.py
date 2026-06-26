# main.py

import pandas as pd
import numpy as np
from strategy import get_signal

# Generate sample market prices
prices = pd.Series(
    np.random.uniform(1.1000, 1.2000, 100)
)

signal = get_signal(prices)

print("=" * 40)
print("      AI Trading Signal Assistant")
print("=" * 40)
print(f"Current Signal: {signal}")
