import unittest
from knowledge.copular_statement import CopularStatement
from knowledge.knowledge_base import KnowledgeBase
from conversation.reader import Reader
from knowledge.song import Song
from knowledge.relation import Relation
from knowledge.concept import Thing


class TestCopularStatement(unittest.TestCase):
    def test_get_logical_form(self):
        copular_statement = CopularStatement()
        knowledge_base = KnowledgeBase()
        song = Song()
        knowledge_base.categories.append(song)
        reader = Reader()
        proposition = copular_statement.get_logical_form('Closer is a song.',
                                                         knowledge_base,
                                                         reader)
        proposition.content.func(*proposition.content.args)
        Closer = type('Closer', (Thing,), {})
        closer = Closer()
        closer.lexical_form = 'Closer'
        self.assertIn(closer, knowledge_base.things)
        relation = Relation('is_a', (closer, song))
        self.assertIn(relation, knowledge_base.relations)

