from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler

async def myaccounts(update: Update, context):
    await update.message.reply_text(
        "حساباتي:\n"
        "🏦 حساب 1: XXXX\n"
        "💳 حساب 2: XXXX"
    )

async def payment(update: Update, context):
    await update.message.reply_text(
        "طرق الدفع:\n"
        "💰 طريقة 1\n"
        "💰 طريقة 2"
    )

async def samples(update: Update, context):
    await update.message.reply_text("العينات: ...")

app = ApplicationBuilder().token("ضع_توكن_البوت_هنا").build()
app.add_handler(CommandHandler("myaccounts", myaccounts))
app.add_handler(CommandHandler("payment", payment))
app.add_handler(CommandHandler("samples", samples))
app.run_polling()
