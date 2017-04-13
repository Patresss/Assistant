#!/usr/bin/env python3
from datetime import datetime

from WordUtil import is_word_in_text
from module.AbstractModule import AbstractMode


class SwearwordModule(AbstractMode):
    KEY_WORDS = ["kurwa", "zajeb", "pierdol", '[c]?huj', 'spierdalaj']

    def __init__(self):
        AbstractMode.__init__(self)

    def response(self, command):
        return "Nie przeklinaj śmieciu!"


