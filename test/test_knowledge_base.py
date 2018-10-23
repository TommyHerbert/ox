import unittest
from knowledge.knowledge_base import KnowledgeBase
from knowledge.knowledge_base_populator import KnowledgeBasePopulator
from knowledge.relation import Relation
from knowledge.myself import Myself
from knowledge.adele import Adele


class TestKnowledgeBase(unittest.TestCase):
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

