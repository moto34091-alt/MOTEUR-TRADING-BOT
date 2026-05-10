from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

from telegram.ext import (
    Updater,
    CommandHandler,
    CallbackContext,
    CallbackQueryHandler
)

import time

from config import (
    BOT_TOKEN,
    POCKET_LINK,
    PROMO_CODE,
    ADMIN_ID,
    FREE_SIGNALS_LIMIT,
    COOLDOWN
)

from pocket_signals import get_otc_signal
from binance_signals import get_binance_signal


users_data = {}


# ==========================
# INIT USER
# ==========================

def init_user(user_id):

    if user_id not in users_data:

        users_data[user_id] = {
            "signals_used": 0,
            "vip": False,
            "history": [],
            "last_signal_time": 0
        }


# ==========================
# START
# ==========================

def start(update: Update, context: CallbackContext):

    user_id = update.effective_user.id

    init_user(user_id)

    keyboard = [
        [InlineKeyboardButton("📊 OTC SIGNALS", callback_data="otc")],
        [InlineKeyboardButton("💹 BINANCE", callback_data="binance")],
        [InlineKeyboardButton("👤 ACCOUNT", callback_data="account")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(
        "🔥 OTC SNIPER PRO\n\nAI SIGNAL ENGINE READY",
        reply_markup=reply_markup
    )


# ==========================
# BUTTONS
# ==========================

def button_handler(update: Update, context: CallbackContext):

    query = update.callback_query

    query.answer()

    user_id = query.from_user.id

    init_user(user_id)

    data = query.data


    # ======================
    # OTC PANEL
    # ======================

    if data == "otc":

        keyboard = [
            [InlineKeyboardButton("⚡ GET SIGNAL", callback_data="signal")],
            [InlineKeyboardButton("🔗 REGISTER", url=POCKET_LINK)],
            [InlineKeyboardButton("⬅️ BACK", callback_data="back")]
        ]

        query.edit_message_text(
            f"🔥 OTC SIGNAL PANEL\n\nPROMO: {PROMO_CODE}",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


    # ======================
    # GET OTC SIGNAL
    # ======================

    elif data == "signal":

        current_time = time.time()

        if current_time - users_data[user_id]["last_signal_time"] < COOLDOWN:
            query.answer("⏳ WAIT...", show_alert=True)
            return

        if (
            users_data[user_id]["signals_used"] >= FREE_SIGNALS_LIMIT
            and not users_data[user_id]["vip"]
        ):

            query.edit_message_text(
                "🔒 FREE LIMIT REACHED\n\nVIP REQUIRED"
            )

            return

        signal = get_otc_signal()

        users_data[user_id]["signals_used"] += 1

        users_data[user_id]["last_signal_time"] = current_time

        users_data[user_id]["history"].append(signal)

        query.edit_message_text(signal)


    # ======================
    # BINANCE PANEL
    # ======================

    elif data == "binance":

        keyboard = [
            [InlineKeyboardButton("💹 GET SIGNAL", callback_data="binance_signal")],
            [InlineKeyboardButton("⬅️ BACK", callback_data="back")]
        ]

        query.edit_message_text(
            "💹 BINANCE AI PANEL",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


    # ======================
    # BINANCE SIGNAL
    # ======================

    elif data == "binance_signal":

        signal = get_binance_signal()

        query.edit_message_text(signal)


    # ======================
    # ACCOUNT
    # ======================

    elif data == "account":

        user = users_data[user_id]

        status = "VIP 👑" if user["vip"] else "FREE"

        text = f"""
👤 ACCOUNT

STATUS: {status}

USED SIGNALS: {user['signals_used']}

HISTORY: {len(user['history'])}
"""

        keyboard = [
            [InlineKeyboardButton("⬅️ BACK", callback_data="back")]
        ]

        query.edit_message_text(
            text,
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


    # ======================
    # BACK
    # ======================

    elif data == "back":

        keyboard = [
            [InlineKeyboardButton("📊 OTC SIGNALS", callback_data="otc")],
            [InlineKeyboardButton("💹 BINANCE", callback_data="binance")],
            [InlineKeyboardButton("👤 ACCOUNT", callback_data="account")]
        ]

        query.edit_message_text(
            "🔥 OTC SNIPER PRO\n\nAI SIGNAL ENGINE READY",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


# ==========================
# VIP ADMIN
# ==========================

def vip(update: Update, context: CallbackContext):

    if update.effective_user.id != ADMIN_ID:
        return

    try:

        target = int(context.args[0])

        init_user(target)

        users_data[target]["vip"] = True

        update.message.reply_text(
            f"✅ {target} VIP ENABLED"
        )

    except:

        update.message.reply_text(
            "/vip USER_ID"
        )


# ==========================
# MAIN
# ==========================

def main():

    updater = Updater(BOT_TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    dp.add_handler(CommandHandler("vip", vip))

    dp.add_handler(CallbackQueryHandler(button_handler))

    print("BOT STARTED")

    updater.start_polling()

    updater.idle()


if __name__ == "__main__":
    main()
