#!/usr/bin/python3
#pipenv run python bot.py
import logging
import os
from getVideo import getVideo, download_video_series
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)
class MyBot:
    def __init__(self):
        """Start the bot."""
        self.updater = Updater("1634518644:AAGm2xoTP44QWmzDGypXIiEOHeRZ7CnH1js", use_context=True)
        self.dp = self.updater.dispatcher
        self.dp.add_handler(CommandHandler("start", self.start))
        self.dp.add_handler(CommandHandler("help", self.help))
        self.dp.add_handler(MessageHandler(Filters.text, self.download))
        self.dp.add_handler(MessageHandler(Filters.video, self.getter))
        self.dp.add_error_handler(self.error)
        self.updater.start_polling()
        self.updater.idle()
    def start(self, update, context):
        """Send a message when the command /start is issued."""
        update.message.reply_text('Please send me a link of anime that you want to download from https://jut.su/')
    def help(self, update, context):
        """Send a message when the command /help is issued."""
        update.message.reply_text('This bot is for downloading animes from https://jut.su/ website.')
    def getter(self, update, context):
        chat_id = update.message.chat_id
        caption = update.message.caption
        if(int(chat_id) == 1734553643): #Must change
            chat_to_send = None
            with open("./queue.txt", "r") as f:
                lines = f.readlines()
                with open("./queue.txt", "w") as f:
                    for line in lines:
                        print(line.split())
                        if line.split()[1] == caption:
                            chat_to_send = line.split()[0]
                        else:
                            f.write(line)     
            f.close()
            if chat_to_send:
                print(chat_to_send)
                self.updater.bot.forward_message(chat_id=chat_to_send, 
                    from_chat_id=chat_id, 
                    message_id=update.message.message_id
                )
    def download(self, update, context):
        chat_id = update.message.chat_id
        print(chat_id)
        if(int(chat_id) == 1734553643): return #Must change
        else:
            self.updater.bot.send_message(update.message.chat_id, 'Please wait...')
            mess = update.message.text
            video = getVideo(mess)
            file_path = download_video_series(video)
            f = open('./queue.txt', 'a')
            print('added' + str(chat_id))
            f.write(str(chat_id) + ' ' + file_path + '\n')
            f.close()
            os.system("./message.py " + file_path)
    def error(self, update, context):
        """Log Errors caused by Updates."""
        logger.warning('Error while downloading. Update "%s" caused error "%s"', update, context.error)
if __name__ == '__main__':
    MyBot()