import unittest
import os
import sys
sys.path.append(os.path.join('../lib'))
from myStatistics import MyStatistics


class outputTest(unittest.TestCase):
    def test_getFieldStdev(self):
        ms = MyStatistics()
        self.assertEqual(ms.getFieldStdev([1,1,1], None), 0, "getFieldStdev error")

    def test_getFieldMean(self):
        ms = MyStatistics()
        self.assertEqual(ms.getFieldMean([1, 2, 3], None), 2, "getFieldMean error")


if __name__ == '__main__':
    unittest.main()
