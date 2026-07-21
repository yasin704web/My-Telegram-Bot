import os
import threading

from flask import Flask
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup

from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
    MessageHandler,
    filters
)

TOKEN = os.getenv("TOKEN")

TRUST_CHANNEL = "https://t.me/+blrD4zwmKgwzNmE0"
SUPPORT = "https://t.me/FF_Ranked0011"

CARD_NUMBER = "5022-2915-1837-1222"
PRICE = "199000 تومان"

# Flask برای Render
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

# ================== ربات ==================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [InlineKeyboardButton("🤖 پکیج ربات", callback_data="robot_pack")],
        [InlineKeyboardButton("⭐ چنل اعتماد", url=TRUST_CHANNEL)],
        [InlineKeyboardButton("📞 پشتیبانی", url=SUPPORT)]
    ]

    await update.message.reply_text(
        "🔥 به فروشگاه فایل حرفه‌ای خوش آمدید\n\n"
        "✅ محصولات کاربردی\n"
        "✅ فایل‌های آموزشی\n"
        "✅ پشتیبانی\n\n"
        "انتخاب کنید 👇",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query
    await query.answer()

    if query.data == "robot_pack":

        keyboard = [
            [InlineKeyboardButton("💳 خرید پکیج", callback_data="payment")],
            [InlineKeyboardButton("📞 پشتیبانی", url=SUPPORT)]
        ]

        await query.edit_message_text(
            "🤖 پکیج ربات تلگرام\n\n"
            "🔥 شامل فایل‌ها و آموزش‌های کاربردی\n\n"
            f"💰 قیمت: {PRICE}\n\n"
            "برای خرید روی گزینه زیر بزنید 👇",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    elif query.data == "payment":

        await query.edit_message_text(
            "💳 اطلاعات پرداخت\n\n"
            f"💰 مبلغ:\n{PRICE}\n\n"
            f"🏦 شماره کارت:\n{CARD_NUMBER}\n\n"
            "بعد از واریز، لطفاً عکس رسید را برای پشتیبانی ارسال کنید.\n\n"
            "📞 پشتیبانی:\n@FF_Ranked0011"
        )

# ================== ارسال عکس به یوزرنیم ==================

async def forward_to_user(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if update.message.photo and update.message.caption:

        username = update.message.caption.strip()

        if username.startswith("@"):

            try:
                photo = update.message.photo[-1].file_id

                await context.bot.send_photo(
                    chat_id=username,
                    photo=photo,
                    caption="📦 پکیج شما آماده است ✅"
                )

                await update.message.reply_text("✅ ارسال شد")

            except:
                await update.message.reply_text("❌ خطا (کاربر استارت نکرده یا یوزرنیم اشتباهه)")

# ================== اجرای ربات ==================

bot = ApplicationBuilder().token(TOKEN).build()

bot.add_handler(CommandHandler("start", start))
bot.add_handler(CallbackQueryHandler(button))
bot.add_handler(MessageHandler(filters.PHOTO, forward_to_user))

print("ربات فروش فایل روشن شد 🚀")

bot.run_polling()
