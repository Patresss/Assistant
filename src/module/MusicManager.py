#!/usr/bin/env python3
import glob
import os
import random

import logging

from exceptions.NotFoundFolder import NotFoundFolder
from module import vlc


class MusicManager:
    logger = logging.getLogger(__name__)

    MUSIC_PATH = "../music/"
    LIST_OF_ALL_MUSIC = []
    LIST_OF_FOLDER_MUSIC = []

    def __init__(self):
        self.player = None
        self.LIST_OF_ALL_MUSIC = self.get_folder_list(self.MUSIC_PATH)

    def get_folder_list(self, path):
        music_list = []
        for filename in glob.iglob(path + '**/*.mp3', recursive=True):
            music_list.append(filename)
        return music_list

    def next_music(self):
        music = self.get_random_music()
        self.play_music(music)

    def stop_music(self):
        if not (self.player is None) and self.player.is_playing():
            self.player.stop()

    def init_folder_music(self, folder_name):
        try:
            folder_path = self.MUSIC_PATH + folder_name + "/"
            self.LIST_OF_FOLDER_MUSIC = self.get_folder_list(folder_path)
            self.next_music()
        except Exception:
            raise NotFoundFolder('Folder ' + folder_name + 'nie istnieje')


    def init_all_music(self):
        self.LIST_OF_FOLDER_MUSIC = self.LIST_OF_ALL_MUSIC
        self.next_music()

    def play_music(self, music):
        self.stop_music()
        self.player = vlc.MediaPlayer(music)
        self.player.play()

    def get_random_music(self):
        return random.choice(self.LIST_OF_FOLDER_MUSIC)
