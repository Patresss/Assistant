#!/usr/bin/env python3
import subprocess

import logging


class Speaker:
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger(__name__)

    def speak(self, text):
        logging.info("Speak " + text)
        subprocess.call(["../speech.sh", text])
