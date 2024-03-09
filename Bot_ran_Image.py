# https://t.me/my_2sinergbot

import telebot
import random

# TOKEN ='' тут токен вашего бота
TOKEN = ''

bot = telebot.TeleBot(TOKEN)

# Список изображений
images = [
    'https://img.freepik.com/free-vector/flat-design-forest-landscape_23-2149155031.jpg',
    'https://img.freepik.com/free-photo/ai-cloud-concept-with-robot-arm_23-2149739748.jpg',
    'https://img.freepik.com/free-photo/ai-cloud-concept-with-robot-face_23-2149739753.jpg',
    'https://img.freepik.com/free-photo/ai-cloud-concept-with-cube_23-2149739756.jpg',
    'https://img.freepik.com/premium-photo/board-game-with-dice-numbers-it_899894-21838.jpg',
    'https://img.freepik.com/premium-photo/man-stands-tunnel-that-has-black-hole-it_899894-2189.jpg',
    'https://img.freepik.com/premium-photo/there-is-turtle-generative-ai_899894-1104.jpg',
    'https://img.freepik.com/free-vector/hand-drawn-mountain-silhouette_23-2150526375.jpg',
    'https://img.freepik.com/free-photo/3d-rendering-house-model_23-2150799797.jpg',
    'https://img.freepik.com/premium-photo/portrait-baby-badger-forest-ai-generative_843410-972.jpg',
    'https://img.freepik.com/premium-photo/baby-squirrel-spring-green-grass-with-flowers-generative-ai_843410-454.jpg'
]


@bot.message_handler(commands=['img'])
def send_random_image(message):
    random_image = random.choice(images)
    bot.send_photo(message.chat.id, random_image)


# Запуск обработчика сообщений
bot.infinity_polling()

# Идеи
# написать логику гет запроса на сайт с картинками, получить ссылку HTML получить запрос от сервака по переменной src получить изображения, и рандомизовать, что бы бот мог выдать кучу картинок
