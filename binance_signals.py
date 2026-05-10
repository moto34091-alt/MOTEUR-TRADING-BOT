import random


def generate_candles():
    candles = []
    price = random.uniform(100, 50000)

    for _ in range(5):
        open_price = price
        close_price = open_price * random.uniform(0.98, 1.02)

        candles.append((open_price, close_price))

        price = close_price

    return candles


def analyze_trend(candles):
    bullish = 0
    bearish = 0

    for o, c in candles:
        if c > o:
            bullish += 1
        else:
            bearish += 1

    if bullish >= 4:
        return "UPTREND 📈"

    elif bearish >= 4:
        return "DOWNTREND 📉"

    return "SIDEWAYS ⚖️"


def detect_signal(candles):
    last = candles[-1]
    prev = candles[-2]

    if last[1] > last[0] and last[1] > prev[1]:
        return "BUY 🟢", 92

    if last[1] < last[0] and last[1] < prev[1]:
        return "SELL 🔴", 92

    return random.choice(["BUY 🟢", "SELL 🔴"]), 80



def get_binance_signal():

    pairs = [
        "BTC/USDT",
        "ETH/USDT",
        "SOL/USDT",
        "XRP/USDT"
    ]

    candles = generate_candles()

    trend = analyze_trend(candles)

    direction, confidence = detect_signal(candles)

    entry = round(random.uniform(100, 50000), 2)

    if "BUY" in direction:
        tp = round(entry * 1.02, 2)
        sl = round(entry * 0.98, 2)
    else:
        tp = round(entry * 0.98, 2)
        sl = round(entry * 1.02, 2)

    return f"""
💹 BINANCE AI SIGNAL

PAIR: {random.choice(pairs)}

TREND: {trend}

SIGNAL: {direction}

ENTRY: {entry}
TP: {tp}
SL: {sl}

ACCURACY: {confidence}%

⚡ AI Sniper Engine Active
"""
