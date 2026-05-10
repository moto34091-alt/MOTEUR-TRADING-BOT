import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# =========================
# 🔐 CONFIGURATION
# =========================
BOT_TOKEN = os.getenv("BOT_TOKEN")

# =========================
# 📊 LOGGING (utile debug)
# =========================
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# =========================
# 🚀 COMMAND /start
# =========================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Bot actif 🔥\n\nEnvoyez /help pour les commandes."
    )

# =========================
# ℹ️ COMMAND /help
# =========================
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📌 Commandes disponibles :\n"
        "/start - démarrer le bot\n"
        "/help - aide"
    )

# =========================
# 🧠 MAIN FUNCTION
# =========================
def main():
    if not BOT_TOKEN:
        print("❌ ERREUR: BOT_TOKEN introuvable dans les variables d'environnement")
        return

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    print("🤖 Bot en ligne...")
    app.run_polling()

# =========================
# ▶️ START
# =========================
if __name__ == "__main__":
    main()
