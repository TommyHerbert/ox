import unittest
from knowledge.knowledge_base import KnowledgeBase
from knowledge.knowledge_base_populator import KnowledgeBasePopulator
from knowledge.relation import Relation
from knowledge.myself import Myself
from knowledge.adele import Adele


class TestKnowledgeBase(unittest.TestCase):
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

