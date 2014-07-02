from numpy import *
import statsmodels.api as sm
import os
import sys

class Regression():
    def __init__(self):
        self.statData = {}
        self.totalPrice = {}
        self.parameters = {}
        self.resultSummary = {}
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
        f.close()

    def quantize(self, rawData):
        self.statData.update({'others':{'others':[]}})
        self.totalPrice.update({'others':{'others':[]}})
        for city in rawData:
            self.statData.update({city:{}})
            self.totalPrice.update({city:{}})
            self.statData[city].update({'others':[]})
            self.totalPrice[city].update({'others':[]})
            for block in rawData[city]:
                self.statData[city].update({block:[]})
                self.totalPrice[city].update({block:[]})
                for rawRecord in rawData[city][block]:
                    X = self.quantizeForRec(rawRecord, city)
                    Y = [rawRecord['總價元']]
                    
                    if len(X) > 0:
                        self.statData[city][block] = self.addArray(self.statData[city][block], X, vstack)
                        self.statData[city]['others'] = self.addArray(self.statData[city]['others'], X, vstack)
                        self.statData['others']['others'] = self.addArray(self.statData['others']['others'], X, vstack)
                        self.totalPrice[city][block] = self.addArray(self.totalPrice[city][block], Y, hstack)
                        self.totalPrice[city]['others'] = self.addArray(self.totalPrice[city]['others'], Y, hstack)
                        self.totalPrice['others']['others'] = self.addArray(self.totalPrice['others']['others'], Y, hstack)

        self.countRegression()


    def quantizeForRec(self, rawRecord, city):
        const = 1
        year = int(rawRecord['交易年月']/100)
        if year < 99 or year > 103:
            return []
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
                
        return [const, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12]
            
    def addArray(self, ori_array, new_array, method):
        if len(ori_array):
            return method((ori_array, new_array))
        else:
            return new_array

    def countRegression(self):
        for city in self.statData:
            self.parameters.update({city:{}})
            self.resultSummary.update({city:{}})
            for block in self.statData[city]:
                if len(self.totalPrice[city][block]) > 8:
                    self.parameters[city].update({block:[]})
                    self.resultSummary[city].update({block:[]})
                    model = sm.OLS(self.totalPrice[city][block], self.statData[city][block])
                    results = model.fit()
                    self.resultSummary[city][block] = results.summary()
                    self.parameters[city][block] = results.params

#direct = 'regression_output/report/'+city+block
#                   if not os.path.exists(direct):
#                       os.makedirs(direct)

    def getTotalParams(self):
        return self.parameters

    def getParameters(self, city, block):
        if city in self.parameters:
            if block in self.parameters[city]:
                return self.parameters[city][block]
            else:
                return self.parameters[city]['others']
        else:
            return self.parameters['others']['others']

    def getRrsultSummary(self, city, block):
        return self.resultSummary[city][block]
