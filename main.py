import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# 🔐 TOKEN
BOT_TOKEN = os.getenv("BOT_TOKEN")

# 📊 LOGS
logging.basicConfig(level=logging.INFO)

# =========================
# 🚀 /start avec boutons
# =========================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [InlineKeyboardButton("🟢 BUY SIGNAL", callback_data="buy")],
        [InlineKeyboardButton("🔴 SELL SIGNAL", callback_data="sell")],
        [InlineKeyboardButton("ℹ️ INFO", callback_data="info")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🤖 MOTEUR TRADING ACTIF 🔥\n\nChoisis une option :",
        reply_markup=reply_markup
    )

# =========================
# 🎯 CLICK BOUTONS
# =========================
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "buy":
        await query.edit_message_text("🟢 SIGNAL BUY CONFIRMÉ 🔥")

    elif query.data == "sell":
        await query.edit_message_text("🔴 SIGNAL SELL CONFIRMÉ ⚡")

    elif query.data == "info":
        await query.edit_message_text("📊 Bot de signaux actif\nVersion 1.0")

# =========================
# 🚀 MAIN
# =========================
def main():

    if not BOT_TOKEN:
        print("❌ BOT_TOKEN manquant")
        return

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("🤖 Bot démarré...")
    app.run_polling(drop_pending_updates=True)

# =========================
# ▶️ RUN
# =========================
if __name__ == "__main__":
    main()
