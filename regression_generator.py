import os
import sys
import pickle
from lib.DataGarageAPI import DataGarageAPI
from lib.addressClassifier import AddressClassifier
from lib.Regression import Regression


def parseData(URL="5365dee31bc6e9d9463a0057"):
    dgAPI = DataGarageAPI()
    dgAPI.setDataID(URL) \
         .setSelector([['都市土地使用分區', '=', '住']]) \
         .setFields(['土地區段位置或建物區門牌', '鄉鎮市區',
                     '總價元', '有無管理組織', '建物型態',
                     '土地移轉總面積平方公尺', '車位移轉總面積平方公尺',
                     '建物移轉總面積平方公尺', '建物型態', '建築完成年月', '交易年月'])
    return dgAPI.getFilteredData()


def outputRegressions(parameters, path="regression_output"):
    os.makedirs(path, exist_ok=True)
    outputReport(path)
    outputDict(path, parameters)


def outputReport(path):
    pass


def outputDict(path, parameters):
    f = open(path+"/.regressions", "wb")
    pickle.dump(parameters, f)
    f.close()


if __name__ == '__main__':
    data = parseData() if len(sys.argv) == 1 else parseData(sys.argv[1])

    ac = AddressClassifier()
    ac.classify(data)
    rawData = ac.getClassifiedData()

    print ("regression_generator start")
    reg = Regression()
    reg.quantize(rawData)
    parameters = reg.getTotalParams()

    outputRegressions(parameters)
    print ("regression_generator finish")
