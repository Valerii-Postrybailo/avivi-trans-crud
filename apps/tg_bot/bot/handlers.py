from django.utils.translation import gettext as _
from django.utils import translation

from telegram import ReplyKeyboardMarkup

def start(update, context):
    update.message.reply_text('Hello there!')
    keyboard = [['🇺🇦 Українська', '🇺🇸 English']]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)

    update.message.reply_text('Choose your language:', reply_markup=reply_markup)


def handle_language_selection(update, context):
    selected_language = update.message.text

    if selected_language == '🇺🇦 Українська':
        context.user_data['language'] = 'uk'
        translation.activate('uk')
        update.message.reply_text(_('Language selected'))
    elif selected_language == '🇺🇸 English':
        context.user_data['language'] = 'en'
        translation.activate('en')
        update.message.reply_text(_('Language selected'))
