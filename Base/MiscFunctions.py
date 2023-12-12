import string
from numpy import datetime64
import pandas as pd
from pandas.tseries.offsets import BDay


class Misc:

    def toDate(date: string) -> datetime64:
        newDate = pd.to_datetime(date)
        return newDate

    def isBusinessDay(date: datetime64) -> bool:
        bday = BDay()
        isBusDay = bday.is_on_offset(date)
        return isBusDay
