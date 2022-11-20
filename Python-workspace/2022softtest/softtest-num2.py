import unittest

# from unittest_demo1 import loginDemo
# from unittest_demo2 import demo

suite1 = unittest.defaultTestLoader.discover('./Case','unittest_demo*.py')

# suite = unittest.TestSuite()
runner = unittest.TextTestRunner()

# suite.addTest(unittest.makeSuite(loginDemo))
# suite.addTest(unittest.makeSuite(demo))

runner.run(suite1)