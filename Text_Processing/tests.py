import unittest
import csv

class testProcessor(unittest.TestCase):

    def setUp(self):
        self.csvfile = open('bookshelf.csv', newline='')

    def tearDown(self):
        self.csvfile.close()

    def test_csv_read(self):
        reader = csv.reader(self.csvfile, delimiter=',', quotechar='|')
        for row in reader:
            print(', '.join(row))

    def test_csv_DictReader(self):
        reader = csv.DictReader(self.csvfile)
        for row in reader:
            print('Title: '+row['Title'])




if __name__ == '__main__':
    unittest.main()
