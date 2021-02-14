from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'RU'
import telebot



owm = OWM('068a0d70832ad0913738b232c02a35c6', config_dict)
bot = telebot.TeleBot("1513643533:AAHQmiFOCCGv5RAqTLLw7lkyVAashh4yqvo") # You can set parse_mode by default. HTML or MARKDOWN

@bot.message_handler(content_types=['text'])
def send_echo(message):
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    temp = w.temperature('celsius')["temp"]

    answer = "В городе " + message.text + " сейчас " + w.detailed_status + "!" + "\n"
    answer += "Температура воздуха " + str(temp) + " градусов!" + "\n\n"

    if temp < 10:
        answer += "Сейчас ппц как холодно, оденься теплее!"
    elif temp < 20:
        answer += "Оденься теплее!"
    else:
        answer += "Температура норм одевай что угодно!"

    bot.send_message(message.chat.id, answer)

bot.polling( none_stop=True )