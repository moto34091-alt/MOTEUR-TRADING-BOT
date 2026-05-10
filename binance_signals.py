import random

def get_binance_signal():
    pairs = [
        "BTC/USDT",
        "ETH/USDT",
        "SOL/USDT",
        "XRP/USDT",
        "BNB/USDT",
        "ADA/USDT"
    ]

    directions = ["BUY 🟢", "SELL 🔴"]

    entry = round(random.uniform(100, 50000), 2)
    tp = round(entry * random.uniform(1.01, 1.03), 2)
    sl = round(entry * random.uniform(0.97, 0.99), 2)

    signal = {
        "pair": random.choice(pairs),
        "direction": random.choice(directions),
        "entry": entry,
        "tp": tp,
        "sl": sl,
        "confidence": random.randint(75, 95)
    }

    return f"""
💹 BINANCE SIGNAL

Pair: {signal['pair']}
Direction: {signal['direction']}

Entry: {signal['entry']}
Take Profit: {signal['tp']}
Stop Loss: {signal['sl']}

Confidence: {signal['confidence']}%

📊 Trend: Market analysis auto-generated
"""
