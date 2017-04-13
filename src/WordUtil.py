#!/usr/bin/env python3
import re
import string

ALL_CHARS = ".*"


def is_word_in_text(text, key_words):
    text = text.lower()
    return any(re.compile(ALL_CHARS + regex + ALL_CHARS).match(text) for regex in key_words)


def get_next_word_in_text(text, key_words):
    try:
        for key in key_words:
            next_word = re.split(key, text)[1]
            next_word = next_word.split(" ")[0]
            if next_word != text:
                return next_word
        return ""
    except:
        return ""
