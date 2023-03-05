from telebot import types


def start_inline_keyboard():
    start_inline_keyboard = types.InlineKeyboardMarkup(row_width=1)
    inline_button_1 = types.InlineKeyboardButton(
        text='Скачать видео', callback_data='download_video')
    start_inline_keyboard.add(inline_button_1)
    return start_inline_keyboard


def go_back_keyboard():
    go_back_keyboard = types.InlineKeyboardMarkup(row_width=1)
    inline_button_1 = types.InlineKeyboardButton(text='Назад',
                                                 callback_data='back')
    go_back_keyboard.add(inline_button_1)
    return go_back_keyboard
