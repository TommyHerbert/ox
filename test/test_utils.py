import unittest
from utils.paths import to_package_path
from utils.lists import sorted_copy
from utils.knowledge import create_knowledge_package
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

    def test_create_knowledge_package(self):
        unique_id = create_knowledge_package(OUTPUT_DIR)
        path = join(OUTPUT_DIR, unique_id)
        self.assertTrue(is_package(path))
        self.assertTrue(is_package(join(path, 'knowledge')))


def is_package(path):
    return isdir(path) and isfile(join(path, '__init__.py'))

