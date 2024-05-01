'''
Fund (:mod:`FundAnalyser.MarketData.Fund`)
==========================================

.. currentmodule:: FundAnalyser.MarketData.Fund

The :mod:`FundAnalyser.MarketData.Fund` contains a fund class

.. autoclass:: Fund

'''


from numpy import double, void
from FundAnalyser.MarketData.MarketDataHelper import MarketDataHelper
import FundAnalyser.Globals.Variables as gv
import string


class Fund:
    '''
    Data Members
    ------------
    ISIN: string
    fullName: string
    dataHelper: MarketDataHelper
    indicators: dict
    '''
    ISIN: string
    fullName: string
    dataHelper: MarketDataHelper
    indicators: dict
    
    def __init__(self, _ISIN, _fullName, _units=123):
        self.indicators = {}
        self.ISIN = _ISIN
        self.fullName = _fullName
        self.units = _units
        self.dataHelper = None
        
    def SetIndicators(self, _mean: double, _absGrowth: double, _growthOnMean: double, _volatility: double) -> void:
        '''Sets the calculated indicators on the Fund'''
        self.indicators[gv.MEAN] = _mean
        self.indicators[gv.ABS_GROWTH] = _absGrowth
        self.indicators[gv.GROWTH_MEAN] = _growthOnMean
        self.indicators[gv.VOL] = _volatility
        self.indicators[gv.UNITS] = self.units
        self.indicators[gv.AVE_VALUE] = self.units * _mean / 100
            
    def setDataHelper(self, _dataHelper: MarketDataHelper) -> void:
        '''Sets the :class:`FundAnalyser.MarketData.MarketDataHelper`'''
        self.dataHelper = _dataHelper
