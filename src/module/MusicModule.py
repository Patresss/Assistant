#!/usr/bin/env python3
import logging

import mpd

import Assistant
from WordUtil import is_word_in_text
from module.AbstractModule import AbstractMode
from module.manager.MpdClient import MpdClient


class MusicModule(AbstractMode):
    logger = logging.getLogger(__name__)
    MAIN_KEYS = ["muzyk", "imprez"]
    STOP_WORDS = ["stop", "[a-z]*trzymaj"]
    PAUSE_WORDS = ["pauza"]
    NEXT_WORDS = ["[a-z]*stęp[a-z]*", "[a-z]*step[a-z]*", "[d]?alej"]
    PREVIOUS_WORDS = ["[a-z]*oprzedni[a-z]*", "[a-z]*statni[a-z]*"]
    KEY_WORDS = MAIN_KEYS + STOP_WORDS + NEXT_WORDS + PAUSE_WORDS + PREVIOUS_WORDS

    def __init__(self):
        AbstractMode.__init__(self)
        self.mpd_client = MpdClient()

    def response(self, command):
        try:
            response = ""
            if is_word_in_text(command, self.NEXT_WORDS):
                self.mpd_client.next()
            elif is_word_in_text(command, self.PREVIOUS_WORDS):
                self.mpd_client.next()
            elif is_word_in_text(command, self.STOP_WORDS):
                self.mpd_client.stop()
                response = "Zatrzymuję muzykę"
            elif is_word_in_text(command, self.PAUSE_WORDS):
                self.mpd_client.pause()
                response = "Zapauzuj muzykę"
            else:
                self.mpd_client.play()
                response = "Uruchamiam muzyke"
            self.set_working(self.mpd_client.is_playing())
        except mpd.ConnectionError:
            self.mpd_client = MpdClient()
        return response

    def set_working(self, work):
        self.working = work
        if work:
            Assistant.Assistant.Instance().listener.phrase_time_limit = 2
        else:
            Assistant.Assistant.Instance().listener.phrase_time_limit = 5
