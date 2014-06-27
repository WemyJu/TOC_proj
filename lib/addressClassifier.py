import re


class AddressClassifier():
    def __init__(self):
        self.firstLevelIdentifier = "^\S\S(?:市|縣)"
        self.classifiedData = {}

    def classify(self, data):
        for datum in data:
            firstLevel = re.findall(self.firstLevelIdentifier, datum['土地區段位置或建物區門牌'])

            if firstLevel:
                firstLevel = firstLevel[0]
                secondLevelIdentifier = firstLevel + datum['鄉鎮市區']

                secondLevel = re.findall(secondLevelIdentifier, datum['土地區段位置或建物區門牌'])

                if secondLevel:
                    secondLevel = secondLevel[0][3:]
                    print (firstLevel, secondLevel)

                    if firstLevel not in self.classifiedData:
                        self.classifiedData[firstLevel] = {secondLevel: [datum]}
                    elif secondLevel not in self.classifiedData[firstLevel]:
                        self.classifiedData[firstLevel][secondLevel] = [datum]
                    else:
                        self.classifiedData[firstLevel][secondLevel].append(datum)

    def getClassifiedData(self):
        return self.classifiedData
