import re
import unittest

class TestRegularExpressions (unittest.TestCase):
    
    def test_getAllOccurrencies(self):
        text = "This is a test. Here we are going to \n extract the number of times that test appears. \n So we should get 3... test!"
        match = re.findall(r'\btest\b', text)
        self.assertTrue(len(match) == 3, "Something Wrong Here" )

    def test_getTheFirstCharacterOfEachLine(self):
        text =  "This is a test. Here we are going to\nextract the initial character of eache line.\nSo we should get [\'T\', \'e\', \'S\']"
        match = re.findall(r'^\w', text, re.MULTILINE)
        self.assertTrue(match[0] == 'T')
        self.assertTrue(match[1] == 'e')
        self.assertTrue(match[2] == 'S')

    def test_getLastCharacterOfEachLine(self):
        text = "This is a test. Here we are going to\nextract the last character of eache line.\nSo we should get [\'o\', \'.\',\']\']"
        match = re.findall(r'.$', text, re.MULTILINE)
        self.assertTrue(match[0] == 'o')
        self.assertTrue(match[1] == '.')
        self.assertTrue(match[2] == ']')
 

if __name__ == '__main__':
    unittest.main()
