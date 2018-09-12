import unittest
from utils.paths import to_package_path
from os.path import join


class TestUtils(unittest.TestCase):
    def test_to_package_path_default_behaviour(self):
        self.assertEqual('', to_package_path(''))

        directory_path = join('foo', 'bar', 'baz')
        self.assertEqual('foo.bar.baz', to_package_path(directory_path))

    def test_to_package_path_with_final_dot(self):
        self.assertEqual('', to_package_path('', final_dot=True))

        expected = 'foo.bar.baz.'
        actual = to_package_path(join('foo', 'bar', 'baz'), final_dot=True)
        self.assertEqual(expected, actual)

