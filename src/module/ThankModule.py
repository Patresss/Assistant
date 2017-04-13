#!/usr/bin/env python3
from datetime import datetime

from WordUtil import is_word_in_text
from module.AbstractModule import AbstractMode


class ThankModule(AbstractMode):
    KEY_WORDS = ["dzięk"]

    def __init__(self):
        AbstractMode.__init__(self)

    def response(self, command):
        return "Nie ma za co!"


