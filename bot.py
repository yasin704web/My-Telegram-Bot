import os

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
    MessageHandler,
    filters
)


TOKEN = os.getenv("TOKEN")

ADMIN_ID = 6847301983

CARD_NUMBER = "5022-2915-1837-1222"

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
            "📞 پشتیبانی:\n@FF_Ranked0011"
        )


    elif query.data == "file":

        keyboard = [
            [
                InlineKeyboardButton(
                    "🛒 خرید فایل",
                    callback_data="buy"
                )
            ]
        ]

        await query.edit_message_text(
            f"📂 محصول:\n\n"
            f"🤖 {FILE_NAME}\n"
            f"💰 قیمت: {PRICE}\n\n"
            "برای خرید کلیک کنید 👇",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


    elif query.data == "buy":

        context.user_data["buying"] = True

        await query.edit_message_text(
            "💳 مبلغ را به کارت زیر واریز کنید:\n\n"
            f"{CARD_NUMBER}\n\n"
            " بعد از پرداخت، عکس رسید را به پشتیبانی ارسال کنید و پس از تایید پکیج‌را تحویل بگیرید."
        )


    elif query.data.startswith("approve"):

        user_id = int(query.data.split("_")[1])

        await context.bot.send_message(
            chat_id=user_id,
            text="✅ پرداخت شما تایید شد."
        )

        await query.edit_message_caption(
            caption="✅ خرید تایید شد."
        )


    elif query.data.startswith("reject"):

        user_id = int(query.data.split("_")[1])

        await context.bot.send_message(
            chat_id=user_id,
            text="❌ پرداخت شما رد شد."
        )

        await query.edit_message_caption(
            caption="❌ خرید رد شد."
        )


async def receipt(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if context.user_data.get("buying"):

        user = update.message.from_user

        keyboard = [
            [
                InlineKeyboardButton(
                    "✅ تایید خرید",
                    callback_data=f"approve_{user.id}"
                ),
                InlineKeyboardButton(
                    "❌ رد خرید",
                    callback_data=f"reject_{user.id}"
                )
            ]
        ]


        await context.bot.send_photo(
            chat_id=ADMIN_ID,
            photo=update.message.photo[-1].file_id,
            caption=(
                "📥 رسید جدید\n\n"
                f"👤 کاربر: {user.first_name}\n"
                f"🆔 ID: {user.id}\n"
                f"📂 محصول: {FILE_NAME}\n"
                f"💰 مبلغ: {PRICE}"
            ),
            reply_markup=InlineKeyboardMarkup(keyboard)
        )


        await update.message.reply_text(
            "✅ رسید شما ارسال شد.\n"
            "بعد از بررسی اطلاع داده می‌شود."
        )


def main():

    app = Application.builder().token(TOKEN).build()

    app.add_handler(
        CommandHandler("start", start)
    )

    app.add_handler(
        CallbackQueryHandler(buttons)
    )

    app.add_handler(
        MessageHandler(filters.PHOTO, receipt)
    )

    print("Smartix Running ✅")

    app.run_polling()


if __name__ == "__main__":
    main()
