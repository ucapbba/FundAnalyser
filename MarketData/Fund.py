from numpy import double, void
from MarketData.MarketDataHelper import MarketDataHelper
import string


class Fund:
    ISIN: string
    fullName: string
    dataHelper: MarketDataHelper
    indicators: dict
    
    def __init__(self, _ISIN, _fullName):
        self.indicators = {}
        self.ISIN = _ISIN
        self.fullName = _fullName
        self.dataHelper = None
        
    def SetIndicators(self, _mean: double, _absGrowth: double, _growthOnMean: double, _volatility: double,) -> void:
        self.indicators["mean"] = _mean
        self.indicators["absGrowth"] = _absGrowth
        self.indicators["growthOnMean"] = _growthOnMean
        self.indicators["volatility"] = _volatility
            
    def setDataHelper(self, _dataHelper: MarketDataHelper) -> void:
        self.dataHelper = _dataHelper
