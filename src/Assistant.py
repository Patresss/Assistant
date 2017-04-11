#!/usr/bin/env python3
import sys

from Listener import Listener
from Speaker import Speaker
from module.JokeModule import JokeModule
from module.SwearwordModule import SwearwordModule
from module.TimeModule import TimeModule
from module.WeatherModule import WeatherModule


class Assistant:
    list_of_module = {TimeModule(), WeatherModule(), SwearwordModule(), JokeModule()}

    def __init__(self):
        self.speaker = Speaker()
        self.listener = Listener()

    def run(self):
        while True:
            sys.stdout.flush()
            self.listen()

    def listen(self):
        command = self.listener.listen()
        module = self.found_module(command)
        if module:
            response = module.response(command)
            self.speaker.speak(response)

    def found_module(self, command):
        for module in self.list_of_module:
            if module.active and module.is_in_text(command):
                return module
