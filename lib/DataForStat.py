from numpy import *

class DataForStat():
	def __init__(self):
		self.statData = array([])

	def quantize(self, rawData)
		for city in rawData:
			#if city not in statData:
				#statData[city] = {}
			for block in rawData[city]:
				#if block not in statDaty[city]:
					#statData[city][block] = {}
				for record in rawData[city][block]:
					x1 = 0
					x2 = (record['有無管理組織'] == '有')
					x3 = record['土地轉移面積']
					x4 = record['車位轉移面積']
					x5 = record['建物轉移面積']
					if record['建築完成年月'] != None:
						houseAge = 1031231 - record['建築完成年月']
						x6 = (houseAge/10000)*12 + (houseAge%10000)/100
					else:
						houseAge = 10312 - record['交易年月']
						x6 = (houseAge/100)*12 + houseAge%100
					x7 = (record['建物型態'] == '住宅大樓(11層含以上有電梯)')
					x8 = (record['建物型態'] == '套房(1房1廳1衛)')
					x9 = (record['建物型態'] == '華廈(10層含以下有電梯)')
					x10 = (record['建物型態'] == '公寓(5樓含以下無電梯)')
					x11 = (record['建物型態'] == '透天厝')
					x12 = (record['建物型態'] == '店面(店鋪)')
					
					if len(self.statData):
						self.statData = vstack((self.statData, [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12]))
					else:
						self.statData = array([x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12])

	def getStatData(self):
		return self.statData
