import unittest
from knowledge.knowledge_base import KnowledgeBase
from knowledge.knowledge_base_populator import KnowledgeBasePopulator


class TestKnowledgeBase(unittest.TestCase):
    def test_copy(self):
        knowledge_base1 = KnowledgeBase()
        KnowledgeBasePopulator.populate(knowledge_base1)
        knowledge_base2 = knowledge_base1.copy()
        self.assertTrue(knowledge_base1.matches(knowledge_base2))
        # TODO: By the way, why do we use 'matches' instead of '=='?
        del knowledge_base1.things[0]
        self.assertFalse(knowledge_base1.matches(knowledge_base2))

