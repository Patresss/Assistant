import unittest
from datetime import datetime, timedelta


class ModuleTest(unittest.TestCase):
    def test_date(self):
        date = datetime.now()
        date = date.replace(hour=12, minute=00)
        date += timedelta(days=10)
        print(date)


if __name__ == '__main__':
    unittest.main()
