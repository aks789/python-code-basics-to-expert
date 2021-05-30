import unittest
import unit_testing.cap_test

class TestCap(unittest.TestCase):
    def test_one_word(self):
        text='python'
        result = unit_testing.cap_test.cap_text(text)
        self.assertEqual(result,'Python')

    def test_multiple_words(self):
        text='akshay akriti'
        result = unit_testing.cap_test.cap_text(text)
        self.assertEqual(result,'Akshay akriti')

    if __name__=='__main__':
        unittest.main()