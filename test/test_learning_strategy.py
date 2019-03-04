from unittest import TestCase
from knowledge.knowledge_base import KnowledgeBase
from conversation.naive_learning_strategy import select
from knowledge.adele import Adele
from knowledge.singer import Singer
from knowledge.relation import Relation


class TestLearningStrategy(TestCase):
    def test_learning_strategy(self):
        knowledge_base = KnowledgeBase()
        adele = Adele()
        singer = Singer()
        relation = Relation('is_a', (adele, singer))
        new_elements = ((adele,), (singer,), (relation,))
        self.assertEqual(new_elements, select(new_elements, knowledge_base))

