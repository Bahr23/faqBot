import telegram

from core import get_user_or_error, get_question
from menu import get_menu
from queuesystem import queue
from models import *


def buttons(update, context):
    query = update.callback_query
    user = get_user_or_error(update.callback_query.from_user.id)
    data = query.data.split('@')[1:]
    if user:
        if 'queue' in context.user_data.keys():
            if context.user_data['queue']:
                if context.user_data['queue_name'] == "create_order":
                    pass

        if data[0] == 'help':
            print(data)

        if data[0] == 'get_question':
            print(data)
            text = get_question(int(data[1]))
            if text:
                context.bot.send_message(
                    chat_id=update.effective_chat.id,
                    text=text,
                    parse_mode=telegram.ParseMode.HTML,
                )