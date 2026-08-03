from numpy import double, void
from pandas import DataFrame, Series
from MarketData.Fund import Fund
from Globals import Variables as gv


class FundAnalyser:
    fund: Fund
    data: DataFrame
    close_data: Series
    close_mean: double

    def __init__(self, fund: Fund):
        self.fund = fund
        self.data = fund.data_helper.get_data_frame()
        self.close_data = self.data[gv.close]
        self.close_mean = self.close_data.mean()

    def get_abs_growth(self) -> double:
        first = self.close_data[0]
        last = self.close_data[self.close_data.size - 1]
        return (last - first) / last * 100

    def get_growth_on_mean(self) -> double:
        last = self.close_data[self.close_data.size - 1]
        return (last - self.close_mean) / last * 100

    def add_rolling_average(self) -> void:
        self.data['MA5'] = self.close_data.rolling(window=5).mean()
        self.data['MA10'] = self.close_data.rolling(window=5).mean()

    def get_volatility(self) -> double:
        points = self.close_data
        vol = 0
        for point in points:
            vol += (point - self.close_mean)**2
        vol = vol / self.close_data.size / self.close_mean
        return vol
