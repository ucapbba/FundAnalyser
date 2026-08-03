from dataclasses import dataclass, field
from numpy import double, void
from MarketData.MarketDataHelper import MarketDataHelper
import Globals.Variables as gv
import string


@dataclass(kw_only=True)
class Fund:
    ISIN: string
    fullName: string
    units: double = 123
    indicators: dict = field(default_factory=dict, init=False)
    dataHelper: MarketDataHelper = field(default=None, init=False)

    def SetIndicators(self, _mean: double, _absGrowth: double, _growthOnMean: double, _volatility: double) -> void:
        self.indicators[gv.MEAN] = _mean
        self.indicators[gv.ABS_GROWTH] = _absGrowth
        self.indicators[gv.GROWTH_MEAN] = _growthOnMean
        self.indicators[gv.VOL] = _volatility
        self.indicators[gv.UNITS] = self.units
        self.indicators[gv.AVE_VALUE] = self.units * _mean / 100

    def setDataHelper(self, _dataHelper: MarketDataHelper) -> void:
        self.dataHelper = _dataHelper
