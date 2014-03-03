import trie
import unittest


class TrieTests(unittest.TestCase):

    def setUp(self):
        self.trie = trie.Trie()

    def test_empty_trie(self):
        results = []
        self.trie.search('', results)
        self.assertEqual(results, [])

    def test_empty_query_returns_no_results(self):
        self.trie.add('Uber')

        results = []
        self.trie.search('', results)
        self.assertEqual(results, [])

    def test_adding_word(self):
        self.trie.add('Uber')

        results = []

        self.trie.search('U', results)
        self.assertTrue('Uber' in results)

        self.trie.search('Ub', results)
        self.assertTrue('Uber' in results)

        self.trie.search('Ube', results)
        self.assertTrue('Uber' in results)

        self.trie.search('Uber', results)
        self.assertTrue('Uber' in results)

    def test_adding_duplicate_word(self):
        self.trie.add('Uber')

        results = []
        self.trie.search('U', results)
        self.assertTrue('Uber' in results)

        results = []
        self.trie.search('Ub', results)
        self.assertTrue('Uber' in results)

        results = []
        self.trie.search('Ube', results)
        self.assertTrue('Uber' in results)

        results = []
        self.trie.search('Uber', results)
        self.assertTrue('Uber' in results)

        self.trie.add('Uber')

        results = []
        self.trie.search('U', results)
        self.assertTrue('Uber' in results)
        self.assertEqual(len(results), 1)

        results = []
        self.trie.search('Ub', results)
        self.assertTrue('Uber' in results)
        self.assertEqual(len(results), 1)

        results = []
        self.trie.search('Ube', results)
        self.assertTrue('Uber' in results)
        self.assertEqual(len(results), 1)

        results = []
        self.trie.search('Uber', results)
        self.assertTrue('Uber' in results)
        self.assertEqual(len(results), 1)

    def test_searching_for_words_with_same_prefix_returns_all_words(self):
        self.trie.add('Uber')
        self.trie.add('Umbrella')
        self.trie.add('Unicorn')

        results = []
        self.trie.search('U', results)

        self.assertTrue('Uber' in results)
        self.assertTrue('Umbrella' in results)
        self.assertTrue('Unicorn' in results)

    def test_adding_word_with_unicode_char(self):
        self.trie.add('\xc3ber')

        results = []
        self.trie.search('\xc3', results)
        self.assertTrue('\xc3ber' in results)

        results = []
        self.trie.search('\xc3b', results)
        self.assertTrue('\xc3ber' in results)

        results = []
        self.trie.search('\xc3b', results)
        self.assertTrue('\xc3ber' in results)

        results = []
        self.trie.search('\xc3be', results)
        self.assertTrue('\xc3ber' in results)

        results = []
        self.trie.search('\xc3ber', results)
        self.assertTrue('\xc3ber' in results)


if __name__ == '__main__':
    unittest.main()
