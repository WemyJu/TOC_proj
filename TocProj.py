# from operator import itemgetter
from lib.DataGarageAPI import DataGarageAPI
# from lib.myStatistics import MyStatistics
from lib.addressClassifier import AddressClassifier

Block = {}


if __name__ == '__main__':
    dgAPI = DataGarageAPI()
    dgAPI.setDataID('5365dee31bc6e9d9463a0057') \
         .setSelector([['都市土地使用分區', '=', '住']])

    data = dgAPI.getFilteredData()

    ac = AddressClassifier()
    ac.classify(data)
    print (ac.getClassifiedData())
