import unittest
import os
import sys
sys.path.append(os.path.join('../lib'))
from addressClassifier import AddressClassifier
import json


class outputTest(unittest.TestCase):
    def test_classify(self):
        ac = AddressClassifier()

        f = open("./sample_data_for_AddressClassifier", "r")
        sampleData = json.loads(f.read())
        f.close()

        ac.classify(sampleData)
        self.assertEqual(len(ac.getClassifiedData()), 2, "classify error")
        self.assertEqual(len(ac.getClassifiedData()['臺北市']), 2, "classify error")
        self.assertEqual(len(ac.getClassifiedData()['臺北市']['文山區']), 9, "classify error")

if __name__ == '__main__':
    unittest.main()
