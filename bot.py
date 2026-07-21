import os

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)


TOKEN = os.getenv("TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    buttons = [
        [
            InlineKeyboardButton(
                "📞 پشتیبانی",
                callback_data="support"
            )
        ],
        [
            InlineKeyboardButton(
                "📂 فروش فایل 1",
                callback_data="file"
            )
        ]
    ]

    keyboard = InlineKeyboardMarkup(buttons)

    await update.message.reply_text(
        "سلام 👋\n\n"
        "من ربات Smartix هستم 🤖\n"
        "یک ربات هوشمند که به شما کمک می‌کنم.\n\n"
        "یکی از گزینه‌ها را انتخاب کنید 👇",
        reply_markup=keyboard
    )


async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    if query.data == "support":
        await query.edit_message_text(
            "📞 پشتیبانی:\n\n"
            "برای ارتباط با پشتیبانی پیام دهید."
        )

    elif query.data == "file":
        await query.edit_message_text(
            "📂 فروش فایل 1\n\n"
            "این بخش به زودی فعال می‌شود 🚀"
        )


def main():

    app = Application.builder().token(TOKEN).build()

    app.add_handler(
        CommandHandler("start", start)
    )

    app.add_handler(
        CallbackQueryHandler(buttons)
    )

    print("Smartix is running ✅")

    app.run_polling()


if __name__ == "__main__":
    main()
