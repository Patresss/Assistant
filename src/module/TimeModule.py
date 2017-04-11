#!/usr/bin/env python3
from datetime import datetime

from WordUtil import is_word_in_text
from module.AbstractModule import AbstractMode


class TimeModule(AbstractMode):
    KEY_WORDS = ["godzina", "czas"]

    def __init__(self):
        AbstractMode.__init__(self)

    def response(self, command):
        time = datetime.now().strftime('%H:%M:%S')
        return "Aktualna godzina to " + time


