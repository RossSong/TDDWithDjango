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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'task item input'
        )

        # She add task
        # Whe input 'bye feather'
        inputbox.send_keys('buy feathers')
        inputbox.send_keys(Keys.ENTER)

        # When she hit enter key, '1: bye feather' item is added
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
                any(row.text == '1: buy feathers' for row in rows),
        )

        self.fail('Finish the test!')

# There is extra input text field and add 'make web with feather'
# Page is reloaded and there are two items
# Edis is wondering if the web site save items
# Site make URL for her
# description for URL is provieded together.

# She can check if the list exists.
# She fall a sleep with satisfaction

if __name__ == '__main__':
    unittest.main(warnings='ignore')
