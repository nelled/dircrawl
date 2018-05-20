import unittest

from helpers.helpers import prepare_url, read_word_list


class HelpersTest(unittest.TestCase):

    def test_prepare_url(self):
        url = 'www.foo.com'
        self.assertFalse(url[-1] == '/')
        self.assertTrue(prepare_url(url)[-1] == '/')

    def test_read_word_list(self):
        words = read_word_list('../fixtures/test_wordfile.txt')
        test_str_a = 'thislineshouldbeincluded'
        test_str_b = 'thisaswell'
        self.assertEqual(2, len(words))
        self.assertTrue(test_str_a in words)
        self.assertTrue(test_str_b in words)
