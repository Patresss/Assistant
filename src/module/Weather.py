#!/usr/bin/env python3
from datetime import datetime, timedelta

import logging
import pyowm
from pyowm.exceptions.not_found_error import NotFoundError


class Weather:
    KEY_API = "cbbb2a1fffc0881cd553539bd15bfc61"
    DEFAULT_CITY = "Krakow"
    DEFAULT_DAY = 0
    over_range = False
    polish_dictionary = {
        'clear sky': 'czyste niebo',
        'few clouds': 'kilka chmur',
        'scattered clouds': 'rozproszone chmury',
        'broken clouds': 'złamane chmury',
        'rain': 'deszcz',
        'thunderstorm': 'burza z piorunami',
        'thunderstorm with light rain': 'burze z lekkim deszczem',
        'thunderstorm with rain': 'burza z deszczem',
        'thunderstorm with heavy rain': 'burza z dużym opadem',
        'light thunderstorm': 'lekka burza',
        'heavy thunderstorm': 'ciężka burza',
        'ragged thunderstorm': 'burza deszczowa',
        'thunderstorm with light drizzle': 'burze z lekkim deszczem',
        'thunderstorm with drizzle': 'burze z deszczem',
        'thunderstorm with heavy drizzle': 'burza z dużym opadem',
        'light intensity drizzle': 'mętność intensywności światła',
        'drizzle': 'mżawka',
        'heavy intensity drizzle': 'deszcz',
        'light intensity drizzle rain': 'deszcz',
        'drizzle rain': 'deszcz',
        'heavy intensity drizzle rain': 'deszcz',
        'shower rain and drizzle': 'mżawka',
        'heavy shower rain and drizzle': 'deszcz',
        'shower drizzle': 'deszcz',
        'light rain': 'lekki deszcz',
        'moderate rain': 'umiarkowany deszcz',
        'heavy intensity rain': 'deszcz o dużej intensywności',
        'very heavy rain': 'bardzo silny deszcz',
        'extreme rain': 'ekstremalny deszcz',
        'freezing rain': 'marznący deszcz',
        'light intensity shower rain': 'deszcz',
        'shower rain': 'niewielki deszczowy',
        'heavy intensity shower rain': 'intensywny deszcz deszczowy',
        'ragged shower rain': 'deszcz',
        'light snow': 'lekkie opady śniegu',
        'snow': 'śnieg',
        'heavy snow': 'duże opady śniegu',
        'sleet': 'śnieg z deszczem',
        'shower sleet': 'deszcz',
        'light rain and snow': 'lekki deszcz i śnieg',
        'rain and snow': 'deszcz i śnieg',
        'light shower snow': 'lekki deszcz śniegu',
        'shower snow': 'pada deszcz',
        'heavy shower snow': 'ciężki deszcz śniegu',
        'mist': 'zamglenie',
        'smoke': 'palić',
        'haze': 'mgła',
        'sand, dust whirls': 'piasek, wiry pyłowe',
        'fog': 'mgła',
        'sand': 'piasek',
        'dust': 'kurz',
        'volcanic ash': 'pył wulkaniczny',
        'squalls': 'skręty',
        'tornado': 'tornado',
        'overcast clouds': 'zachmurzone chmury',
        'tropical storm': 'burza tropikalna',
        'hurricane': 'huragan',
        'cold': 'zimno',
        'hot': 'gorąco',
        'windy': 'wietrzny',
        'hail': 'grad',
        'calm': 'spokojna',
        'light breeze': 'lekka bryza',
        'gentle breeze': 'delikatna bryza',
        'moderate breeze': 'umiarkowana bryza',
        'fresh breeze': 'świeża bryza',
        'strong breeze': 'silny powiew',
        'high wind, near gale': 'silny wiatr, blisko wiatru',
        'gale': 'wichura',
        'severe gale': 'ciężki oddech',
        'storm': 'burza',
        'violent storm': 'gwałtowna burza'
    }

    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)

    def __init__(self, city=DEFAULT_CITY, day_to_forecast=DEFAULT_DAY):
        logging.debug("Checking weather for city: %s | day: %s", city, str(day_to_forecast))
        self.owm = pyowm.OWM(self.KEY_API)
        self.city = city
        self.day_to_forecast = day_to_forecast
        if day_to_forecast <= 0:
            self.forecast_at_day = 0
            observation = self.owm.weather_at_place(city)
            weather = observation.get_weather()
            temp_float = weather.get_temperature('celsius').get('temp')
            self.temp = int(temp_float)
            org_description = weather.get_detailed_status()
            self.description = self.get_translated_description(org_description)
        else:
            try:
                date_to_forecast = self.get_day(day_to_forecast)
                forecast = self.owm.daily_forecast(city)
                temp_float = forecast.get_weather_at(date_to_forecast).get_temperature('celsius').get('day')
                self.temp = int(temp_float)
                org_description = forecast.get_weather_at(date_to_forecast).get_detailed_status()
                self.description = self.get_translated_description(org_description)
            except NotFoundError:
                self.over_range = True

    def get_translated_description(self, english_word):
        try:
            return self.polish_dictionary[english_word]
        except KeyError:
            return english_word

    def get_response(self):
        if self.over_range:
            logging.warn("Day in forecast is overange")
            return "Liczba jest po za zakresem, podaj max 5"
        else:
            if self.day_to_forecast == 0:
                day_part = "obecnie "
            elif self.day_to_forecast == 1:
                day_part = "na jutro "
            else:
                day_part = "za %d dni: " % (self.day_to_forecast)
            message = "Pogoda dla miasta %s %s: %s i %d stopni celcjusza" % (self.city, day_part, self.description, self.temp)
            return message

    def get_day(self, day):
        date = datetime.now()
        date = date.replace(hour=12, minute=00)
        date += timedelta(days=day)
        return date
