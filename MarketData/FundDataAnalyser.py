from numpy import double, void
from pandas import DataFrame, Series
from MarketData.Fund import Fund
from Globals import Variables as gv


class FundAnalyser:
    fund: Fund
    data: DataFrame
    closeData: Series
    closeMean: double

    def __init__(self, _fund: Fund):
        self.fund = _fund
        self.data = _fund.dataHelper.GetDataFrame()
        self.closeData = self.data[gv.close]
        self.closeMean = self.closeData.mean()
    
    def GetAbsGrowth(self) -> double:
        first = self.closeData[0]
        last = self.closeData[self.closeData.size - 1]
        return (last - first) / last * 100
    
    def GetGrowthOnMean(self) -> double:
        last = self.closeData[self.closeData.size - 1]
        return (last - self.closeMean) / last * 100

    def AddRollingAverage(self) -> void:
        self.data['MA5'] = self.closeData.rolling(window=5).mean()
        self.data['MA10'] = self.closeData.rolling(window=5).mean()
     
    def GetVolatility(self) -> double:
        points = self.closeData
        vol = 0
        for point in points:
            vol += (point - self.closeMean)**2
        vol = vol / self.closeData.size
        return vol
