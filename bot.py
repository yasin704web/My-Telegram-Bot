import os
import threading

from flask import Flask
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)


TOKEN = os.getenv("TOKEN")

TRUST_CHANNEL = "https://t.me/USERNAME_CHANNEL"


# بخش وب برای Render
app_web = Flask(__name__)

@app_web.route("/")
def home():
    return "Bot is running 🚀"


def run_web():
    app_web.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))


# شروع وب سرور در کنار ربات
threading.Thread(target=run_web).start()


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
        "✅ محصولات کاربردی\n"
        "✅ پشتیبانی\n"
        "✅ فایل‌های آموزشی\n\n"
        "انتخاب کنید 👇",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    if query.data == "robot_pack":
        await query.edit_message_text(
            "🤖 پکیج ربات تلگرام\n\n"
            "برای خرید و اطلاعات بیشتر:\n"
            "@FF_Ranked0011"
        )

    elif query.data == "support":
        await query.edit_message_text(
            "📞 پشتیبانی:\n"
            "@FF_Ranked0011"
        )


bot = ApplicationBuilder().token(TOKEN).build()

bot.add_handler(CommandHandler("start", start))
bot.add_handler(CallbackQueryHandler(button))


print("ربات فروش فایل روشن شد 🚀")

bot.run_polling()
