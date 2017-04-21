#!/usr/bin/env python3

from mpd import MPDClient


class MpdClient:
    HOSTNAME = "192.168.72.129"
    PORT = 6600
    TIMEOUT = 3

    def __init__(self):
        self.client = MPDClient()
        self.client.connect(self.HOSTNAME, self.PORT, self.TIMEOUT)

    def pause(self):
        self.client.pause()

    def play(self):
        self.client.play()

    def next(self):
        self.client.next()

    def previous(self):
        self.client.previous()

    def stop(self):
        self.client.stop()

    def is_playing(self):
        print(self.client.status().get('state') == "play")
