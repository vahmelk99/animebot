#!/usr/bin/python3
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.
#pipenv run python bot.py
"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

class MyBot:
    def __init__(self):
        """Start the bot."""
        # Create the Updater and pass it your bot's token.
        # Make sure to set use_context=True to use the new context based callbacks
        # Post version 12 this will no longer be necessary
        self.updater = Updater("1697050455:AAFPZUllWEhDJ4ZsjEkBACOYF6ebcUV-au0", use_context=True)

        # Get the dispatcher to register handlers
        self.dp = self.updater.dispatcher

        # on different commands - answer in Telegram
        self.dp.add_handler(CommandHandler("start", self.start))
        self.dp.add_handler(CommandHandler("help", self.help))

        # on noncommand i.e message - echo the message on Telegram
        self.dp.add_handler(MessageHandler(Filters.text, self.echo))

        # log all errors
        self.dp.add_error_handler(self.error)

        # Start the Bot
        self.updater.start_polling()

        # Run the bot until you press Ctrl-C or the process receives SIGINT,
        # SIGTERM or SIGABRT. This should be used most of the time, since
        # start_polling() is non-blocking and will stop the bot gracefully.
        self.updater.idle()
    # Define a few command handlers. These usually take the two arguments update and
    # context. Error handlers also receive the raised TelegramError object in error.
    def start(self, update, context):
        """Send a message when the command /start is issued."""
        update.message.reply_text('Incha ile Xcho?')


    def help(self, update, context):
        """Send a message when the command /help is issued."""
        update.message.reply_text('This bot is for protecting you from Xcho!')

    def echo(self, update, context):
        """Echo the user message."""
        mess = update.message.text
        print(update.message)
        if update.message.from_user.first_name.lower() == 'khach':
            update.message.delete()
            self.updater.bot.send_message(update.message.chat_id, 'Hajox Xcho')
        # elif update.message.from_user.first_name.lower() == 'gor':
        #     update.message.reply_text('Ktruk sharjumner mi ara')
        if 'xcho' in mess.lower() or 'xch' in mess.lower() or 'խչ' in mess.lower() or 'խչո' in mess.lower():
            update.message.reply_text('Xchon Merienc tanna')
        if 'babken' in mess.lower():
            update.message.reply_text('Babken@ mer @ngerna')

    def error(self, update, context):
        """Log Errors caused by Updates."""
        logger.warning('Xcho won. Update "%s" caused error "%s"', update, context.error)

if __name__ == '__main__':
    MyBot()