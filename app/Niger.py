"""
 _____
/  __ \
| /  \/ ___  _ __  ___ _   _
| |    / _ \| '_ \/ __| | | |
| \__/\ (_) | | | \__ \ |_| |
 \____/\___/|_| |_|___/\__, |
                        __/ |
                       |___/
©Consy 2024-2025
"""

from random import randint
from telebot import types, TeleBot
from os import listdir
bot = TeleBot("", parse_mode=None)
admin = ""
def sendphoto(message):
    files = listdir('neko')
    file_numbers = [int(file.split('.')[0]) for file in files if file.split('.')[0].isdigit()]
    image = open("app/neko/" + str(randint(0, max(file_numbers))) + ".jpg", "rb")
    bot.send_photo(message.chat.id, image)
    image.close()

@bot.message_handler(commands=['neko'])
def neko(message):
    sendphoto(message)
@bot.message_handler(commands=['all_photo'])
def all(message):
    files = listdir("neko")
    file_numbers = [int(file.split('.')[0]) for file in files if file.split('.')[0].isdigit()]
    for i in range(0, max((file_numbers))):
        with open(f"app/neko/{i}.jpg", "rb") as f:
            bot.send_photo(message.chat.id, f, caption=str(i + 1))
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Neko")
    btn2 = types.KeyboardButton("About")
    markup.add(btn1, btn2)
    bot.reply_to(message, "Command: \n/neko - send neko image", reply_markup=markup)
@bot.message_handler(commands=['nsfw'])
def nsfw1(message):
    bot.reply_to(message, "/nekoNSFW")
@bot.message_handler(commands=['nekoNSFW'])
def func(message):
    image = open("app/nsfw/" + str(randint(0, 37)) + ".jpg", "rb")
    bot.send_photo(message.chat.id, image)
    image.close()
    db[message.chat.id]['point'] += 1
@bot.message_handler(content_types=['text'])
def button(message):
    if(message.text == "Neko"):
        sendphoto(message)
    elif(message.text == "About"):
        bot.reply_to(message, "Discord: cons_y\nTelegram: @fu4ju")
    else:
        try:
            image = open("app/neko/" + str(int(message.text) - 1) + ".jpg", "rb")
            bot.send_photo(message.chat.id, image)
            image.close()
        except:
            files = listdir('app/neko')
            file_numbers = [int(file.split('.')[0]) for file in files if file.split('.')[0].isdigit()]
            bot.reply_to(message, f"Максимальное значение {max(file_numbers) + 1}, минимальное значение 1")
@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    if str(message.chat.id) == admin:
        # Получаем информацию о файле
        file_id = message.photo[-1].file_id
        file_info = bot.get_file(file_id)
        file_extension = '.' + file_info.file_path.split('.')[-1]

        # Находим порядковый номер для нового файла
        files = listdir('app/neko')
        file_numbers = [int(file.split('.')[0]) for file in files if file.split('.')[0].isdigit()]
        if file_numbers:
            next_file_number = max(file_numbers) + 1
        else:
            next_file_number = 1

        # Сохраняем файл в папку 'neko'
        downloaded_file = bot.download_file(file_info.file_path)
        with open(f'app/neko/{next_file_number}{file_extension}', 'wb') as new_file:
            new_file.write(downloaded_file)

        bot.reply_to(message, "Фото сохранено!")
bot.polling(none_stop=True)
#alah adbar
