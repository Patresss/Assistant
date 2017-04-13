#!/usr/bin/env python3
from datetime import datetime

from WordUtil import is_word_in_text
from module.AbstractModule import AbstractMode


class DrinkModule(AbstractMode):
    KEY_WORDS = ["piwo", "piwa", "wódka", 'wóda', 'wódeczki', 'napiłbym']

    def __init__(self):
        AbstractMode.__init__(self)

    def response(self, command):
        return "Czas na picie!"


