from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackContext
import datetime


async def hi_command (update: Update, context: CallbackContext):
    update.message.reply_text(f'Hi {update.effective_user.first_name}')

async def help_command (update: Update, context: CallbackContext):
    update.message.reply_text(f'/Hi \n/time\n/help')

async def time_command (update: Update, context: CallbackContext):
    update.message.reply_text(f'{datetime.datetime.now().time()}')

async def time_command (update: Update, context: CallbackContext):
    update.message.reply_text(f'{datetime.datetime.now().time()}')