import unittest
from utils.paths import to_package_path
from os.path import join

class TestUtils(unittest.TestCase):
    def test_to_package_path(self):
        directory_path = join('foo', 'bar', 'baz')
        self.assertEqual('foo.bar.baz', to_package_path(directory_path))
        self.assertEqual('', to_package_path(''))

