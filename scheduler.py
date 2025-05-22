from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update
import os

TOKEN = os.getenv("TELEGRAM_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Benvenuto nel bot di trading crypto scalping!")

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = database.get_account_summary()
    await update.message.reply_text(f"💼 Stato conto demo:\n{data}")

async def run_bot():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))

    await app.initialize()
    await app.start()
    print("Bot avviato e in esecuzione.")

    try:
        await asyncio.Future()  # rimane in esecuzione indefinitamente
    finally:
        await app.stop()
        await app.shutdown()
