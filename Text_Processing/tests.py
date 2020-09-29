import unittest
import csv
import json
import yaml


class testProcessor(unittest.TestCase):

    def test_csv_read(self):
        with open('bookshelf.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in reader:
                print(', '.join(row))

    def test_csv_DictReader(self):
        with open('bookshelf.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                print('Title: '+row['Title'])

    def test_json_read(self):
        with open('bookshelf.json') as jsonfile:
            dict_values = json.loads(jsonfile.read())
            print(dict_values)

    #def test_json_write(self):
    #    to_dump = {"Title": "Real and Complex Analysis", "Authors": ["Walter Rudin"], "Year of Production": 1987, "Publisher": "The McGraw-Hill Companies Inc.", "Edition": "Third"}
    #    strjson = {}
    #    with open('bookshelf.json', 'r') as jsonfile:
    #        strjson = json.load(jsonfile)
    #        strjson.append(to_dump)

    #    with open('bookshelf.json', 'w') as jsonfile:
    #        json.dump(strjson, jsonfile, indent=4)

    def test_read_yaml(self):
        with open('bookshelf.yml') as yamlfile:
            dict_values = yaml.load(yamlfile.read(), Loader=yaml.FullLoader)
            print(dict_values)

    def test_write_yaml(self):
        dict_to_write = {"Title": "Real and Complex Analysis", "Authors": ["Walter Rudin"], "Year of Production": 1987, "Publisher": "The McGraw-Hill Companies Inc.", "Edition": "Third"}
        dict_to_write_str = yaml.dump(dict_to_write, indent=4)
        with open('new_yaml.yml', 'w') as yamlfile:
            yamlfile.write(dict_to_write_str)


if __name__ == '__main__':
    unittest.main()
