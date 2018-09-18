import unittest
from knowledge.singer import Singer
from knowledge.hello import Hello
from knowledge.someone_like_you import SomeoneLikeYou


class TestConcept(unittest.TestCase):
    def test_equality(self):
        singer1 = Singer()
        singer2 = Singer()
        adele1 = Adele()
        adele2 = Adele()

        self.assertEqual(singer1, singer2)
        self.assertEqual(adele1, adele2)
        self.assertNotEqual(singer1, adele1)

    def test_less_than(self):
        hello1 = Hello()
        hello2 = Hello()
        someone_like_you = SomeoneLikeYou()
        self.assertTrue(hello1 < someone_like_you)
        self.assertFalse(hello1 < hello2)

