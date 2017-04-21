#!/usr/bin/env python3
import logging
import os

from module.AbstractModule import AbstractMode


class SystemModule(AbstractMode):
    logger = logging.getLogger(__name__)
    KEY_WORDS = ["wyłącz"]

    def __init__(self):
        AbstractMode.__init__(self)

    def response(self, command):
        os.system("shutdown now -h")
        return "Dowidzenia"
