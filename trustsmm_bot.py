import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler

logging.basicConfig(level=logging.INFO)

# /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    keyboard = [
        [InlineKeyboardButton("Instagram Services", callback_data='instagram')],
        [InlineKeyboardButton("YouTube Services", callback_data='youtube')],
        [InlineKeyboardButton("Spotify Services", callback_data='spotify')],
        [InlineKeyboardButton("Telegram Services", callback_data='telegram')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Welcome to TrustSMM!\nChoose a service below:", reply_markup=reply_markup)

# Callback for buttons
async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    choice = query.data
    await query.edit_message_text(text=f"You selected: {choice.capitalize()} Services 🚀")

# Main function
async def main():
    import os
    TOKEN = os.getenv("BOT_TOKEN")  # Add BOT_TOKEN in Render Environment Variables

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_callback))

    await app.run_polling()

# Run the bot
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
