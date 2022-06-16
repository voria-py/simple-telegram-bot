'''
simple python telegram bot
by amirkho.ir

'''

#import logging

from telegram import Bot
from telegram.ext import *
from os import system
system('clear')



API_KEY = '5454640691:AAGLuQcY9jqktLdtl2VDkFOjj0Ue6UzdpnQ'


# set up logging
# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
# logging.info('Starting bot...')


def start_command(bot,context):
    bot.message.reply_text('Hello there! I\'m a bot. What\'s up? ')

def help_command(update , context):
    update.message.reply_text('try to type anything and I will do my best response!')

def custom_command(update , context):
    update.message.reply_text('this is a custom command!')

def handle_message(update , context):
    text = str(update.message.text).lower()
#    logging.info(f'User ({update.message.chat.id}) says: {text} ')

    # Bot response
    for x in text:
        update.message.reply_text(x)


#def error(update , context):
    #   Log errors
    #logging.error(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    updater = Updater(API_KEY,use_context = True)
    dp = updater.dispatcher


    #   Commands
    dp.add_handler(CommandHandler('start' , start_command))
    dp.add_handler(CommandHandler('help' , help_command))
    dp.add_handler(CommandHandler('custom' , custom_command))



    #   Messages
    dp.add_handler(MessageHandler(Filters.text,handle_message))


    # Log all errors
    #dp.add_error_handler(error)

    # Run the bot
    updater.start_polling(1.0)
    updater.idle()


