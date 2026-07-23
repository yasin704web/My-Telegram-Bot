import os

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


TOKEN = os.getenv("TOKEN")

# ساخت سنس خودکار برای هر گوشی
def generate_sens(model):
    base = abs(hash(model)) % 20 + 80
    return f"🎯 {base} / {base-5} / {base-10} / {base-15}"

# دستور استارت
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        model = " ".join(context.args)

        sens = generate_sens(model)

        await update.message.reply_text(
f"""🔥 مدل: {model}

{sense}

💰 قیمت: 10,000 تومان
💳 کارت:
5022-2915-1837-1222

📸 بعد پرداخت:
@FF_Ranked0011
"""
        )
    else:
        await update.message.reply_text("📱 لطفاً مدل گوشی رو از سایت انتخاب کن")

# اجرای ربات
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("🤖 Bot is running...")
app.run_polling()
