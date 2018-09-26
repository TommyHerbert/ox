import unittest
from utils.paths import to_package_path
from utils.lists import sorted_copy
from utils.knowledge import create_knowledge_package
from os.path import join


class TestUtils(unittest.TestCase):
    def setUp(self):
        # 'utils_test_output'
        pass # TODO

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
        pass # TODO
