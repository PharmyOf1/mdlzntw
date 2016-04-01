# -*- coding: utf-8 -*-
from selenium import webdriver
from django.core.urlresolvers import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase  
import unittest
 
 
class NewVisitorTest(unittest.TestCase):
 
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
 
    def tearDown(self):
        self.browser.quit()
 
    def test_it_worked(self):
        self.browser.get('http://localhost:8000')
 
if __name__ == '__main__':
    unittest.main(warnings='ignore')