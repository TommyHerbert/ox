import unittest
from knowledge.singer import Singer
from knowledge.adele import Adele
from knowledge.hello import Hello
from knowledge.someone_like_you import SomeoneLikeYou
from os import makedirs
from os.path import join, exists
from shutil import rmtree
from utils.knowledge import create_empty_package

OUTPUT_DIR = 'utils_test_output'


class TestConcept(unittest.TestCase):
    def setUp(self):
        self.clear_output()

    def tearDown(self):
        self.clear_output()

    def clear_output(self):
        if exists(OUTPUT_DIR):
            rmtree(OUTPUT_DIR)
 
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

