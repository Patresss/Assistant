#!/usr/bin/env python3
import sys

from Listener import Listener
from Singleton import Singleton
from Speaker import Speaker
from module.CuriosityModule import CuriosityModule
from module.DrinkModule import DrinkModule
from module.JokeModule import JokeModule
from module.MusicModule import MusicModule
from module.SwearwordModule import SwearwordModule
from module.ThankModule import ThankModule
from module.TimeModule import TimeModule
from module.WeatherModule import WeatherModule


@Singleton
class Assistant:
    list_of_module = {
        TimeModule(),
        WeatherModule(),
        SwearwordModule(),
        JokeModule(),
        CuriosityModule(),
        DrinkModule(),
        MusicModule(),
        ThankModule()}

    def __init__(self):
        self.speaker = Speaker()
        self.listener = Listener()

    def run(self):
        self.speaker.speak("Dzień dobry")
        while True:
            sys.stdout.flush()
            self.listen()

    def listen(self):
        command = self.listener.listen()
        module = self.found_module(command)
        if module:
            response = module.response(command)
            self.speaker.speak(response)
            module.work(command)

    def found_module(self, command):
        for module in self.list_of_module:
            if module.active and module.is_in_text(command):
                return module
