import unittest
from knowledge.song import Song
from knowledge.adele import Adele
from knowledge.knowledge_base import KnowledgeBase
from knowledge.knowledge_base_populator import KnowledgeBasePopulator


class TestSelfWriting(unittest.TestCase):
    def setUp(self):
        pass # TODO: create test_output package with __init__.py

    def tearDown(self):
        pass # TODO: destroy test_output package and all its contents

    def test_get_import_statement(self):
        expected = 'from foo.bar.baz.qux.knowledge.song import Song'
        actual = Song().get_import_statement('foo/bar/baz/qux')
        self.assertEqual(expected, actual)

    def test_get_import_statement_with_empty_path(self):
        expected = 'from knowledge.song import Song'
        actual = Song().get_import_statement()
        self.assertEqual(expected, actual)

    def test_get_instantiation_statement(self):
        expected = 'adele = Adele()'
        self.assertEqual(expected, Adele().get_instantiation_statement())

    def test_is_knowledge_base_empty(self):
        knowledge_base = KnowledgeBase()
        self.assertTrue(knowledge_base.is_empty())
        KnowledgeBasePopulator.populate(knowledge_base)
        self.assertFalse(knowledge_base.is_empty())

    def test_matches(self):
        knowledge_base1 = KnowledgeBase()
        knowledge_base2 = KnowledgeBase()
        knowledge_base3 = KnowledgeBase()
        knowledge_base1.things.append(Adele())
        knowledge_base2.things.append(Adele())
        knowledge_base3.categories.append(Song())
        self.assertTrue(knowledge_base1.matches(knowledge_base2))
        self.assertFalse(knowledge_base1.matches(knowledge_base3))

    #def test_export_populator(self):
    #    knowledge_base1 = KnowledgeBase()
    #    KnowledgeBasePopulator.populate(knowledge_base1)
    #    knowledge_base1.export_populator('test_output/iteration2')
    #    from test_output.iteration2.knowledge \
    #        import KnowledgeBasePopulator as KnowledgeBasePopulator2
    #    knowledge_base2 = KnowledgeBase()
    #    KnowledgeBasePopulator2.populate(knowledge_base2)
    #    self.assertTrue(knowledge_base1.matches(knowledge_base2))
        # TODO

