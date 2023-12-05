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
        
    def SetIndicators(self, _volatility: double, _growth: double) -> void:
        self.indicators["volatility"] = _volatility
        self.indicators["growth"] = _growth
            
    def setDataHelper(self, _dataHelper: MarketDataHelper) -> void:
        self.dataHelper = _dataHelper
