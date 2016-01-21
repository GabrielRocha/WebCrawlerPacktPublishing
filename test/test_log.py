from unittest import TestCase
from log import write_log
import os

BASE_DIR = os.path.dirname(__file__)

class TestLog(TestCase):

    def tearDown(self):
        os.remove(os.path.join(BASE_DIR,'log'))

    def test_exist_log(self):
        write_log(BASE_DIR)
        self.assertTrue(os.path.isfile('log'))

    def test_write_log(self):
        write_log(BASE_DIR,'Python', 'Added')
        content_file = open(os.path.join(BASE_DIR,'log')).readlines()
        self.assertIn('Book: Python -- Status: Added', content_file[0])