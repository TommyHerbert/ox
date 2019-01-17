import unittest
from knowledge.knowledge_base import KnowledgeBase
from knowledge.knowledge_base_populator import KnowledgeBasePopulator
from knowledge.relation import Relation
from knowledge.myself import Myself
from knowledge.adele import Adele
from knowledge.hello import Hello
from knowledge.singer import Singer
from knowledge.song import Song
from os.path import exists
from shutil import rmtree
from utils.knowledge import create_empty_knowledge_package

OUTPUT_DIR = 'utils_test_output'


class TestKnowledgeBase(unittest.TestCase):
    def setUp(self):
        self.clear_output()

    def tearDown(self):
        self.clear_output()

    def clear_output(self):
        if exists(OUTPUT_DIR):
            rmtree(OUTPUT_DIR)

    def test_copy(self):
        knowledge_base1 = KnowledgeBase()
        KnowledgeBasePopulator.populate(knowledge_base1)
        knowledge_base2 = knowledge_base1.copy()
        self.assertTrue(knowledge_base1.matches(knowledge_base2))
        # TODO: By the way, why do we use 'matches' instead of '=='?
        del knowledge_base1.things[0]
        self.assertFalse(knowledge_base1.matches(knowledge_base2))

    def test_add_thing(self):
        knowledge_base = KnowledgeBase()
        adele = Adele()
        knowledge_base.add_thing(adele)
        self.assertIn(adele, knowledge_base.things)
        knowledge_base.add_thing(adele)
        self.assertEqual(1, len(knowledge_base.things)) # no duplicates

    def test_add_relation(self):
        knowledge_base = KnowledgeBase()
        KnowledgeBasePopulator.populate(knowledge_base)
        initial_relations_count = len(knowledge_base.relations)
        name = 'likes'
        args = (Myself(), Adele(), 1000)
        knowledge_base.add_relation(name, args)
        relations_count = len(knowledge_base.relations)
        self.assertEqual(initial_relations_count + 1, relations_count)
        relation = Relation(name, args)
        self.assertIn(relation, knowledge_base.relations)

    def test_merge(self):
        adele = Adele()
        hello = Hello()
        singer = Singer()
        song = Song()

        base1 = KnowledgeBase()
        base2 = KnowledgeBase()
        expected = KnowledgeBase()

        base1.add_thing(adele)
        base1.categories.append(singer)
        base1.add_relation('is_a', (adele, singer))

        base2.add_thing(adele)
        base2.add_thing(hello)
        base2.categories.append(song)
        base2.add_relation('is_a', (hello, song))

        expected.add_thing(adele)
        expected.things = [adele, hello]
        expected.categories = [singer, song]
        expected.add_relation('is_a', (adele, singer))
        expected.add_relation('is_a', (hello, song))

        self.assertTrue(expected.matches(base1.merge(base2)))

    def test_write_package(self):
        create_empty_knowledge_package(OUTPUT_DIR)
        knowledge_base = KnowledgeBase()
        KnowledgeBasePopulator.populate(knowledge_base)
        knowledge_base.write_package(OUTPUT_DIR)
        from OUTPUT_DIR import knowledge as knowledge2
        copied_base = knowledge2.KnowledgeBase()
        knowledge2.KnowledgeBasePopulator.populate(copied_base)
        self.assertTrue(knowledge_base.matches(copied_base))
