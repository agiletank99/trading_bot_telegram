from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import database

import os
TOKEN = os.getenv("7511093606:AAEyFndoQZa5u5XSQUX5kh6hKIwxxA6K_6g")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Benvenuto nel bot di trading crypto scalping!")

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = database.get_account_summary()
    await update.message.reply_text(f"💼 Stato conto demo:\n{data}")

def run_bot():
    app = ApplicationBuilder().token('7511093606:AAEyFndoQZa5u5XSQUX5kh6hKIwxxA6K_6g').build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))
    app.run_polling()
