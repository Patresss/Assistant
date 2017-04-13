#!/usr/bin/env python3
from datetime import datetime

from module import vlc
from module.AbstractModule import AbstractMode


class MusicModule(AbstractMode):
    KEY_WORDS = ["muzyk", "imprez"]

    def __init__(self):
        AbstractMode.__init__(self)

    def response(self, command):
        return "Uruchamiam muzyke"

    def work(self):
        player = vlc.MediaPlayer("../music/Spotify/4 Non Blondes - What's Up.mp3")
        player.play()

