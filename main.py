from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from customFilter import FilterAwesome

filter_awesome = FilterAwesome()

#objeto principal e dispatcher
updater = Updater(token= '1663266180:AAF5igg_d5IOgrMS8wi1wgAYxe9QFea_E7k', use_context=True)
dispatcher = updater.dispatcher

#log
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

#func callback start
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Olá tudo bem?")

#func callback echo
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

#func callback caps
def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

#func callback #bot
def bot(update, context):
    context.bot.send_message(chat_id=-1001417903590, text=update.message.text)
    
#funções do bot
bot_handler = MessageHandler(filter_awesome, bot)
dispatcher.add_handler(bot_handler)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler) 

caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)

updater.start_polling()











