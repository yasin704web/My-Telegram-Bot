import os
import telebot
from telebot import types

# گرفتن توکن از Render (محیط)
TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

# استارت
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🎮 سنس فری فایر", "🌐 سایت")

    bot.send_message(message.chat.id, "سلام 👋 یکی رو انتخاب کن:", reply_markup=markup)

# سنس
@bot.message_handler(func=lambda m: m.text == "🎮 سنس فری فایر")
def sens(message):
    bot.send_message(message.chat.id, """
🎮 پکیج سنس فری فایر

💰 قیمت: 15,000 تومان

💳 شماره کارت:
5022-2915-1837-1222

📌 مراحل خرید:
1. واریز مبلغ
2. ارسال مدل گوشی
3. ارسال فیش
4. دریافت سنس بعد تایید
""")

# منوی سایت
@bot.message_handler(func=lambda m: m.text == "🌐 سایت")
def site_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("🛒 فروشگاهی و تجاری")
    markup.add("🧰 خدماتی")
    markup.add("🏢 معرفی و شرکتی")
    markup.add("⚡ تخصصی‌تر")
    markup.add("🔙 بازگشت")

    bot.send_message(message.chat.id, "نوع سایت:", reply_markup=markup)

# فروشگاهی
@bot.message_handler(func=lambda m: m.text == "🛒 فروشگاهی و تجاری")
def shop(message):
    bot.send_message(message.chat.id, """
🛒 انواع سایت فروشگاهی:

• سایت فروشگاهی (عمومی)
• سایت طلافروشی
• سایت پوشاک و مد
• سایت لوازم آرایشی
• سایت دیجیتال و موبایل
• سایت مبلمان
• سایت کتاب‌فروشی
• سایت لوازم خانگی
• سایت سوپرمارکت آنلاین
• سایت گل‌فروشی
""")

# خدماتی
@bot.message_handler(func=lambda m: m.text == "🧰 خدماتی")
def service(message):
    bot.send_message(message.chat.id, """
🧰 سایت‌های خدماتی:

• رزرو هتل
• رزرو بلیط
• خدمات پزشکی
• سایت آموزشی
• رستوران و غذا
• خدمات حقوقی
• آژانس مسافرتی
• آرایشگاه
""")

# شرکتی
@bot.message_handler(func=lambda m: m.text == "🏢 معرفی و شرکتی")
def company(message):
    bot.send_message(message.chat.id, """
🏢 سایت‌های معرفی:

• سایت شرکتی
• پورتفولیو
• سایت خبری
• وبلاگ
• رزومه آنلاین
• NGO
""")

# تخصصی
@bot.message_handler(func=lambda m: m.text == "⚡ تخصصی‌تر")
def pro(message):
    bot.send_message(message.chat.id, """
⚡ سایت‌های تخصصی:

• املاک
• خودرو
• بازی
• موسیقی
• ورزشی
""")

# بازگشت
@bot.message_handler(func=lambda m: m.text == "🔙 بازگشت")
def back(message):
    start(message)

bot.infinity_polling()
