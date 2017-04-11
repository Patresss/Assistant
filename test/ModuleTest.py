import unittest

from module.JokeModule import JokeModule
from module.SwearwordModule import SwearwordModule
from module.TimeModule import TimeModule
from module.WeatherModule import WeatherModule


class ModuleTest(unittest.TestCase):
    def test_module_weather(self):
        module = WeatherModule()
        response = module.response("Pogoda")
        print(response)
        self.assertIsNotNone(response)

    def test_module_weather_day(self):
        module = WeatherModule()
        response = module.response("Pogoda za 3 dni")
        print(response)
        self.assertIsNotNone(response)

    def test_module_weather_city(self):
        module = WeatherModule()
        response = module.response("Pogoda dla Wrocław")
        print(response)
        self.assertIsNotNone(response)

    def test_module_weather_full(self):
        module = WeatherModule()
        response = module.response("Pogoda dla Kraków za 4 dni")
        print(response)
        self.assertIsNotNone(response)

    def test_module_time(self):
        module = TimeModule()
        response = module.response("")
        print(response)
        self.assertIsNotNone(response)

    def test_module_joke(self):
        module = JokeModule()
        response = module.response("")
        print(response)
        self.assertIsNotNone(response)

    def test_module_swearword(self):
        module = SwearwordModule()
        response = module.response("")
        print(response)
        self.assertIsNotNone(response)

if __name__ == '__main__':
    unittest.main()
