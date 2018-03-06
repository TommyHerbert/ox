from unittest import TestCase
from main.ox import Ox


class TestOx(TestCase):
    def test_song(self):
        self.assertEqual('Hello', Ox().tell("What's your favourite song?"))

    def test_adele_song(self):
        self.assertEqual('Hello', Ox().tell("What's your favourite Adele song?"))

    def test_dont_understand(self):
        self.assertEqual("Sorry, I didn't understand that.", Ox().tell("Hello Ox."))

    def test_favourite_foo(self):
        self.assertEqual("Sorry, I didn't understand that.", Ox().tell("What's your favourite foo?"))
