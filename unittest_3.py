import os
import shutil
import unittest


class TestDirectory(unittest.TestCase):
    def setUp(self):
        self.dir_path = '/path/to/new/folder'
        os.makedirs(self.dir_path)
        with open(self.dir_path+'/test.txt', 'w') as f:
            f.write('This is a test file')

    def test_file_contents(self):
        with open(self.dir_path+'/test.txt', 'r') as f:
            contents = f.read()
            self.assertNotEqual(contents, '')
            self.assertIn('test', contents)

    def tearDown(self):
        shutil.rmtree(self.dir_path)


if __name__ == '__main__':
    unittest.main()
