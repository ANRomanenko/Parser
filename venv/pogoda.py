from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
config_dict['language'] = 'RU'

owm = OWM('068a0d70832ad0913738b232c02a35c6', config_dict)
place = input("В каком городе/стране?: ")

mgr = owm.weather_manager()
observation = mgr.weather_at_place(place)
w = observation.weather

temp = w.temperature('celsius')["temp"]

print("В городе", place, "сейчас", w.detailed_status + "!", "Температура воздуха", temp, "градусов!")

if temp < 10:
    print("Сейчас ппц как холодно, оденься теплее!")
elif temp < 20:
    print("Оденься теплее!")
else:
    print("Температура норм одевай что угодно!")

