import unittest
from knowledge.adele import Adele
from knowledge.singer import Singer
from knowledge.hello import Hello
from knowledge.someone_like_you import SomeoneLikeYou
from knowledge.relation import Relation


class TestRelation(unittest.TestCase):
    def test_equality(self):
        adele1 = Adele()
        adele2 = Adele()
        singer1 = Singer()
        singer2 = Singer()
        adeleSinger1 = Relation('is_a', (adele1, singer1))
        adeleSinger2 = Relation('is_a', (adele2, singer2))
        self.assertEqual(adeleSinger1, adeleSinger2)

        singerAdele = Relation('is_a', (singer1, adele1))
        self.assertNotEqual(adeleSinger1, singerAdele)

    def test_less_than(self):
        adele = Adele()
        hello = Hello()
        someone_like_you = SomeoneLikeYou()
        hello_relation = Relation('sang', (adele, hello))
        someone_relation = Relation('sang', (adele, someone_like_you))
        self.assertTrue(hello_relation < someone_like_you)

