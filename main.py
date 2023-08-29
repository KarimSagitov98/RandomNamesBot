import random
import telebot

bot = telebot.TeleBot('Token')  # Укажите здесь свой токен бота

# Загрузка данных имен и фамилий из файлов
with open('имена.txt', 'r', encoding='utf-8') as f:
    имена = f.read().splitlines()

with open('фамилии.txt', 'r', encoding='utf-8') as f:
    фамилии = f.read().splitlines()

# Обработка команды /name
@bot.message_handler(commands=['name'])
def get_name(message):
    # Генерация случайного имени и фамилии
    имя = random.choice(имена)
    фамилия = random.choice(фамилии)

    # Отправка имени и фамилии пользователю
    bot.send_message(message.chat.id, f'{фамилия} {имя}')

# Обработка команды /generate с параметром
@bot.message_handler(commands=['generate'])
def generate_names(message):
    count = int(message.text.split()[1])  # Получение числа из параметра

    result = []  # Список для хранения сгенерированных имен
    if count > 100:
        bot.send_message(message.chat.id, 'Нельзя генерировать более 100 имен')

    # Генерация нужного количества имен
    else:
        for _ in range(count):
            имя = random.choice(имена)
            фамилия = random.choice(фамилии)
            result.append(f'{фамилия} {имя}')

    # Отправка списка имен пользователю
    bot.send_message(message.chat.id, '\n'.join(result))

# Запуск бота
bot.polling()