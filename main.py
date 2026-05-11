import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ BOT ONLINE")

def main():

    if not BOT_TOKEN:
        print("❌ BOT_TOKEN MANQUANT")
        return

    print("✅ TOKEN OK")

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("🤖 BOT EN LIGNE")

    app.run_polling()

if __name__ == "__main__":
    main()
