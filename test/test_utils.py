import unittest
from utils.paths import to_package_path
from utils.lists import sorted_copy
from utils.knowledge import create_unique_package, \
                            create_empty_knowledge_package, \
                            copy_knowledge_package
from utils.case import phrase_to_headline
from os import makedirs
from os.path import join, exists, isdir, isfile
from shutil import rmtree

OUTPUT_DIR = 'utils_test_output'


class TestUtils(unittest.TestCase):
    def setUp(self):
        self.clear_output()

    def tearDown(self):
        self.clear_output()

    def clear_output(self):
        if exists(OUTPUT_DIR):
            rmtree(OUTPUT_DIR)

    def test_to_package_path_default_behaviour(self):
        self.assertEqual('', to_package_path(''))
        directory_path = join('foo', 'bar', 'baz')
        self.assertEqual('foo.bar.baz', to_package_path(directory_path))

    def test_to_package_path_with_final_dot(self):
        self.assertEqual('', to_package_path('', final_dot=True))
        expected = 'foo.bar.baz.'
        actual = to_package_path(join('foo', 'bar', 'baz'), final_dot=True)
        self.assertEqual(expected, actual)

    def test_sorted_copy(self):
        list1 = [3, 2, 1]
        list2 = sorted_copy(list1)
        self.assertEqual([3, 2, 1], list1)
        self.assertEqual([1, 2, 3], list2)

    def test_create_unique_package(self):
        path = join(OUTPUT_DIR, create_unique_package(OUTPUT_DIR))
        self.assertTrue(is_package(path))

    def test_create_empty_knowledge_package(self):
        path = join(OUTPUT_DIR, create_unique_package(OUTPUT_DIR))
        create_empty_knowledge_package(path)
        self.assertTrue(is_package(join(path, 'knowledge')))

    def test_copy_knowledge_package(self):
        source_path = join(OUTPUT_DIR, create_unique_package(OUTPUT_DIR))
        target_path = join(OUTPUT_DIR, create_unique_package(OUTPUT_DIR))
        create_empty_knowledge_package(source_path)
        source_knowledge_path = join(source_path, 'knowledge')
        with open(join(source_knowledge_path, 'file1.txt'), 'w') as sf1:
            sf1.write('foo')
        source_dir1_path = join(source_knowledge_path, 'dir1')
        makedirs(source_dir1_path)
        with open(join(source_dir1_path, 'file2.txt'), 'w') as sf2:
            sf2.write('bar')
        copy_knowledge_package(source_path, target_path)
        with open(join(target_path, 'knowledge', 'file1.txt')) as tf1:
            self.assertEqual('foo', tf1.read())
        with open(join(target_path, 'knowledge', 'dir1', 'file2.txt')) as tf2:
            self.assertEqual('bar', tf2.read())

    def test_phrase_to_headline(self):
        self.assertEqual('Adele', phrase_to_headline('Adele'))
        self.assertEqual('Song', phrase_to_headline('song'))
        self.assertEqual('ShapeOfYou', phrase_to_headline('Shape of You'))


def is_package(path):
    return isdir(path) and isfile(join(path, '__init__.py'))

