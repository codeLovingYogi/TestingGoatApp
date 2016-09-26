from selenium import webdriver
#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        # caps = DesiredCapabilities.FIREFOX
        # caps["marionette"] = True
        # caps["binary"] = "/usr/bin/firefox"
        # browser = webdriver.Firefox(capabilities=caps)
        self.browser = webdriver.PhantomJS()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_list_and_retrieve_it_later(self):
        # User goes to homepage
        self.browser.get('http://localhost:8000')
        self.browser.implicitly_wait(3)

        # User sees from page title and header this is a to-do list
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish this test')

        # User invited to enter a to-do item

        # User types 'Buy milk' into text box

        # User clicks Enter and page updates, page lists '#1: Buy milk' as a to-do item

        # Text box is still there to invite user to add another to-do item. User enters 'Pay bills'

        # Page updates again and two to-do items show up on list

        # User tries to save to-do list and looks for unique URL to save page

        # User tries to go access her to-do list

        # User leaves page to work on her tasks

if __name__ == '__main__':
    unittest.main()

