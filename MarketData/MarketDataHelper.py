import string
from Base.BaseDataHelper import BaseDataHelper
from Base.MiscFunctions import Misc
from numpy import ndarray, datetime64
from pandas import DataFrame
import numpy as np


class MarketDataHelper(BaseDataHelper):
    myArray: ndarray
    myDataFrame: DataFrame
    myStartDate: datetime64
    myEndDate: datetime64

    def __init__(self, _myDataFrame: DataFrame, _myStartDate: string, _myEndDate: string):
        self.myDataFrame = _myDataFrame
        self.myStartDate = Misc.toDate(_myStartDate)
        self.myEndDate = Misc.toDate(_myEndDate)
        
    def IsEmpty(self) -> bool:
        if self.myDataFrame.empty:
            return True
        return False

    def HasFullDatesRange(self,) -> bool:
        dates = self.myDataFrame['Date']
        startDate = Misc.toDate(str(dates[0]))
        endDate = Misc.toDate(dates[dates.size - 1]) + np.timedelta64(1, 'D')
        if startDate != self.myStartDate:
            print("data start date = " + str(startDate) + " when requested was " + str(self.myStartDate))
            return False
        if endDate != self.myEndDate:
            print("data end date = " + str(endDate) + " when requested was" + str(self.myEndDate))
            return True
