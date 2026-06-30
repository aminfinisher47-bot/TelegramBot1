import os
from dotenv import load_dotenv
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID"))

# منوی اصلی
main_menu = [
    ["🛒 خرید محصول جدید", "📦 سفارش‌های من"],
    ["📞 پشتیبانی", "📢 کانال‌های ما"]
]

products_menu = [
    ["890", "990", "110"],
    ["870", "650", "115"],
    ["417", "🔙 برگشت"]
]

models_menu = [
    ["مدل 1", "مدل 2", "مدل 3"],
    ["مدل 4", "مدل 5", "مدل 6"],
    ["مدل 7", "🔙 برگشت"]
]

pay_menu = [["💳 کارت به کارت", "🔙 برگشت"]]


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "به فروشگاه Tri_Art_studio خوش آمدید 🌿",
        reply_markup=ReplyKeyboardMarkup(main_menu, resize_keyboard=True)
    )


async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    user = update.message.from_user

    if text == "🛒 خرید محصول جدید":
        await update.message.reply_text(
            "کد محصول را انتخاب کنید:",
            reply_markup=ReplyKeyboardMarkup(products_menu, resize_keyboard=True)
        )

    elif text == "📦 سفارش‌های من":
        await update.message.reply_text("سفارشی ثبت نشده.", reply_markup=ReplyKeyboardMarkup(main_menu, resize_keyboard=True))

    elif text == "📞 پشتیبانی":
        await update.message.reply_text("برای پشتیبانی پیام دهید.", reply_markup=ReplyKeyboardMarkup(main_menu, resize_keyboard=True))

    elif text == "📢 کانال‌های ما":
        await update.message.reply_text("در حال تکمیل...", reply_markup=ReplyKeyboardMarkup(main_menu, resize_keyboard=True))

    elif text == "🔙 برگشت":
        await update.message.reply_text(
            "بازگشت به منو اصلی",
            reply_markup=ReplyKeyboardMarkup(main_menu, resize_keyboard=True)
        )

    elif text == "890":
        await update.message.reply_text(
            "مدل را انتخاب کنید:",
            reply_markup=ReplyKeyboardMarkup(models_menu, resize_keyboard=True)
        )

    elif text in ["990", "110", "870", "650", "115", "417"]:
        await update.message.reply_text(
            "این محصول فعلاً غیرفعال است.",
            reply_markup=ReplyKeyboardMarkup(main_menu, resize_keyboard=True)
        )

    elif text.startswith("مدل"):
        await update.message.reply_text(
            "قیمت نهایی:\n890,000 ریال (89,000 تومان)\n\nروش پرداخت:",
            reply_markup=ReplyKeyboardMarkup(pay_menu, resize_keyboard=True)
        )

    elif text == "💳 کارت به کارت":
        await update.message.reply_text(
            "💳 شماره کارت:\n6037997406047093\n\n💰 مبلغ: 890,000 ریال\n\nفیش پرداخت را ارسال کنید."
        )

        await context.bot.send_message(
            chat_id=ADMIN_ID,
            text=f"🧾 کاربر جدید پرداخت را شروع کرد:\nID: {user.id}\nUsername: @{user.username}"
        )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()