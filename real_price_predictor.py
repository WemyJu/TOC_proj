import os
import sys
import subprocess
import pickle
import numpy
from distutils.util import strtobool
from lib.Regression import Regression


class userInterface():
    def __init__(self):
        self.inputTitle = ['縣市', '鄉鎮市區',
                           '有無管理組織', '建物型態',
                           '土地移轉總面積平方公尺', '車位移轉總面積平方公尺', '建物移轉總面積平方公尺',
                           '建築完成年月', '交易年月']
        self.defaultPath = "regression_output"
        self.regressions = dict()
        self.inputVars = dict()
        self.quantizedVars = dict()
        self.predictPrice = int()

        self.readRegressions()

    def readRegressions(self, path=None):
        path = self.defaultPath + "/.regressions" if path is None else 0
        if not os.path.isfile(path):
            print ("There is not regressions. Automatically generate.")
            cmd = ["python3", "regression_generator.py"]
            p = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            p.communicate()
            print ("Successfully generate!")

        f = open(path, "rb")
        self.regressions = pickle.load(f)
        f.close()

    def yesNoQuery(self, question):
        print(question, end = "\t")
        while True:
            try:
                return strtobool(input().lower())
            except ValueError:
                print ("Please repond with y or n")

    def __isfloat(self, inStr):
        try:
            float(inStr)
            return True
        except ValueError:
            return False

    def __handleInputType(self, inStr):
        if inStr.isnumeric():
            inStr = int(inStr)
        elif self.__isfloat(inStr):
            inStr = float(inStr)
        return inStr

    def userInput(self):
        for title in self.inputTitle:
            self.inputVars[title] = self.__handleInputType(input(title + ":"))

    def fileInput(self, path):
        try:
            f = open(path, "r")

            for line, title in zip(f.read().splitlines(), self.inputTitle):
                self.inputVars[title] = self.__handleInputType(line)

            if len(self.inputVars) != len(self.inputTitle):
                print ("Your input file contains wrong parameter numbers!!!")
                sys.exit(0)
        except FileNotFoundError:
            print ("Your input file does not exist!!!")
            sys.exit(0)

    def quantize(self):
        city = self.inputVars['縣市'][:3]
        region = self.inputVars['鄉鎮市區']

        reg = Regression()
        self.quantizedVars['縣市'] = city
        self.quantizedVars['鄉鎮市區'] = region
        self.quantizedVars['variables'] = numpy.array(reg.quantizeForRec(self.inputVars, city))
        return self

    def predict(self):
        city = self.quantizedVars['縣市']
        region = self.quantizedVars['鄉鎮市區']
        coefficient = self.regressions[city][region]
        self.predictedPrice = numpy.dot(self.quantizedVars["variables"], coefficient)

    def getPredictedPrice(self):
        return self.predictedPrice

    def outputReport(self):
        path = self.defaultPath + "/report/"
        city = self.quantizedVars["縣市"]
        region = self.quantizedVars["鄉鎮市區"]

        if os.path.isfile(path + city):
            path += city + "/"
            if os.path.isfile(path + region):
                path += region + "/" + region + ".txt"
            else:
                path += city + ".txt"
        else:
            path += "total.txt"
        f = open(path)
        print (f.read())
        f.close()


if __name__ == '__main__':
    ui = userInterface()

    if ui.yesNoQuery("Input from file? [y/n]"):
        path = input("Please input path of your file: ")
        ui.fileInput(path)
    else:
        ui.userInput()

    ui.quantize().predict()
    print ("The predicted price is : %f\n" % ui.getPredictedPrice())

    if ui.yesNoQuery("Output regression report? [y/n]"):
        ui.outputReport()
