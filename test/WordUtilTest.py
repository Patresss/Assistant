import unittest

from WordUtil import is_word_in_text, get_next_word_in_text
from module.WeatherModule import WeatherModule


class WordUtilTest(unittest.TestCase):
    def test_is_word_in_text(self):
        text = "Która jest godzina?"
        text2 = "Jaki mamy czas?"
        text3 = "Jaka jest teraz minuta?"
        key_words = ["godzina", "czas"]

        self.assertTrue(is_word_in_text(text, key_words))
        self.assertTrue(is_word_in_text(text2, key_words))
        self.assertFalse(is_word_in_text(text3, key_words))

    def test_next_word_city(self):
        module = WeatherModule()
        text = "Pogoda dla Kraków test"
        word = get_next_word_in_text(text, module.BEFORE_CITY_WORD)
        self.assertEqual(word, "Kraków")

    def test_next_word_day(self):
        module = WeatherModule()
        text = "Pogoda dla Kraków za 3 dni"
        word = get_next_word_in_text(text, module.BEFORE_DAY_WORD)
        self.assertEqual(word, "3")

    def test_next_word_music(self):
        text = "Muzyka dla folderu Kraków"
        word = get_next_word_in_text(text, ["folde[a-z]*", "katalog"])
        self.assertEqual(word, "Kraków")


if __name__ == '__main__':
    unittest.main()
