import os

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
    MessageHandler,
    filters
)


TOKEN = os.getenv("TOKEN")

ADMIN_USERNAME = "@FF_Ranked0011"

CARD_NUMBER = "5022291518371222"

FILE_NAME = "ربات تلگرام"
PRICE = "160 هزار تومان"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [
            InlineKeyboardButton(
                "📞 پشتیبانی",
                callback_data="support"
            )
        ],
        [
            InlineKeyboardButton(
                "📂 فروش فایل",
                callback_data="file"
            )
        ]
    ]

    await update.message.reply_text(
        "سلام 👋\n\n"
        "من ربات Smartix هستم 🤖\n"
        "یک ربات هوشمند که به شما کمک می‌کنم.",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    if query.data == "support":

        await query.edit_message_text(
            "📞 پشتیبانی:\n"
            f"{ADMIN_USERNAME}"
        )


    elif query.data == "file":

        keyboard = [
            [
                InlineKeyboardButton(
                    "🛒 درخواست خرید",
                    callback_data="buy"
                )
            ]
        ]

        await query.edit_message_text(
            "📂 محصول:\n\n"
            f"🤖 {FILE_NAME}\n"
            f"💰 قیمت: {PRICE}\n\n"
            "برای خرید روی دکمه زیر بزنید 👇",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


    elif query.data == "buy":

        context.user_data["buying"] = True

        await query.edit_message_text(
            "🛒 درخواست خرید ثبت شد.\n\n"
            "لطفاً مبلغ را به کارت زیر واریز کنید:\n\n"
            f"💳 {CARD_NUMBER}\n\n"
            "بعد از پرداخت، عکس رسید را ارسال کنید."
        )


async def receipt(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if context.user_data.get("buying"):

        await update.message.forward(
            chat_id=update.message.chat_id
        )

        await update.message.reply_text(
            "✅ رسید شما دریافت شد.\n"
            "بعد از بررسی، فایل ارسال می‌شود."
        )


def main():

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.add_handler(
        CallbackQueryHandler(buttons)
    )

    app.add_handler(
        MessageHandler(
            filters.PHOTO,
            receipt
        )
    )

    print("Smartix Running ✅")

    app.run_polling()


if __name__ == "__main__":
    main()
