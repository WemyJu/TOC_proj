import os
import subprocess
import pickle
import numpy
from lib.Regression import Regression


def readRegressions(path="regression_output/.regressions"):
    if not os.path.isfile(path):
        cmd = ["python3", "regression_generator.py"]
        p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        p.communicate()

    f = open(path, "rb")
    regressions = pickle.load(f)
    f.close()
    return regressions


def userInput():
    inputVars = dict()
    inputVars['縣市'] = input('縣市')
    inputVars['鄉鎮市區'] = input('鄉鎮市區 : ')
    inputVars['有無管理組織'] = input('有無管理組織 : ')
    inputVars['建物型態'] = input('建物型態 : ')
    inputVars['土地移轉總面積平方公尺'] = float(input('土地移轉總面積平方公尺 : '))
    inputVars['車位移轉總面積平方公尺'] = float(input('車位移轉總面積平方公尺 : '))
    inputVars['建物移轉總面積平方公尺'] = float(input('建物移轉總面積平方公尺 : '))
    inputVars['建築完成年月'] = int(input('建築完成日期 : '))
    inputVars['交易年月'] = int(input('交易年月 : '))
    return inputVars


def quantize(data):
    city = data['縣市'][:3]
    region = data['鄉鎮市區']

    reg = Regression()
    result = dict()
    result['縣市'] = city
    result['鄉鎮市區'] = region
    result['variables'] = numpy.array(reg.quantizeForRec(data, city))
    return result


def estimate(var, regs):
    city = var['縣市']
    region = var['鄉鎮市區']

    coefficient = regs[city][region]
    y = numpy.dot(var["variables"], coefficient)
    return y


if __name__ == '__main__':
    inputVars = userInput()
    quantizedVars = quantize(inputVars)

    regressions = readRegressions()
    predictedPrice = estimate(quantizedVars, regressions)
    print ("The predicted price is : ", predictedPrice)
