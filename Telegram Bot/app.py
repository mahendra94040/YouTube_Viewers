from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, CallbackContext
from telegram.update import Update
from telegram.bot import Bot

def start(update: Update, context: CallbackContext):
	update.message.reply_text("Send msg to user what do u want....")

def video(update: Update, context: CallbackContext):
	context.bot.send_message(chat_id=update.effective_chat.id, text="nice video bro ...")


def messagebot(update: Update, context: CallbackContext):
	context.bot.send_message(chat_id=update.effective_chat.id, text="Have a nice day bro ...")


if __name__ == '__main__':
	Bot_Token="token from telegram bot-father"
	bot=Bot(Bot_Token)

	updater=Updater(Bot_Token, use_context=True)

	updater.dispatcher.add_handler(CommandHandler('start', start))
	updater.dispatcher.add_handler(MessageHandler(Filters.video, video))
	updater.dispatcher.add_handler(MessageHandler(Filters.text, messagebot))
	updater.start_polling()
	updater.idle()