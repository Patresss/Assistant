#!/usr/bin/env python3
import os
import random

import logging

from WordUtil import get_next_word_in_text, is_word_in_text
from module.AbstractModule import AbstractMode
from module.MusicManager import MusicManager


class MusicModule(AbstractMode):
    logger = logging.getLogger(__name__)
    KEY_WORDS = ["muzyk", "imprez"]

    FOLDER_WORDS = [" folde[a-z]* ", " kataloga-z]* "]
    STOP_WORDS = ["stop", "trzymaj", "pauza"]
    NEXT_WORDS = ["stęp", "step", "dalej"]
    MANAGER_WORDS = STOP_WORDS + NEXT_WORDS
    player = None
    MUSIC_PATH = "../music/"

    def __init__(self):
        AbstractMode.__init__(self)
        self.music_manager = MusicManager()

    def response(self, command):
        if is_word_in_text(command, self.NEXT_WORDS):
            self.music_manager.next_music()
            return ""
        elif is_word_in_text(command, self.STOP_WORDS):
            self.music_manager.stop_music()
            self.working = False
            return "Zatrzymuję muzykę"
        else:
            folder = get_next_word_in_text(command, self.FOLDER_WORDS)
            folder = folder.lower()
            self.logger.debug("Load folder: " + folder)
            if folder != "":
                try:
                    self.music_manager.init_folder_music(folder)
                except Exception as error:
                    return str(error)
            else:
                self.music_manager.init_all_music()
            self.working = True
            return "Uruchamiam muzyke " + folder

    def get_random_music(self, folder):
        folder_path = self.MUSIC_PATH + folder
        self.logger.debug("Found music directory: " + folder_path)
        random_file = random.choice(os.listdir(folder_path))
        file = folder_path + "/" + random_file
        self.logger.debug("Found music file: " + file)
        return file
