#!/usr/bin/env python3
import urllib.request
from datetime import datetime

from WordUtil import is_word_in_text
from module.AbstractModule import AbstractMode


class CuriosityModule(AbstractMode):
    KEY_WORDS = ["ciekaw"]

    def __init__(self):
        AbstractMode.__init__(self)

    def response(self, command):
        link = "http://www.deszczowce.pl/skrypty/losowa_ciekawostka.php"

        response = urllib.request.urlopen(link).read().decode("latin2")
        response2 = response.replace("&#45; ", "")
        response3 = response2.replace("');", "")
        response4 = response3.replace("document.write('", "")
        joke = " ".join(response4.split("<br />"))
        return joke


