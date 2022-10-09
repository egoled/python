from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext


async def hi_command (update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(f'Hi {update.effective_user.first_name}')