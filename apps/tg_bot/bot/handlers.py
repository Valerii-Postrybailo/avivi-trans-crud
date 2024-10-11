from django.utils.translation import gettext as _
from django.utils import translation

from telegram import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

from apps.store.models import Product

PRODUCTS_PER_PAGE = 5


def start(update, context):
    update.message.reply_text('Hello there!')
    keyboard = [['🇺🇦 Українська', '🇺🇸 English']]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)
    update.message.reply_text('Choose your language:', reply_markup=reply_markup)


def show_menu(update, context):
    keyboard = [[_("catalog btn")]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, )
    update.message.reply_text(_('greeting and menu'), reply_markup=reply_markup)


def show_catalog(update, context):
    pagination_buttons = []
    keyboard = []

    products = Product.objects.filter(is_active=True)
    page = int(context.user_data.get('page', 0))
    total_pages = (len(products) - 1) // PRODUCTS_PER_PAGE + 1

    start_index = page * PRODUCTS_PER_PAGE
    end_index = start_index + PRODUCTS_PER_PAGE
    current_products = products[start_index:end_index]

    for product in current_products:
        button = InlineKeyboardButton(product.name, callback_data=f'product_{product.id}')
        keyboard.append([button])

    if page > 0:
        pagination_buttons.append(InlineKeyboardButton(_("{} back_arrow_btn").format("⬅️"), callback_data=f'catalog_page_{page - 1}'))
    if page < total_pages - 1:
        pagination_buttons.append(InlineKeyboardButton(_("next_arrow_btn {}").format("➡️"), callback_data=f'catalog_page_{page + 1}'))

    keyboard.append(pagination_buttons)
    keyboard.append([InlineKeyboardButton(_("page {} of {}").format(page + 1, total_pages), callback_data='none')])

    reply_markup = InlineKeyboardMarkup(keyboard)
    query = update.callback_query

    if query:
        query.answer()
        if update.callback_query.data == "back_to_catalog":
            context.bot.send_message(chat_id=query.message.chat_id, text=_("here is our catalog"),
                                     reply_markup=reply_markup)
        else:
            query.edit_message_text(_("here is our catalog"), reply_markup=reply_markup)
    else:
        update.message.reply_text(_("here is our catalog"), reply_markup=reply_markup)


def product_detail(update, context, settings):
    query = update.callback_query
    query.answer()

    product_id = query.data.split('_')[1]

    back_button = InlineKeyboardButton(_("back_btn"), callback_data='back_to_catalog')
    keyboard = [[back_button]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    try:
        product = Product.objects.get(id=product_id)
        product_photo = product.image.url
        context.bot.send_photo(
            chat_id=query.message.chat_id,
            photo=f'{settings.webhook_url}{product_photo}',
            caption=_("Name: {}\n"
                      "Description: {}\n"
                      "Price: {}\n"
                      "Stock Quantity: {}\n"
                      ).format(product.name,
                               product.description,
                               product.price,
                               product.stock_quantity),
            reply_markup=reply_markup
        )

    except Product.DoesNotExist:
        query.edit_message_text(_("Product not found."))


def handle_menu_selection(update, context):
    selected_option = update.message.text

    if selected_option == '🇺🇸 English':
        context.user_data['language'] = 'en'
        translation.activate('en')
        update.message.reply_text(_('language selected'))
        show_menu(update, context)

    elif selected_option == '🇺🇦 Українська':
        context.user_data['language'] = 'uk'
        translation.activate('uk')
        update.message.reply_text(_('language selected'))
        show_menu(update, context)

    if selected_option == _("catalog btn"):
        show_catalog(update, context)


def handle_callback_query(update, context):
    query = update.callback_query
    query.answer()

    if query.data == 'back_to_catalog':
        show_catalog(update, context)

    elif query.data.startswith('catalog_page_'):
        new_page = int(query.data.split('_')[-1])
        context.user_data['page'] = new_page
        show_catalog(update, context)
