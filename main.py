import os
import logging
from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

# =========================
# 🔐 TOKEN
# =========================
BOT_TOKEN = os.getenv("BOT_TOKEN")

# =========================
# 📊 LOGS
# =========================
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# =========================
# 🚀 START MENU
# =========================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [InlineKeyboardButton("📊 OTC MARKET", callback_data="otc")],
        [InlineKeyboardButton("📈 FOREX MARKET", callback_data="forex")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🤖 SIGNAL SNIPER BOT\n\nChoisis ton marché 👇",
        reply_markup=reply_markup
    )

# =========================
# 🎯 BUTTON HANDLER
# =========================
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    # =========================
    # OTC MARKET
    # =========================
    if query.data == "otc":

        keyboard = [
            [InlineKeyboardButton("⚡ 15 SECONDES", callback_data="15s")],
            [InlineKeyboardButton("⏱ 1 MINUTE", callback_data="1m")],
            [InlineKeyboardButton("📊 5 MINUTES", callback_data="5m")]
        ]

        await query.edit_message_text(
            "⏱ Choisis la durée 👇",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # =========================
    # ANALYSE
    # =========================
    elif query.data in ["15s", "1m", "5m"]:

        await query.edit_message_text(
f"""🧠 ANALYSE EN COURS...

📊 MARKET: EUR/USD OTC
⏱ TIMEFRAME: {query.data}

📈 RSI: 100%
⚡ MOMENTUM: 100%
🧱 STRUCTURE: VALID

🔥 POSITION: BUY NOW 🟢"""
        )

# =========================
# 🚀 MAIN
# =========================
def main():

    # ❌ TOKEN MANQUANT
    if not BOT_TOKEN:
        print("❌ BOT_TOKEN introuvable")
        return

    print("✅ TOKEN CHARGÉ")

    # 🚀 APP
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # HANDLERS
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("🤖 BOT EN LIGNE...")

    # ▶ RUN
    app.run_polling(drop_pending_updates=True)

# =========================
# ▶ START
# =========================
if __name__ == "__main__":
    main()
