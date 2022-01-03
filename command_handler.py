from telegram.ext import CommandHandler, MessageHandler, Filters, CallbackQueryHandler

from buttons_commands import buttons
from user_commands import *


def command_handler(dispatcher):
    # Buttons
    dispatcher.add_handler(CallbackQueryHandler(buttons))

    # User commands
    dispatcher.add_handler(CommandHandler("start", start))

    dispatcher.add_handler(CommandHandler("help", help))
    dispatcher.add_handler(MessageHandler(Filters.regex("Помощь"), help))

    dispatcher.add_handler(CommandHandler("ask", ask_question))
    dispatcher.add_handler(MessageHandler(Filters.regex("Задать вопрос"), ask_question))

    # Admin commands

    # Utils
    dispatcher.add_handler(MessageHandler(Filters.text, all_messages))