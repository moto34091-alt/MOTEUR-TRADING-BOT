from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler

from config import BOT_TOKEN, POCKET_LINK, PROMO_CODE
from pocket_signals import get_otc_signal
from binance_signals import get_binance_signal

# ===============================
# START MENU
# ===============================
def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("📊 Pocket Option OTC", callback_data="pocket")],
        [InlineKeyboardButton("💹 Binance Signals", callback_data="binance")],
        [InlineKeyboardButton("👤 Mon compte", callback_data="account")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(
        "🚀 *MOTEUR TRADING BOT*\n\nChoisissez une option :",
        parse_mode="Markdown",
        reply_markup=reply_markup
    )

# ===============================
# BUTTON HANDLER
# ===============================
def button_handler(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()

    data = query.data

    # -----------------------
    # POCKET OPTION PANEL
    # -----------------------
    if data == "pocket":
        keyboard = [
            [InlineKeyboardButton("📊 Get Signal", callback_data="pocket_signal")],
            [InlineKeyboardButton("🔗 Register", url=POCKET_LINK)],
            [InlineKeyboardButton("⬅️ Back", callback_data="back")]
        ]

        query.edit_message_text(
            f"📊 *POCKET OPTION OTC*\n\nCode promo: `{PROMO_CODE}`",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif data == "pocket_signal":
        signal = get_otc_signal()
        query.edit_message_text(signal)

    # -----------------------
    # BINANCE PANEL
    # -----------------------
    elif data == "binance":
        keyboard = [
            [InlineKeyboardButton("💹 Get Signal", callback_data="binance_signal")],
            [InlineKeyboardButton("⬅️ Back", callback_data="back")]
        ]

        query.edit_message_text(
            "💹 *BINANCE SIGNALS PANEL*\n\nSignals crypto en temps réel (simulation).",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif data == "binance_signal":
        signal = get_binance_signal()
        query.edit_message_text(signal)

    # -----------------------
    # BACK MENU
    # -----------------------
    elif data == "back":
        start_from_callback(query)

# ===============================
# BACK TO START
# ===============================
def start_from_callback(query):
    keyboard = [
        [InlineKeyboardButton("📊 Pocket Option OTC", callback_data="pocket")],
        [InlineKeyboardButton("💹 Binance Signals", callback_data="binance")],
        [InlineKeyboardButton("👤 Mon compte", callback_data="account")]
    ]

    query.edit_message_text(
        "🚀 *MOTEUR TRADING BOT*\n\nChoisissez une option :",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

# ===============================
# ACCOUNT (simple placeholder)
# ===============================
def account(update: Update, context: CallbackContext):
    update.message.reply_text(
        "👤 Compte utilisateur\n\n- Statut: FREE\n- Upgrade bientôt disponible"
    )

# ===============================
# MAIN
# ===============================
def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("account", account))
    dp.add_handler(CallbackQueryHandler(button_handler))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
