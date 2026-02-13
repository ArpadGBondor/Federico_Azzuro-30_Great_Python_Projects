from credentials import TELEGRAM_BOT_TOKEN, TELEGRAM_BOT_USERNAME
from chat import chat_bot
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
)


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello there! Nice to meet you. Let's chat!")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Just type something, and I will respond to you!")


async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("This is a custom command.")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type = update.message.chat.type
    text: str = update.message.text

    # Log
    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    # Handle message type
    if message_type == "group":
        if TELEGRAM_BOT_USERNAME in text:
            new_text: str = text.replace(TELEGRAM_BOT_USERNAME, "").strip()
            response: str = chat_bot(new_text)
        else:
            return
    else:
        response: str = chat_bot(text)

    # Reply
    print(f'Bot: "{response}"')
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update "{update}" caused error: "{context.error}"')


def main():
    print("Starting up bot...")
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Commands
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("custom", custom_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    print("Polling...")
    app.run_polling(poll_interval=5)


if __name__ == "__main__":
    main()
