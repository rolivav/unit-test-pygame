from unittest import TestCase
from main import App

__author__ = 'Rodrigo'


class TestApp(TestCase):
    def test_on_init(self):
        theApp = App()
        self.assertRaises(Exception, theApp.__init__)