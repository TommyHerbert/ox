import unittest
from knowledge.song import Song
from knowledge.adele import Adele
from knowledge.singer import Singer
from knowledge.knowledge_base import KnowledgeBase
from knowledge.knowledge_base_populator import KnowledgeBasePopulator
from knowledge.relation import get_relation_import_statement, write_relation
from os import mkdir
from pathlib import Path
from shutil import rmtree


class TestSelfWriting(unittest.TestCase):
    def setUp(self):
        mkdir('test_output')
        Path('test_output/__init__.py').touch()

    def tearDown(self):
        rmtree('test_output')

    def test_get_import_statement(self):
        expected = 'from foo.bar.baz.qux.knowledge.song import Song'
        actual = Song().get_import_statement('foo/bar/baz/qux')
        self.assertEqual(expected, actual)

    def test_get_import_statement_with_empty_path(self):
        expected = 'from knowledge.song import Song'
        actual = Song().get_import_statement()
        self.assertEqual(expected, actual)

    def test_get_relation_import_statement(self):
        expected = 'from foo.bar.baz.qux.knowledge.relation import Relation'
        actual = get_relation_import_statement('foo/bar/baz/qux')
        self.assertEqual(expected, actual)

    def test_get_relation_import_statement_with_empty_path(self):
        expected = 'from knowledge.relation import Relation'
        actual = get_relation_import_statement()
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

    def test_get_concept_type(self):
        self.assertEqual('Thing', Adele().get_concept_type())
        self.assertEqual('Category', Singer().get_concept_type())

    def test_write_concept(self):
        adele1 = Adele()
        adele1.write('test_output/adele2')
        from test_output.adele2.knowledge.adele import Adele as Adele2
        adele2 = Adele2()
        self.assertEqual('Adele', adele2.get_lexical_form())

    # TODO: I've sort of recapped other tests here
    # I guess it would be neater to export a populator and then somehow
    # run all the unit tests on the new package
    # (everything about this project eats its own tail)
    def test_write_relation(self):
        write_relation('test_output/relation2')
        from test_output.relation2.knowledge.relation \
            import Relation as Relation2
        adele = Adele()
        adele_singer = Relation2('is_a', (adele, Singer()))
        self.assertEqual(adele_singer, adele_singer)
        adele_song = Relation('wrote_a', (adele, Song()))
        self.assertTrue(adele_singer < adele_song)
        from test_output.relation2.knowledge.relation \
            import has_lexical_form as has_lexical_form2
        self.assertTrue(has_lexical_form2(adele_singer, 'Adele'))
        from test_output.relation2.knowledge.relation \
            import get_relation_import_statement \
            as get_relation_import_statement2
        expected = 'from foo.bar.baz.qux.knowledge.relation import Relation'
        actual = get_relation_import_statement2('foo/bar/baz/qux')
        self.assertEqual(expected, actual)

    def test_export_populator(self):
        knowledge_base1 = KnowledgeBase()
        KnowledgeBasePopulator.populate(knowledge_base1)

        knowledge_base1.export_populator('test_output/iteration2')
        from test_output.iteration2.knowledge.knowledge_base_populator \
            import KnowledgeBasePopulator as KnowledgeBasePopulator2
        knowledge_base2 = KnowledgeBase()
        KnowledgeBasePopulator2.populate(knowledge_base2)
        self.assertTrue(knowledge_base1.matches(knowledge_base2))
        
        knowledge_base2.export_populator('test_output/iteration3')
        from test_output.iteration3.knowledge.knowledge_base_populator \
            import KnowledgeBasePopulator as KnowledgeBasePopulator3
        knowledge_base3 = KnowledgeBase()
        KnowledgeBasePopulator3.populate(knowledge_base3)
        self.assertTrue(knowledge_base1.matches(knowledge_base3))

