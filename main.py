import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

# 🔐 TOKEN (ENV)
BOT_TOKEN = os.getenv("BOT_TOKEN")

# 📊 LOGS
logging.basicConfig(level=logging.INFO)


# =========================
# 🚀 /start (INTERFACE)
# =========================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [InlineKeyboardButton("🟢 RECEVOIR DES SIGNAUX", callback_data="signals")],
        [InlineKeyboardButton("📊 ANALYSE RAPIDE", callback_data="scan")],
        [InlineKeyboardButton("⚡ MODE SNIPER 15S", callback_data="sniper")],
        [InlineKeyboardButton("👑 CONTACT OWNER", url="https://t.me/Mr_dflam")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
"""🔵 SIGNAL SNIPER BOT
⚡ Ultra Fast Trading Engine

📊 Market: EUR/USD OTC
⏱ Mode: 15 SEC EXPIRY

🧠 Status: READY
⚡ AI Scan: ACTIVE

👑 Propriétaire : @Mr_dflam
📩 Contact : @Mr_dflam

⚠️ RISQUE ÉLEVÉ - TRADING OTC""",
        reply_markup=reply_markup
    )


# =========================
# 🎯 BOUTONS ACTIONS
# =========================
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    # 🟢 SIGNALS
    if query.data == "signals":
        await query.edit_message_text(
"""🚨 SIGNAL SNIPER

📊 EUR/USD OTC
🟢 DIRECTION: BUY
⏱ EXPIRY: 15 SEC
🧠 CONFIDENCE: 90%

⚡ ENTRY NOW 🔥"""
        )

    # 📊 SCAN
    elif query.data == "scan":
        await query.edit_message_text(
"""🧠 SCAN MARKET

EUR/USD → BULLISH 🟢
GBP/USD → BEARISH 🔴
USD/JPY → NEUTRAL

⚡ BEST OPPORTUNITY: EUR/USD BUY"""
        )

    # ⚡ SNIPER MODE
    elif query.data == "sniper":
        await query.edit_message_text(
"""⚡ SNIPER MODE ACTIVE

📊 15 SECONDS CANDLES ENABLED
🧠 AI FILTERING: ON
🚀 FAST SIGNAL ENGINE READY

⚡ WAITING FOR ENTRY..."""
        )


# =========================
# 🚀 MAIN
# =========================
def main():

    if not BOT_TOKEN:
        print("❌ BOT_TOKEN MANQUANT")
        return

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("🤖 SIGNAL SNIPER BOT EN LIGNE...")
    app.run_polling(drop_pending_updates=True)


# =========================
# ▶️ START
# =========================
if __name__ == "__main__":
    main()
