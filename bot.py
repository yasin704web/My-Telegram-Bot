from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)
import os

TOKEN = os.getenv("TOKEN")

# آیدی چنل اعتماد را اینجا بگذار
TRUST_CHANNEL = "https://t.me/+blrD4zwmKgwzNmE0"


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
        "✅ محصولات کاربردی و تست‌شده\n"
        "✅ آموزش‌های ساده و کاربردی\n"
        "✅ پشتیبانی برای راهنمایی خرید\n\n"
        "محصول مورد نظر خود را انتخاب کنید 👇",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()


    if query.data == "robot_pack":

        keyboard = [
            [
                InlineKeyboardButton(
                    "📦 اطلاعات بیشتر",
                    callback_data="info"
                )
            ],
            [
                InlineKeyboardButton(
                    "🔙 برگشت",
                    callback_data="back"
                )
            ]
        ]

        await query.edit_message_text(
            "🤖 پکیج ربات تلگرام\n\n"
            "✔️ سورس آماده ربات\n"
            "✔️ آموزش نصب و راه‌اندازی\n"
            "✔️ مناسب برای شروع برنامه‌نویسی\n\n"
            "برای اطلاعات بیشتر گزینه زیر را بزنید 👇",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


    elif query.data == "info":

        await query.edit_message_text(
            "📦 این پکیج شامل فایل‌های مورد نیاز و آموزش کامل است.\n\n"
            "برای خرید و دریافت محصول با پشتیبانی در ارتباط باشید:\n\n"
            "@FF_Ranked0011"
        )


    elif query.data == "support":

        await query.edit_message_text(
            "📞 پشتیبانی فروشگاه\n\n"
            "برای سوالات و راهنمایی خرید پیام دهید:\n\n"
            "@FF_Ranked0011"
        )


    elif query.data == "back":

        await start(update, context)



app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

print("ربات فروش فایل روشن شد 🚀")

app.run_polling()from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes
)

TOKEN = "8762852784:AAGkCMHxM--AVlwa8UitXifwSa7zRCMsiiw"

# آیدی چنل اعتماد را اینجا بگذار
TRUST_CHANNEL = "https://t.me/+blrD4zwmKgwzNmE0"


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
        "✅ محصولات کاربردی و تست‌شده\n"
        "✅ آموزش‌های ساده و کاربردی\n"
        "✅ پشتیبانی برای راهنمایی خرید\n\n"
        "محصول مورد نظر خود را انتخاب کنید 👇",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()


    if query.data == "robot_pack":

        keyboard = [
            [
                InlineKeyboardButton(
                    "📦 اطلاعات بیشتر",
                    callback_data="info"
                )
            ],
            [
                InlineKeyboardButton(
                    "🔙 برگشت",
                    callback_data="back"
                )
            ]
        ]

        await query.edit_message_text(
            "🤖 پکیج ربات تلگرام\n\n"
            "✔️ سورس آماده ربات\n"
            "✔️ آموزش نصب و راه‌اندازی\n"
            "✔️ مناسب برای شروع برنامه‌نویسی\n\n"
            "برای اطلاعات بیشتر گزینه زیر را بزنید 👇",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


    elif query.data == "info":

        await query.edit_message_text(
            "📦 این پکیج شامل فایل‌های مورد نیاز و آموزش کامل است.\n\n"
            "برای خرید و دریافت محصول با پشتیبانی در ارتباط باشید:\n\n"
            "@FF_Ranked0011"
        )


    elif query.data == "support":

        await query.edit_message_text(
            "📞 پشتیبانی فروشگاه\n\n"
            "برای سوالات و راهنمایی خرید پیام دهید:\n\n"
            "@FF_Ranked0011"
        )


    elif query.data == "back":

        await start(update, context)



app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))

print("ربات فروش فایل روشن شد 🚀")

app.run_polling()import os
