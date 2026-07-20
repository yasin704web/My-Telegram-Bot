import os
import threading

from flask import Flask
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    ContextTypes,
    filters
)


TOKEN = os.getenv("TOKEN")

TRUST_CHANNEL = "https://t.me/+blrD4zwmKgwzNmE0"
SUPPORT_ID = "6847301983"

ADMIN_ID = 6847301983


# ذخیره کاربران
USERS = {}

# ذخیره پکیج عکس و متن
PACKAGE = []


# برای روشن ماندن در Render
app_web = Flask(__name__)


@app_web.route("/")
def home():
    return "Bot is running 🚀"


def run_web():
    app_web.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000))
    )


threading.Thread(
    target=run_web,
    daemon=True
).start()



# استارت ربات
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user = update.message.from_user

    if user.username:
        USERS[user.username] = user.id


    keyboard = [
        [
            InlineKeyboardButton(
                "📦 پکیج",
                callback_data="package"
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
        "🔥 خوش آمدید\n\nانتخاب کنید 👇",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
    # دریافت عکس از ادمین و ذخیره در پکیج
async def save_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.message.from_user.id != ADMIN_ID:
        return

    photo = update.message.photo[-1]

    caption = update.message.caption

    if not caption:
        caption = "بدون متن"


    file = await context.bot.get_file(photo.file_id)


    filename = f"package_{len(PACKAGE)+1}.jpg"


    await file.download_to_drive(filename)


    PACKAGE.append(
        (
            filename,
            caption
        )
    )


    await update.message.reply_text(
        f"✅ عکس ذخیره شد\n"
        f"تعداد پکیج: {len(PACKAGE)}"
    )





# ارسال پکیج به یک کاربر خاص
async def send_package(chat_id, context):

    if len(PACKAGE) == 0:

        await context.bot.send_message(
            chat_id=chat_id,
            text="❌ هنوز پکیجی ساخته نشده."
        )

        return


    for img, text in PACKAGE:

        try:

            await context.bot.send_photo(
                chat_id=chat_id,
                photo=open(img, "rb"),
                caption=text
            )

        except Exception as e:

            print(e)





# دستور ارسال توسط ادمین
async def send_command(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.message.from_user.id != ADMIN_ID:
        return


    if len(context.args) == 0:

        await update.message.reply_text(
            "مثال:\n/send username"
        )

        return



    username = context.args[0].replace("@", "")



    if username not in USERS:

        await update.message.reply_text(
            "❌ این کاربر هنوز ربات را استارت نکرده."
        )

        return



    user_id = USERS[username]



    await update.message.reply_text(
        "📦 ارسال شروع شد..."
    )


    await send_package(
        user_id,
        context
    )


    await update.message.reply_text(
        "✅ ارسال تمام شد."
    )





# دکمه ها
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()


    if query.data == "support":

        await query.edit_message_text(
            f"📞 پشتیبانی:\n@{SUPPORT_ID}"
        )


    elif query.data == "package":

        await query.edit_message_text(
            "📦 پکیج آماده خرید است."
        )
        # ساخت ربات
bot = ApplicationBuilder().token(TOKEN).build()


# دستورات
bot.add_handler(
    CommandHandler(
        "start",
        start
    )
)


bot.add_handler(
    CommandHandler(
        "send",
        send_command
    )
)


# دریافت عکس فقط برای ادمین
bot.add_handler(
    MessageHandler(
        filters.PHOTO,
        save_photo
    )
)


# دکمه ها
bot.add_handler(
    CallbackQueryHandler(
        button
    )
)



print("ربات روشن شد 🚀")


bot.run_polling()
