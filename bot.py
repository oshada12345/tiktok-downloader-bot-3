import os
import config
import telebot
from keyboard import start_inline_keyboard, go_back_keyboard
from tiktok_downloader import snaptik


bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def start_command(message):
    text = ('Привет, с помощью этого бота ты можешь'
            ' скачать видео из тикток без водяного знака!')
    bot.send_message(chat_id=message.chat.id,
                     text=text,
                     reply_markup=start_inline_keyboard())


@bot.callback_query_handler(func=lambda call: True)
def answer(call):

    chat_id = call.message.chat.id
    message_id = call.message.message_id

    if call.data == 'download_video':
        bot.delete_message(message_id=message_id, chat_id=chat_id)
        text = 'Отправьте ссылку на видео ТикТок'
        message = bot.send_message(chat_id=chat_id,
                                   text=text,
                                   reply_markup=go_back_keyboard())
        bot.register_next_step_handler(message, download_video)

    elif call.data == 'back':
        bot.delete_message(message_id=message_id, chat_id=chat_id)
        text = ('Привет, с помощью этого бота ты можешь'
                ' скачать видео из тикток без водяного знака!')
        bot.send_message(chat_id=chat_id,
                         text=text,
                         reply_markup=start_inline_keyboard())


def download_video(message):
    try:
        ID = str(message.chat.id)
        text = 'Начинаю скачивание, в среднем оно занимает до 3х минут.'
        caption = ('Спасибо за использование нашего бота!'
                   ' Скачать еще одно видео?')
        bot.send_message(chat_id=ID, text=text)
        url = message.text
        get_video = snaptik(f'{url}')
        get_video_list = list(get_video)
        get_video_list[0].download(f'video{ID}.mp4')
        video = open(f'video{ID}.mp4', 'rb')
        bot.send_video(chat_id=ID, video=video,
                       caption=caption,
                       reply_markup=start_inline_keyboard())
        video.close()
        os.remove(f'video{ID}.mp4')
    except:
        text = 'Некоректная ссылка, или тех.работы. Попробуйте позже.'
        bot.send_message(chat_id=message.chat.id,
                         text=text, reply_markup=start_inline_keyboard())


bot.polling(none_stop=True, interval=0)
