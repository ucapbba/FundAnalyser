from numpy import datetime64
import pandas as pd
from pandas.tseries.offsets import BDay


class Misc:

    def to_date(date: str) -> datetime64:
        new_date = pd.to_datetime(date)
        return new_date

    def is_business_day(date: datetime64) -> bool:
        bday = BDay()
        is_bus_day = bday.is_on_offset(date)
        return is_bus_day
