import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

# =========================
# 🎯 /start avec boutons
# =========================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📊 SIGNAL BUY 🟢", callback_data="buy")],
        [InlineKeyboardButton("📉 SIGNAL SELL 🔴", callback_data="sell")],
        [InlineKeyboardButton("ℹ️ AIDE", callback_data="help")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🤖 MOTEUR TRADING ACTIF 🔥\n\nChoisis une action :",
        reply_markup=reply_markup
    )

# =========================
# 🎯 ACTION DES BOUTONS
# =========================
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "buy":
        await query.edit_message_text("🟢 SIGNAL BUY CONFIRMÉ 🔥\nTendance haussière détectée")

    elif query.data == "sell":
        await query.edit_message_text("🔴 SIGNAL SELL CONFIRMÉ ⚡\nTendance baissière détectée")

    elif query.data == "help":
        await query.edit_message_text(
            "📌 COMMANDES :\n"
            "/start - menu principal\n"
            "Boutons pour générer signal"
        )

# =========================
# 🚀 MAIN
# =========================
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("🤖 Bot trading en ligne...")
    app.run_polling()

if __name__ == "__main__":
    main()
