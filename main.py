import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# 🔐 TOKEN (ENV)
BOT_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)


# =========================
# 🚀 START
# =========================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [InlineKeyboardButton("🟢 RECEVOIR SIGNAUX", callback_data="signals")],
        [InlineKeyboardButton("📊 ANALYSE", callback_data="scan")],
        [InlineKeyboardButton("⚡ MODE SNIPER", callback_data="sniper")]
    ]

    await update.message.reply_text(
"""🤖 BOT SIGNAL SNIPER

✔ SYSTEM ONLINE
✔ READY FOR ANALYSIS""",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# =========================
# 🎯 BUTTONS
# =========================
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    if query.data == "signals":
        await query.edit_message_text("🚨 SIGNAL: BUY NOW 🟢 (demo)")

    elif query.data == "scan":
        await query.edit_message_text("🧠 ANALYSE MARKET... OK")

    elif query.data == "sniper":
        await query.edit_message_text("⚡ SNIPER MODE ACTIVE")


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

    print("🤖 BOT RUNNING...")

    app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()
