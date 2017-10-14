#from unittest import TestCase

from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By

# Create your tests here.
class Kata_TDD_Test(TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()

    def test_title(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Busco Ayuda', self.browser.title)
