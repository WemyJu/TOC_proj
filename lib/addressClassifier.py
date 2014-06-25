import re

class AddressClassifier():
    def __init__(self):
        self.firstLevelIdentifier = "^\S\S(?:市|線)"
        self.secondLevelIdentifier = ""

    def classify(self, data):
        reResult = re.findall(self.firstLevelIdentifier, datum['土地區段位置或建物區門牌'])

        if reResult:
            reResult = reResult[0]
            if reResult not in Block:
                Block[reResult] = [datum]
            else:
                Block[reResult].append(datum)
