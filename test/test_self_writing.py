import unittest
from knowledge.song import Song
from knowledge.adele import Adele
from knowledge.knowledge_base import KnowledgeBase


class TestSelfWriting(unittest.TestCase):

    # TODO: pass in a path
    def test_get_import_statement(self):
        expected = 'from knowledge.song import Song'
        self.assertEqual(expected, Song().get_import_statement())

    def test_get_instantiation_statement(self):
        expected = 'adele = Adele()'
        self.assertEqual(expected, Adele().get_instantiation_statement())

