#!/usr/bin/env python3
import logging
import speech_recognition
from subprocess import Popen, PIPE, STDOUT

import time


class Listener:
    DEFAULT_LANGUAGE = 'pl-PL'
    logger = logging.getLogger(__name__)
    phrase_time_limit = None

    def __init__(self):
        self.recognizer = speech_recognition.Recognizer()

    def listen(self):
        with speech_recognition.Microphone() as source:
            print("Say something!")
            audio = self.recognizer.listen(source, phrase_time_limit=self.phrase_time_limit)

        # recognize speech using Google Speech Recognition
        try:
            text = self.recognizer.recognize_google(audio, language=self.DEFAULT_LANGUAGE)
            logging.debug("Google Speech Recognition thinks you said " + text)
            return text
        except speech_recognition.UnknownValueError:
            logging.error("Google Speech Recognition could not understand audio")
            return ""
        except speech_recognition.RequestError as e:
            logging.error("Could not request results from Google Speech Recognition service; {0}".format(e))
