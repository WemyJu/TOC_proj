import re
from operator import itemgetter
from lib.DataGarageAPI import DataGarageAPI
from lib.myStatistics import MyStatistics

Block = {}


if __name__ == '__main__':
    dgAPI = DataGarageAPI()
    dgAPI.setDataID('5365dee31bc6e9d9463a0057')
    data = dgAPI.getRawData()

    for datum in data:
        reResult = re.findall("^\S\S(?:市|縣)", datum['土地區段位置或建物區門牌'])

        if reResult:
            reResult = reResult[0]
            if reResult not in Block:
                Block[reResult] = [datum]
            else:
                Block[reResult].append(datum)

    # for firstLevel in Block:
        # reResult = re.findall(datum)
    for k in Block:
        Block[k] = sorted(Block[k], key=itemgetter("總價元"), reverse=False)

    ms = MyStatistics()

    tmp = []
    for key in Block:
        tmp.append([key, ms.getFieldMean(Block[key], '總價元')])
    tmp = sorted(tmp, key=itemgetter(1))

    for t in tmp:
        print (t)
