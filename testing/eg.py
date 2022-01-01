import unittest
class TestCaseDemo(unittest.TestCase):
    def setUp(self):
        print('setUp method')
    def test(self):
        print('test method')
    def tearDown(self):
        print('tearDown method')

unittest.TestCase()