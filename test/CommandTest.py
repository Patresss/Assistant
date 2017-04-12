import unittest

from Assistant import Assistant
from module.CuriosityModule import CuriosityModule
from module.DrinkModule import DrinkModule
from module.JokeModule import JokeModule
from module.MusicModule import MusicModule
from module.SwearwordModule import SwearwordModule
from module.ThankModule import ThankModule
from module.TimeModule import TimeModule
from module.WeatherModule import WeatherModule


class CommandTest(unittest.TestCase):
    assistant = Assistant()

    def test_module_time(self):
        command_time = "Która jest godzina?"
        module = self.assistant.found_module(command_time)
        self.assertIsInstance(module, TimeModule.__base__)

    def test_module_weather(self):
        command_time = "Jaką mamy pogodę?"
        module = self.assistant.found_module(command_time)
        self.assertIsInstance(module, WeatherModule.__base__)

    def test_module_swearword(self):
        command_time = "chuj"
        module = self.assistant.found_module(command_time)
        self.assertIsInstance(module, SwearwordModule.__base__)

    def test_module_curiosity(self):
        command_time = "Powiedz coś ciekawego"
        module = self.assistant.found_module(command_time)
        self.assertIsInstance(module, CuriosityModule.__base__)

    def test_module_joke(self):
        command_time = "Powiedz żart"
        module = self.assistant.found_module(command_time)
        self.assertIsInstance(module, JokeModule.__base__)

    def test_module_drink(self):
        command_time = "Napiłbym się piwa"
        module = self.assistant.found_module(command_time)
        self.assertIsInstance(module, DrinkModule.__base__)

    def test_module_thank(self):
        command_time = "Dziękuję"
        module = self.assistant.found_module(command_time)
        self.assertIsInstance(module, ThankModule.__base__)

    def test_module_music(self):
        command_time = "Uruchom muzykę"
        module = self.assistant.found_module(command_time)
        self.assertIsInstance(module, MusicModule.__base__)

if __name__ == '__main__':
    unittest.main()
