from Base.MiscFunctions import Misc
import pandas as pd


def test_ToDate():
    startDate = '2023-06-01'
    mydatetime64 = Misc.to_date(startDate)
    assert pd.to_datetime(startDate) == mydatetime64


def test_isBusinesDay():
    startDate = '2023-06-01'
    mydatetime64 = Misc.to_date(startDate)
    isBusDay = Misc.is_business_day(mydatetime64)
    assert isBusDay is True
    startDate = '2023-06-03'
    mydatetime64 = Misc.to_date(startDate)
    isBusDay = Misc.is_business_day(mydatetime64)
    assert isBusDay is False
