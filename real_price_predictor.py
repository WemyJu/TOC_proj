from lib.DataGarageAPI import DataGarageAPI
from lib.addressClassifier import AddressClassifier
# from operator import itemgetter
# from lib.myStatistics import MyStatistics

Block = {}


if __name__ == '__main__':
    dgAPI = DataGarageAPI()
    dgAPI.setDataID('5365dee31bc6e9d9463a0057') \
         .setSelector([['都市土地使用分區', '=', '住']]) \
         .setFields(['土地區段位置或建物區門牌', '鄉鎮市區',
                    '總價元', '有無管理組織', '建物型態',
                    '土地移轉總面積平方公尺', '車位移轉總面積平方公尺',
                    '建物移轉總面積平方公尺', '建物型態', '建築完成年月', '交易年月'])

    data = dgAPI.getFilteredData()

    ac = AddressClassifier()
    ac.classify(data)
    tempData = ac.getClassifiedData()
    for i in tempData:
        for j in tempData[i]:
            for k in tempData[i][j]:
                print (k)
