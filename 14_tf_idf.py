import os
import math
import pickle
import unittest


class TFIDF:
    def __init__(self, corpus_path):
        self.corpus_path = corpus_path
        self.idf_values = {}
        self.load_idf()

    def load_idf(self):
        idf_file = 'idf_values.pickle'
        if os.path.isfile(idf_file):
            with open(idf_file, 'rb') as f:
                self.idf_values = pickle.load(f)
        else:
            self.calculate_idf()
            with open(idf_file, 'wb') as f:
                pickle.dump(self.idf_values, f)

    def calculate_idf(self):
        num_documents = 0
        word_counts = {}
        for root, dirs, files in os.walk(self.corpus_path):
            for file in files:
                if file.endswith('.txt'):
                    num_documents += 1
                    with open(os.path.join(root, file), 'r') as f:
                        words = set(f.read().split())
                        for word in words:
                            if word not in word_counts:
                                word_counts[word] = 1
                            else:
                                word_counts[word] += 1
        for word, count in word_counts.items():
            self.idf_values[word] = math.log(num_documents / count)

    def calculate_tf_idf(self, text):
        tf_values = {}
        words = text.split()
        for word in words:
            if word not in tf_values:
                tf_values[word] = 1
            else:
                tf_values[word] += 1
        max_tf = max(tf_values.values())
        tf_idf_values = {}
        for word, tf in tf_values.items():
            tf_idf_values[word] = tf / max_tf * self.idf_values.get(word, 0)
        return tf_idf_values



tfidf = TFIDF('morfology.xml')
text = 'Проди призывает граждан к возрождению страны.'
tfidf_values = tfidf.calculate_tf_idf(text)
print(tfidf_values)


class TestTFIDF(unittest.TestCase):
    def setUp(self):
        self.tfidf = TFIDF('corpus')

    def test_idf_values(self):
        self.assertAlmostEqual(self.tfidf.idf_values['sample'], 0.6931, places=4)
        self.assertAlmostEqual(self.tfidf.idf_values['testing'], 0.6931, places=4)

    def test_tf_idf_values(self):
        text = 'This is a sample text for testing TF-IDF'
        tfidf_values = self.tfidf.calculate_tf_idf(text)
        self.assertAlmostEqual(tfidf_values['sample'], 0.6931, places=4)
        self.assertAlmostEqual(tfidf_values['testing'], 0.6931, places=4)


if __name__ == '__main__':
    unittest.main()
