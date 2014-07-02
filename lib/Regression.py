from numpy import *
import statsmodels.api as sm

class Regression():
	def __init__(self):
		self.statData = array([])
		self.totalPrice = array([])
		self.parameters = array([])

	def quantize(self, rawRecord):
		x1 = 0
		x2 = (rawRecord['有無管理組織'] == '有')
		x3 = rawRecord['土地移轉總面積平方公尺']
		x4 = rawRecord['車位移轉總面積平方公尺']
		x5 = rawRecord['建物移轉總面積平方公尺']
		if rawRecord['建築完成年月'] != None:
			houseAge = 1031231 - rawRecord['建築完成年月']
			x6 = (houseAge/10000)*12 + (houseAge%10000)/100
		else:
			houseAge = 10312 - rawRecord['交易年月']
			x6 = (houseAge/100)*12 + houseAge%100
		x7 = (rawRecord['建物型態'] == '住宅大樓(11層含以上有電梯)')
		x8 = (rawRecord['建物型態'] == '套房(1房1廳1衛)')
		x9 = (rawRecord['建物型態'] == '華廈(10層含以下有電梯)')
		x10 = (rawRecord['建物型態'] == '公寓(5樓含以下無電梯)')
		x11 = (rawRecord['建物型態'] == '透天厝')
		x12 = (rawRecord['建物型態'] == '店面(店鋪)')
		y = rawRecord['總價元']
		
		if len(self.statData):
			self.statData = vstack((self.statData, [x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12]))
		else:
			self.statData = array([x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12])
			
		if len(self.totalPrice):
			self.totalPrice = hstack((self.totalPrice, [y]))
		else:
			self.totalPrice = array([y])
                            
	def countRegression(self):
		if len(self.totalPrice) > 5:
			self.statData = sm.add_constant(self.statData, prepend=False)
			model = sm.OLS(self.totalPrice, self.statData)
			results = model.fit()
			self.parameters = results.params
			print(self.parameters)
			return True
			#print(results.summary())
		else:
			return False

	def getParameters(self):
		print(self.parameters)
		return self.parameter
