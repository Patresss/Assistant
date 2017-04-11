#!/usr/bin/env python3
import re
import string

ALL_CHARS = ".*"


def is_word_in_text(text, key_words):
    return any(re.compile(ALL_CHARS + regex + ALL_CHARS).match(text) for regex in key_words)


def get_next_word_in_text(text, key):
    separate_words = [word.strip(string.punctuation) for word in text.lower().split()]
    try:
        index = separate_words.index(key)
        next_word = separate_words[index + 1]
        return next_word
    except:
        return ""
