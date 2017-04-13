#!/usr/bin/env python3
from WordUtil import get_next_word_in_text
from module.AbstractModule import AbstractMode

from module.Weather import Weather


class WeatherModule(AbstractMode):
    KEY_WORDS = ["pogod"]
    BEFORE_CITY_WORD = [" dla "]
    BEFORE_DAY_WORD = [" za ", " na "]

    def __init__(self):
        AbstractMode.__init__(self)

    def response(self, command):
        city = get_next_word_in_text(command, self.BEFORE_CITY_WORD)

        day_str = get_next_word_in_text(command, self.BEFORE_DAY_WORD)
        try:
            day = int(day_str)
        except ValueError:
            day = 0

        if city == "":
            weather = Weather(day_to_forecast=day)
        else:
            weather = Weather(city, day)
        return weather.get_response()
