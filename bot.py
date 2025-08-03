import os
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("–Ø —Ö—Ä–∞–Ω–∏—Ç–µ–ª—å –ó–∞–ª–≥–æ. –Ø –ø—Ä–æ—Å–Ω—É–ª—Å—è.")

def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == '__main__':
    main()ê•¶®¨ ¢Î¢Æ§† ™Æ¨†≠§ ≠† Ì™‡†≠ (ECHO) ¢™´ÓÁ•≠.
