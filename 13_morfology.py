import xml.etree.ElementTree as ET
import unittest

tree = ET.parse('morfology.xml')
root = tree.getroot()


class Corpus:

    def __init__(self, path_to_file):
        self._sentences = []

    def load(self):
        for sent in root.findall("text/paragraphs/paragraph/sentence"):
            words = []
            sent_str = sent.find('source').text
            for token in sent.find('tokens'):
                token_str = token.attrib['text']
                token_gr = []
                for gr in token.findall('tfr/v/l/g'):
                    token_gr.append(gr.attrib['v'])
                word = Wordform(token_str, token_gr)
                words.append(word)
            sentence = Sentence(sent_str, words)
            self._sentences.append(sentence)

    def get_sentences(self):
        return self._sentences

    def i_sent(self, num_sent):
        return self._sentences[num_sent]

    def show_sent(self, num_sent):
        sentence = self.i_sent(num_sent)
        return sentence.get_str_sent()

    def i_word(self, num_sent, num_word):
        return self.i_sent(num_sent).get_word(num_word)

    def show_word(self, num_sent, num_word):
        word = self.i_word(num_sent, num_word)
        return word.get_str_word()

    def show_gr(self, num_sent, num_word, num_gr):
        return self.i_word(num_sent, num_word).get_gr(num_gr)


class Sentence:
    def __init__(self, sent_str, words):
        self._sent = sent_str
        self._words = words

    def get_word(self, i):
        return self._words[i]

    def get_str_sent(self):
        return self._sent

    def get_words(self):
        return self._words


class Wordform:
    def __init__(self, word_str, list_gr):
        self._word = word_str
        self._gram = list_gr

    def get_gr(self, i):
        return self._gram[i]

    def get_str_word(self):
        return self._word

    def get_grams(self):
        return self._gram


class TestCorpus(unittest.TestCase):
    def setUp(self):
        self.test_corp = Corpus("morfology.xml")
        self.test_corp.load()

    def test_instances(self):
        for sentence in self.test_corp.get_sentences():
            with self.subTest(sentence=sentence):
                self.assertTrue(isinstance(sentence, Sentence))

            for word in sentence.get_words():
                with self.subTest(word=word):
                    self.assertTrue(isinstance(word, Wordform))

    def test_gram(self):
        for token, word in zip(root.find("text/paragraphs/paragraph/sentence/tokens"),
                               self.test_corp.i_sent(0).get_words()):
            with self.subTest(token=token, word=word):
                grams = [gram.attrib['v'] for gram in token.findall('tfr/v/l/g')]
                test_grams = word.get_grams()
                self.assertEqual(test_grams, grams)


if __name__ == '__main__':
    unittest.main()
