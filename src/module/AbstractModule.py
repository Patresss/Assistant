#!/usr/bin/env python3
from WordUtil import is_word_in_text


class AbstractMode:
    KEY_WORDS = []
    MANAGER_WORDS = []
    working = False

    def __init__(self):
        self.active = True

    def is_in_text(self, text):
        return is_word_in_text(text, self.KEY_WORDS) or (self.working and is_word_in_text(text, self.MANAGER_WORDS))

    def work(self, command):
        return