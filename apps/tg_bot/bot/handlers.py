from telegram import ReplyKeyboardMarkup


def start(update, context):
    update.message.reply_text('Hello there!')
    keyboard = [['🇺🇦 Українська', '🇺🇸 English']]
    reply_markup = ReplyKeyboardMarkup(keyboard,resize_keyboard=True, one_time_keyboard=True)

    update.message.reply_text('Виберіть мову:', reply_markup=reply_markup)


def handle_language_selection(update, context):
    selected_language = update.message.text

    if selected_language == '🇺🇦 Українська':
        context.user_data['language'] = 'ukrainian'
        update.message.reply_text('Ви вибрали українську мову!')
    elif selected_language == '🇺🇸 English':
        context.user_data['language'] = 'english'
        update.message.reply_text('You selected English!')
