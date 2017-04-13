#!/usr/bin/env python3
import logging
import os
import random

import Assistant
from WordUtil import get_next_word_in_text, is_word_in_text
from module.AbstractModule import AbstractMode
from module.manager.MusicManager import MusicManager


class SystemModule(AbstractMode):
    logger = logging.getLogger(__name__)
    KEY_WORDS = ["wyłącz"]

    def __init__(self):
        AbstractMode.__init__(self)
        self.music_manager = MusicManager()

    def response(self, command):
        os.system("shutdown now -h")
        return "Dowidzenia"
