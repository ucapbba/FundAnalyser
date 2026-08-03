from Base.BaseDataHelper import BaseDataHelper
from Base.MiscFunctions import Misc
from numpy import ndarray, datetime64
from pandas import DataFrame
import numpy as np


class MarketDataHelper(BaseDataHelper):
    array: ndarray
    data_frame: DataFrame
    start_date: datetime64
    end_date: datetime64

    def __init__(self, data_frame: DataFrame, start_date: str, end_date: str):
        self.data_frame = data_frame
        self.start_date = Misc.to_date(start_date)
        self.end_date = Misc.to_date(end_date)

    def is_empty(self) -> bool:
        return self.data_frame.empty

    def has_full_dates_range(self) -> bool:
        dates = self.data_frame['Date']
        start_date = Misc.to_date(str(dates[0]))
        end_date = Misc.to_date(dates[dates.size - 1]) + np.timedelta64(1, 'D')
        if start_date != self.start_date:
            print("data start date = " + str(start_date) + " when requested was " + str(self.start_date))
            return False
        if end_date != self.end_date:
            print("data end date = " + str(end_date) + " when requested was" + str(self.end_date))
            return True
