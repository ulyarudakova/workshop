from MORFOLOGY import *
import unittest


class TestCorpus(unittest.TestCase):
    def setUp(self):
        self.corpus = Corpus('morfology.txt')

    def test_corpus_size(self):
        expected_size = 1000
        actual_size = len(self.corpus.get_sentences())
        self.assertEqual(expected_size, actual_size)

    def test_word_in_sentence(self):
        sentence = self.corpus.i_sent(1)
        words = sentence.get_words()
        tokens = [word.get_str_word() for word in words]
        self.assertIn("язык", tokens)


if __name__ == '__main__':
    unittest.main()
