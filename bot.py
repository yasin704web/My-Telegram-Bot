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

TRUST_CHANNEL = "https://t.me/+blrD4zwmKgwzNmE0"
SUPPORT_ID = "FF_Ranked0011"

# آیدی عددی خودت را اینجا بگذار
ADMIN_ID = 6847301983

# ذخیره کاربران
USERS = {}


app_web = Flask(__name__)


@app_web.route("/")
def home():
    return "Bot is running 🚀"


def run_web():
    app_web.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000))
    )


threading.Thread(target=run_web).start()



# پکیج
PACKAGE = [
    ("images/1.jpg", "متن آموزش 1"),
    ("images/2.jpg", "متن آموزش 2"),
    ("images/3.jpg", "متن آموزش 3"),
    ("images/4.jpg", "متن آموزش 4"),
    ("images/5.jpg", "متن آموزش 5"),
    ("images/6.jpg", "متن آموزش 6"),
    ("images/7.jpg", "متن آموزش 7"),
    ("images/8.jpg", "متن آموزش 8"),
    ("images/9.jpg", "متن آموزش 9"),
    ("images/10.jpg", "متن آموزش 10"),
    ("images/11.jpg", "متن آموزش 11"),
    ("images/12.jpg", "متن آموزش 12"),
    ("images/13.jpg", "متن آموزش 13"),
    ("images/14.jpg", "متن آموزش 14"),
    ("images/15.jpg", "متن آموزش 15"),
    ("images/16.jpg", "متن آموزش 16"),
    ("images/17.jpg", "متن آموزش 17"),
    ("images/18.jpg", "متن آموزش 18"),
    ("images/19.jpg", "متن آموزش 19"),
    ("images/20.jpg", "متن آموزش 20"),
    ("images/21.jpg", "متن آموزش 21"),
]



# استارت
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.message.from_user

    if user.username:
        USERS[user.username] = user.id


    keyboard = [
        [InlineKeyboardButton("🤖 پکیج ربات", callback_data="robot_pack")],
        [InlineKeyboardButton("⭐ چنل اعتماد", url=TRUST_CHANNEL)],
        [InlineKeyboardButton("📞 پشتیبانی", callback_data="support")]
    ]


    await update.message.reply_text(
        "🔥 به فروشگاه فایل حرفه‌ای خوش آمدید\n\n"
        "انتخاب کنید 👇",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )



# ارسال پکیج
async def send_package(chat_id, context):

    for img, text in PACKAGE:

        try:
            await context.bot.send_photo(
                chat_id=chat_id,
                photo=open(img, "rb"),
                caption=text
            )

        except Exception as e:
            print("خطا:", e)




# ارسال دستی توسط ادمین
async def send_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.message.from_user.id != ADMIN_ID:
        return


    if len(context.args) == 0:

        await update.message.reply_text(
            "مثال:\n/send 123456789"
        )

        return



    user_id = int(context.args[0])


    await update.message.reply_text(
        "📦 ارسال پکیج شروع شد..."
    )


    await send_package(
        user_id,
        context
    )



# دکمه‌ها
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()


    if query.data == "robot_pack":

        keyboard = [
            [
                InlineKeyboardButton(
                    "💰 خرید پکیج 199,000 تومان",
                    callback_data="buy"
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
            "📦 شامل آموزش کامل\n\n"
            "برای خرید بزن 👇",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )



    elif query.data == "buy":

        await query.message.reply_text(
            "💳 برای خرید با پشتیبانی تماس بگیرید."
        )



    elif query.data == "support":

        await query.edit_message_text(
            f"📞 پشتیبانی:\n@{SUPPORT_ID}"
        )



    elif query.data == "back":

        keyboard = [
            [InlineKeyboardButton("🤖 پکیج ربات", callback_data="robot_pack")],
            [InlineKeyboardButton("⭐ چنل اعتماد", url=TRUST_CHANNEL)],
            [InlineKeyboardButton("📞 پشتیبانی", callback_data="support")]
        ]


        await query.edit_message_text(
            "🔥 به فروشگاه فایل حرفه‌ای خوش آمدید",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )





bot = ApplicationBuilder().token(TOKEN).build()


bot.add_handler(
    CommandHandler("start", start)
)


bot.add_handler(
    CommandHandler("send", send_command)
)


bot.add_handler(
    CallbackQueryHandler(button)
)



print("ربات روشن شد 🚀")


bot.run_polling()
