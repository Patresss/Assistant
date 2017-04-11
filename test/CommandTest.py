import unittest

from Assistant import Assistant
from module.SwearwordModule import SwearwordModule
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


if __name__ == '__main__':
    unittest.main()
