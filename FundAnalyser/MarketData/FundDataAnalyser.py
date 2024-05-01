'''
FundAnalyser (:mod:`FundAnalyser.MarketData.FundDataAnalyser`)
==============================================================

.. currentmodule:: FundAnalyser.MarketData.FundDataAnalyser

The :mod:`FundAnalyser.MarketData.FundDataAnalyser` calculates indicators for the fund
        
.. autoclass:: FundAnalyser

'''


from numpy import double, void
from pandas import DataFrame, Series
from FundAnalyser.MarketData.Fund import Fund
from FundAnalyser.Globals import Variables as gv


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
        '''
        Growth between start and end date
        '''
        first = self.closeData[0]
        last = self.closeData[self.closeData.size - 1]
        return (last - first) / last * 100
    
    def GetGrowthOnMean(self) -> double:
        '''
        Calcualtes the growth on the mean
        '''
        last = self.closeData[self.closeData.size - 1]
        return (last - self.closeMean) / last * 100

    def AddRollingAverage(self) -> void:
        '''
        Calculates 5 and 10 day rolling average
        '''
        self.data['MA5'] = self.closeData.rolling(window=5).mean()
        self.data['MA10'] = self.closeData.rolling(window=5).mean()
     
    def GetVolatility(self) -> double:
        '''
        Calcualtes the volatility over the reporting period
        '''
        points = self.closeData
        vol = 0
        for point in points:
            vol += (point - self.closeMean)**2
        vol = vol / (self.closeData.size - 1)  # Use N-1 for an unbiased estimator
        volatility = vol**0.5  # Take the square root to get the standard deviation
        return volatility
