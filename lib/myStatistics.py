import statistics

class MyStatistics():
    def __init__(self):
        pass

    def getFieldStdev(self, data, field = None):
        return statistics.stdev([datum[field] for datum in data]) if field is not None else statistics.stdev(data)

    def getFieldMean(self, data, field = None):
        return statistics.mean([datum[field] for datum in data]) if field is not None else statistics.mean(data)
