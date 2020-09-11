import re
import unittest

class TestRegularExpressions (unittest.TestCase):

    def setUp(self):
        self.bigText = '''
The COVID‑19 pandemic!, also known as the coronavirus pandemic, is an ongoing pandemic of coronavirus disease 2019 (COVID‑19) caused by severe acute respiratory syndrome coronavirus 2 (SARS‑CoV‑2).[1] It was first identified in December 2019 in Wuhan, China.[4] The World Health Organization declared the outbreak a Public Health Emergency of International Concern on 30 January 2020 and a pandemic on 11 March.
As of 10 September 2020, more than 27.8 million cases have been reported in more than 188 countries and territories, resulting in more than 904,000 deaths; more than 18.7 million people have recovered.[5]

The virus is spread primarily via small droplets from coughing, sneezing, and talking. The droplets are usually not airborne, however those standing in close proximity may inhale them and become infected.[b] People may also become infected by touching a contaminated surface and then touching their face. The transmission may also occur through aerosols that can stay suspended in the air for longer periods of time in enclosed spaces. It is most contagious during the first three days after the onset of symptoms, although spread is possible before symptoms appear, and from people who are asymptomatic.[6][7]
Common symptoms include fever, cough, fatigue, shortness of breath or breathing difficulties, and loss of smell. Complications may include pneumonia and acute respiratory distress syndrome. The incubation period is typically around five days but may range from two to 14 days. There are several vaccine candidates in development, although none have completed clinical trials to prove their safety and efficacy. There is no known specific antiviral medication, so primary treatment is currently symptomatic.[8]
        '''
    
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

    def test_getAllDivInAngularBrackets(self):
        text = '''
            <div>
                <p> This is an Unordered list </p>
                <ul>
                    <li> First Item inside a <div </li>
                    <li> Second Item inside a div </li>
                    <li> Third Item inside a div/> </li>
                </ul>
            </div>
        ''' 
        match = re.findall(r'(?<=<)div(?=>)|(?<=<\/)div(?=>)', text)
        self.assertTrue(match[0] == 'div')
        self.assertTrue(match[1] == 'div')

    def test_getAllWordsThatStartsWithGivenLetterCaseInsensitive(self):
        match = re.findall(r'\bt\w+', self.bigText, re.IGNORECASE)
        self.assertEqual(len(match), 37)

    def test_substituteAllWordsStartingWithGivenCharacterPrecededByGivenSetOfCharacters(self):
        #Here we substitute all words starting with 'T' and preceded by '. ' with "Yeah"
        match = re.sub(r'(?<=\. )T\w+', 'Yeah', self.bigText)
        self.assertEqual(len(re.findall('Yeah', match)), 5)



if __name__ == '__main__':
    unittest.main()
