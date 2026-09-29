from numpy import double, void
from pandas import DataFrame, Series, DateOffset, to_datetime
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
        # Yahoo sometimes returns rows with no close yet (e.g. the latest day for some European
        # listings); drop them and renumber so positional lookups like close_data[0] still work
        if self.data[gv.close].isna().any():
            self.data = self.data.dropna(subset=[gv.close]).reset_index(drop=True)
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

    def get_change_since_previous_close(self) -> double:
        """% change from the previous trading day's close to the latest close."""
        if self.close_data.size < 2:
            return None
        previous = self.close_data.iloc[-2]
        last = self.close_data.iloc[-1]
        return (last - previous) / previous * 100

    def get_change_over(self, offset: DateOffset) -> double:
        """% change from the last close on or before (latest date - offset) to the latest close.

        Returns None if the data doesn't go back far enough.
        """
        dates = to_datetime(self.data['Date'])
        target = dates.iloc[-1] - offset
        earlier = self.close_data[dates <= target]
        if earlier.empty:
            return None
        then = earlier.iloc[-1]
        last = self.close_data.iloc[-1]
        return (last - then) / then * 100

    def get_period_changes(self) -> dict:
        return {
            gv.CHANGE_DAY: self.get_change_since_previous_close(),
            gv.CHANGE_WEEK: self.get_change_over(DateOffset(weeks=1)),
            gv.CHANGE_MONTH: self.get_change_over(DateOffset(months=1)),
            gv.CHANGE_YEAR: self.get_change_over(DateOffset(years=1)),
            gv.CHANGE_5YEAR: self.get_change_over(DateOffset(years=5)),
        }
