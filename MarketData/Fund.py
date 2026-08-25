from dataclasses import dataclass, field
from numpy import double, void
from MarketData.MarketDataHelper import MarketDataHelper
import Globals.Variables as gv


@dataclass(kw_only=True)
class Fund:
    isin: str
    full_name: str
    units: double = 1
    indicators: dict = field(default_factory=dict, init=False)
    data_helper: MarketDataHelper = field(default=None, init=False)
    market_cap: double = field(default=None, init=False)

    def set_indicators(self, mean: double, abs_growth: double, growth_on_mean: double, volatility: double) -> void:
        self.indicators[gv.MEAN] = mean
        self.indicators[gv.ABS_GROWTH] = abs_growth
        self.indicators[gv.GROWTH_MEAN] = growth_on_mean
        self.indicators[gv.VOL] = volatility
        self.indicators[gv.UNITS] = self.units
        self.indicators[gv.AVE_VALUE] = self.units * mean / 100
        if self.market_cap is not None:
            self.indicators[gv.MARKET_CAP] = self.market_cap

    def set_data_helper(self, data_helper: MarketDataHelper) -> void:
        self.data_helper = data_helper

    def set_market_cap(self, market_cap: double) -> void:
        self.market_cap = market_cap
