from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8467516257:AAGKMdwn7bh3Js1Nk_2DM4YKzFjOBFd85O4"

WHATSAPP_LINK = "https://wa.me/919057617196"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [InlineKeyboardButton("💬 Chat on WhatsApp", url=WHATSAPP_LINK)]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "📲 Chat on WhatsApp Now\n\n"
        "Click the button below to connect with us directly on WhatsApp.",
        reply_markup=reply_markup
    )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
