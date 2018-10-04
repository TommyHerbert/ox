from importlib import import_module
import unittest
from utils.knowledge import create_unique_package, copy_knowledge_package
from utils.paths import to_package_path
from knowledge.myself import Myself
from knowledge.song import Song
from knowledge.adele import Adele
from knowledge.singer import Singer
from knowledge.knowledge_base import KnowledgeBase
from knowledge.knowledge_base_populator import KnowledgeBasePopulator
from knowledge.relation import get_relation_import_statement, \
                               write_relation, \
                               Relation
from os import mkdir, environ
from os.path import join
from pathlib import Path
from shutil import rmtree

SOURCE_PATH_KEY = 'OX_SOURCE_PATH'


class TestSelfWriting(unittest.TestCase):
    def setUp(self):
        mkdir('test_output')
        Path('test_output/__init__.py').touch()

    def tearDown(self):
        rmtree('test_output')

    def test_get_import_statement(self):
        expected = 'from foo.bar.baz.qux.knowledge.song import Song'
        actual = Song().get_import_statement('foo/bar/baz/qux/knowledge')
        self.assertEqual(expected, actual)

    def test_get_import_statement_with_empty_path(self):
        expected = 'from song import Song'
        actual = Song().get_import_statement()
        self.assertEqual(expected, actual)

    def test_get_relation_import_statement(self):
        expected = 'from foo.bar.baz.qux.knowledge.relation import Relation'
        actual = get_relation_import_statement('foo/bar/baz/qux/knowledge')
        self.assertEqual(expected, actual)

    def test_get_relation_import_statement_with_empty_path(self):
        expected = 'from relation import Relation'
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

    def test_overwrite_copy(self):
        create_dummy_thing_class('test_output')
        Adele().overwrite_copy('test_output')
        from test_output.adele import Adele as Adele2
        self.assertEqual('Adele', Adele2().lexical_form)

    def test_export_populator(self):
        knowledge_base1 = KnowledgeBase()
        KnowledgeBasePopulator.populate(knowledge_base1)
        new_relation = Relation('likes', (Myself(), Adele(), 1000))
        knowledge_base1.relations.append(new_relation)
        knowledge_base2 = generate_copy(knowledge_base1, 'test_output')
        self.assertTrue(knowledge_base1.matches(knowledge_base2))
        knowledge_base3 = generate_copy(knowledge_base2, 'test_output')
        self.assertTrue(knowledge_base1.matches(knowledge_base3))


def create_dummy_thing_class(path):
    with open(join(path, 'concept.py'), 'w') as f:
        f.write('class Thing:\n    pass\n')

 
def generate_copy(knowledge_base, path):
    unique_id = create_unique_package(path)
    source_path = environ[SOURCE_PATH_KEY]
    copy_knowledge_package(source_path, join(path, unique_id))
    knowledge_directory_path = join(path, unique_id, 'knowledge')
    knowledge_base.export_populator(knowledge_directory_path)
    populator_module_path = to_package_path(knowledge_directory_path) + \
                            '.knowledge_base_populator'
    populator_module = import_module(populator_module_path)
    knowledge_base_copy = KnowledgeBase()
    populator_module.KnowledgeBasePopulator.populate(knowledge_base_copy)
    return knowledge_base_copy

