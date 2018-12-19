from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome('chromedriver')
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')
       
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

# She add task
# Whe input 'bye feather'
# When she hit enter key, '1: bye feather' item is added
# There is extra input text field and add 'make web with feather'
# Page is reloaded and there are two items
# Edis is wondering if the web site save items
# Site make URL for her
# description for URL is provieded together.

# She can check if the list exists.
# She fall a sleep with satisfaction

if __name__ == '__main__':
    unittest.main(warnings='ignore')
