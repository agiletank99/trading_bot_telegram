import os
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import database

# Prendere il token dalla variabile ambiente corretta, es. TELEGRAM_TOKEN
TOKEN = os.getenv("TELEGRAM_TOKEN")

if not TOKEN:
    raise Exception("❌ Variabile d'ambiente 'TELEGRAM_TOKEN' non trovata!")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Benvenuto nel bot di trading crypto scalping!")

async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = database.get_account_summary()
    await update.message.reply_text(f"💼 Stato conto demo:\n{data}")

async def run_bot():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))

    # Inizializza e avvia manualmente il bot
    await app.initialize()
    await app.start()
    print("Bot avviato e in esecuzione.")

    try:
        # Mantieni il bot in esecuzione indefinitamente
        await asyncio.Future()
    finally:
        # Chiudi correttamente il bot
        await app.stop()
        await app.shutdown()

if __name__ == "__main__":
    asyncio.run(run_bot())
