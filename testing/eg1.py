import unittest
class TestCaseDemo(unittest.TestCase):
    def setUp(self):
        print('setUp method')
    def test_m1(self):
        print('test method1')
    def test_m2(self):
        print('test method2')
    def tearDown(self):
        print('tearDown method')

unittest.TestCase()