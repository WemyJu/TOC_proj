import os
import sys
import subprocess
import pickle
import numpy
from distutils.util import strtobool
from lib.Regression import Regression


inputTitle = ['縣市', '鄉鎮市區',
              '有無管理組織', '建物型態',
              '土地移轉總面積平方公尺', '車位移轉總面積平方公尺', '建物移轉總面積平方公尺',
              '建築完成年月', '交易年月']


def readRegressions(path="regression_output/.regressions"):
    if not os.path.isfile(path):
        cmd = ["python3", "regression_generator.py"]
        p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        p.communicate()

    f = open(path, "rb")
    regressions = pickle.load(f)
    f.close()
    return regressions


def yesNoQuery(question):
    print(question, end = "\t")
    while True:
        try:
            return strtobool(input().lower())
        except ValueError:
            print ("Please repond with y or n")


def isfloat(inStr):
    try:
        float(inStr)
        return True
    except ValueError:
        return False


def handleInputType(inStr):
    if inStr.isnumeric():
        inStr = int(inStr)
    elif isfloat(inStr):
        inStr = float(inStr)
    return inStr


def userInput():
    inputVars = dict()

    global inputTitle
    for title in inputTitle:
        inputVars[title] = handleInputType(input(title + ":"))
    return inputVars


def fileInput(path):
    inputVars = dict()

    global inputTitle
    try:
        f = open(path, "r")

        for line, title in zip(f.read().splitlines(), inputTitle):
            inputVars[title] = handleInputType(line)

        if len(inputVars) != len(inputTitle):
            print ("Your input file contains wrong parameter numbers!!!")
            sys.exit(0)
    except FileNotFoundError:
        print ("Your input file does not exist!!!")
        sys.exit(0)
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


def predict(var, regs):
    city = var['縣市']
    region = var['鄉鎮市區']

    coefficient = regs[city][region]
    y = numpy.dot(var["variables"], coefficient)
    return y


if __name__ == '__main__':
    if yesNoQuery("Input from file? [y/n]"):
        path = input("Please input path of your file: ")
        inputVars = fileInput(path)
    else:
        inputVars = userInput()

    quantizedVars = quantize(inputVars)

    regressions = readRegressions()
    predictedPrice = predict(quantizedVars, regressions)
    print ("The predicted price is : ", predictedPrice)

    if yesNoQuery("Output regression report? [y/n]"):
        path = "./regression_output/report/"
        if os.path.isfile(path + quantizedVars["縣市"]):
            path += quantizedVars["縣市"] + "/"
            if os.path.isfile(path + quantizedVars["鄉鎮市區"]):
                path += quantizedVars["鄉鎮市區"] + "/" + quantizedVars["鄉鎮市區"] + ".txt"
            else:
                path += quantizedVars["縣市"] + ".txt"
        else:
            path += "total.txt"

        f = open(path)
        print (f.read())
        f.close()
