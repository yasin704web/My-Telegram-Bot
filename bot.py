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

# 🔑 توکن ربات (از Environment Variable بگیر)
TOKEN = os.getenv("TOKEN")

# 📢 لینک چنل اعتماد
TRUST_CHANNEL = "https://t.me/+blrD4zwmKgwzNmE0"

# 📞 آیدی پشتیبانی
SUPPORT_ID = "FF_Ranked0011"

# 🌐 وب سرور برای Render
app_web = Flask(__name__)

@app_web.route("/")
def home():
    return "Bot is running 🚀"

def run_web():
    app_web.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

# اجرای وب سرور در ترد جدا
threading.Thread(target=run_web).start()

# 🚀 دستور استارت
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

# 🎯 مدیریت دکمه‌ها
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    # 📦 پکیج ربات
    if query.data == "robot_pack":

        keyboard = [
            [InlineKeyboardButton("💰 خرید پکیج 199,000 تومان", url=f"https://t.me/{SUPPORT_ID}")],
            [InlineKeyboardButton("🔙 برگشت", callback_data="back")]
        ]

        await query.edit_message_text(
            "🤖 پکیج ربات تلگرام\n\n"
            "📦 شامل آموزش + سورس + راه‌اندازی کامل\n\n"
            "برای خرید روی دکمه زیر بزن 👇",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # 📞 پشتیبانی
    elif query.data == "support":
        await query.edit_message_text(
            f"📞 پشتیبانی:\n@{SUPPORT_ID}"
        )

    # 🔙 برگشت به منوی اصلی
    elif query.data == "back":

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

        await query.edit_message_text(
            "🔥 به فروشگاه فایل حرفه‌ای خوش آمدید\n\n"
            "✅ محصولات کاربردی\n"
            "✅ پشتیبانی\n"
            "✅ فایل‌های آموزشی\n\n"
            "انتخاب کنید 👇",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

# 🤖 اجرای ربات
bot = ApplicationBuilder().token(TOKEN).build()

bot.add_handler(CommandHandler("start", start))
bot.add_handler(CallbackQueryHandler(button))

print("ربات فروش فایل روشن شد 🚀")

bot.run_polling()
