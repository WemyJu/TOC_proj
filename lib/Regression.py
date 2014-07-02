from numpy import *
import statsmodels.api as sm


class Regression():
    def __init__(self):
        self.statData = array([])
        self.totalPrice = array([])
        self.parameters = array([])
        self.resultSummary = ""
        self.houseIndices = {}
        self.getHouseIndex()

    def getHouseIndex(self):
        f = open('res/房價指數.txt', 'r')
        line = f.readline()
        cityName = line.strip().split('\t')
        for i in range(1, 8, 1):
            self.houseIndices.update({cityName[i]:{}})
        while True:
            line = f.readline()
            if line == "":
                break
            tempList = line.strip().split('\t')
            season = tempList[0]
            for i in range(1, 8, 1):
                self.houseIndices[cityName[i]].update({season:tempList[i]})
        #print(self.houseIndices)
        f.close()

    def quantize(self, rawRecord, city):
        const = 1
        year = int(rawRecord['交易年月']/100)
        if year < 99 or year > 103:
            return
        season = int(rawRecord['交易年月']%100/4+1)
        season = str(year)+"Q"+str(season)
        if city in self.houseIndices:
            x1 = float(self.houseIndices[city][season])
        else:
            x1 = float(self.houseIndices['全國'][season])
        x2 = (rawRecord['有無管理組織'] == '有')
        x3 = rawRecord['土地移轉總面積平方公尺']
        x4 = rawRecord['車位移轉總面積平方公尺']
        x5 = rawRecord['建物移轉總面積平方公尺']

        if rawRecord['建築完成年月'] is not None:
            houseAge = 1031231 - rawRecord['建築完成年月']
            x6 = int((houseAge/10000)*12) + int((houseAge % 10000)/100)
        else:
            houseAge = 10312 - rawRecord['交易年月']
            x6 = int(houseAge/100*12) + int(houseAge % 100)
        x7 = (rawRecord['建物型態'] == '住宅大樓(11層含以上有電梯)')
        x8 = (rawRecord['建物型態'] == '套房(1房1廳1衛)')
        x9 = (rawRecord['建物型態'] == '華廈(10層含以下有電梯)')
        x10 = (rawRecord['建物型態'] == '公寓(5樓含以下無電梯)')
        x11 = (rawRecord['建物型態'] == '透天厝')
        x12 = (rawRecord['建物型態'] == '店面(店鋪)')
        y = rawRecord['總價元']

        if len(self.statData):
            self.statData = vstack((self.statData, [const, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12]))
        else:
            self.statData = array([const, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12])

        if len(self.totalPrice):
            self.totalPrice = hstack((self.totalPrice, [y]))
        else:
            self.totalPrice = array([y])

    def countRegression(self):
        if len(self.totalPrice) > 5:
            self.statData = sm.add_constant(self.statData, prepend=False)
            model = sm.OLS(self.totalPrice, self.statData)
            results = model.fit()
            print(results.summary())
            self.resultSummary = results.summary()
            self.parameters = results.params
            #print(self.parameters)
            return True
        else:
            return False

    def getParameters(self):
        return self.parameters

    def getRrsultSummary(self):
        return self.resultSummary
