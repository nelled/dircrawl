import unittest

from helpers.helpers import read_word_list
from url_generator import UrlGenerator


class UrlGeneratorTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.url = 'www.foo.com'
        cls.words = read_word_list('../fixtures/test_wordfile.txt')

    def test_generate_urls(self):
        url_generator = UrlGenerator(UrlGeneratorTest.url, UrlGeneratorTest.words)
        urls = [url for url in url_generator.generate_urls()]
        test_str_a = 'www.foo.com/thislineshouldbeincluded'
        test_str_b = 'www.foo.com/thisaswell'
        self.assertEqual(2, len(urls))
        self.assertTrue(test_str_a in urls)
        self.assertTrue(test_str_b in urls)
