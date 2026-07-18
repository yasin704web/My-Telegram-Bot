import os

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)


TOKEN = os.getenv("TOKEN")

TRUST_CHANNEL = "https://t.me/USERNAME_CHANNEL"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [
            InlineKeyboardButton(
                "🤖 پکیج ربات",
                callback_data="robot_pack"
            )
        ],
        [
            InlineKeyboardButton(
                "⭐ چنل اعتماد",
                url=TRUST_CHANNEL
            )
        ],
        [
            InlineKeyboardButton(
                "📞 پشتیبانی",
                callback_data="support"
            )
        ]
    ]

    await update.message.reply_text(
        "🔥 به فروشگاه فایل حرفه‌ای خوش آمدید\n\n"
        "✅ محصولات کاربردی و تست شده\n"
        "✅ آموزش ساده و کاربردی\n"
        "✅ پشتیبانی برای راهنمایی\n\n"
        "انتخاب کنید 👇",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()


    if query.data == "robot_pack":

        await query.edit_message_text(
            "🤖 پکیج ربات تلگرام\n\n"
            "✔️ سورس آماده ربات\n"
            "✔️ آموزش نصب\n"
            "✔️ مناسب شروع برنامه نویسی\n\n"
            "برای خرید با پشتیبانی ارتباط بگیرید:\n"
            "@FF_Ranked0011"
        )


    elif query.data == "support":

        await query.edit_message_text(
            "📞 پشتیبانی فروشگاه\n\n"
            "پیام دهید:\n"
            "@FF_Ranked0011"
        )


app = ApplicationBuilder().token(TOKEN).build()


app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))


print("ربات فروش فایل روشن شد 🚀")


app.run_polling()
