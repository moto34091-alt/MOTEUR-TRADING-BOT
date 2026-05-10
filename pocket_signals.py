import random


def get_otc_signal():
    pairs = [
        "EUR/USD OTC",
        "GBP/USD OTC",
        "USD/JPY OTC",
        "EUR/JPY OTC",
        "AUD/USD OTC"
    ]

    directions = ["BUY 🟢", "SELL 🔴"]
    timings = ["15 SEC", "30 SEC", "1 MIN"]

    signal = {
        "pair": random.choice(pairs),
        "direction": random.choice(directions),
        "timing": random.choice(timings),
        "confidence": random.randint(88, 96)
    }

    return f"""
🔥 OTC SNIPER SIGNAL

PAIR: {signal['pair']}

SIGNAL: {signal['direction']}

EXPIRY: {signal['timing']}

ACCURACY: {signal['confidence']}%

⚡ AI Momentum Detected
"""
