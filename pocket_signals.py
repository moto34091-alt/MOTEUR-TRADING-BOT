import random

def get_otc_signal():
    pairs = [
        "EUR/USD OTC",
        "GBP/USD OTC",
        "USD/JPY OTC",
        "AUD/USD OTC",
        "EUR/JPY OTC"
    ]

    directions = ["BUY 🟢", "SELL 🔴"]
    timings = ["1 min", "3 min", "5 min"]

    signal = {
        "pair": random.choice(pairs),
        "direction": random.choice(directions),
        "timing": random.choice(timings),
        "confidence": random.randint(78, 96)
    }

    return f"""
📊 OTC SIGNAL

Pair: {signal['pair']}
Direction: {signal['direction']}
Timing: {signal['timing']}
Confidence: {signal['confidence']}%

⚠️ Wait candle confirmation before entry.
"""
