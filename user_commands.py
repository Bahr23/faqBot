import telegram
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from menu import get_menu, build_menu
from models import *
from core import *
from queuesystem import stop_queue, queue, current_queue


@db_session
def start(update, context):
    stop_queue(context)
    user = get_user_or_error(id=update.message.from_user.id)
    if user:

        text = f"{user.name}, привет!"
    else:
        if update.message.from_user.username:
            username = update.message.from_user.username
        else:
            username = 'none'
        user = User(
            user_id=update.message.from_user.id,
            status='user',
            name=update.message.from_user.first_name,
            username=username
        )
        text = f"{user.name}, вы успешно зарегистрировались!"
    menu = get_menu("main")
    context.bot.send_message(chat_id=update.effective_chat.id, text=text, reply_markup=get_menu('main'))


def help(update, context):
    user = get_user_or_error(id=update.message.from_user.id)
    if user:
        if 'queue' in context.user_data.keys():
            if context.user_data['queue']:
                queue(update, context, user, )
                return
        context.user_data.update({'last_message': update.message.text})

        text = "Текст помощи."
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=text,
            parse_mode=telegram.ParseMode.HTML,
            reply_markup=get_menu('main')
        )
    else:
        start(update, context)


def all_messages(update, context):
    user = get_user_or_error(id=update.message.from_user.id)
    if user:
        if 'queue' in context.user_data.keys():
            if context.user_data['queue']:
                queue(update, context, user, )
                return
        context.user_data.update({'last_message': update.message.text})

        text = f"{user.name}, чем могу вам помочь? Нажмите кнопку <i>'Помощь'</i>" \
            f" или используйте команду <code>/help</code>, чтобы узнать мои возможности."
        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=text,
            parse_mode=telegram.ParseMode.HTML,
            reply_markup=get_menu('main')
        )
    else:
        start(update, context)


def ask_question(update, context):
    user = get_user_or_error(id=update.message.from_user.id)
    if user:
        if 'queue' in context.user_data.keys():
            if context.user_data['queue']:
                queue(update, context, user, )
                return
        queue_list = [
            {'question_text': 'Напишите ваш вопрос:'}
        ]

        context.user_data.update({
            'queue': True,
            'queue_name': 'ask_question',
            'queue_finish': 'Выберите наиболее подходящий вопрос 👆',
            'queue_list': queue_list,
            'queue_position': 0,
            'queue_answers': [],
            'queue_docs': '',
            'last_queue_message': ''})

        current_queue(update, context, user)

    else:
        start(update, context)