from Base.MiscFunctions import Misc
import pandas as pd


def test_ToDate():
    startDate = '2023-06-01'
    mydatetime64 = Misc.toDate(startDate)
    assert pd.to_datetime(startDate) == mydatetime64


def test_isBusinesDay():
    startDate = '2023-06-01'
    mydatetime64 = Misc.toDate(startDate)
    isBusDay = Misc.isBusinessDay(mydatetime64)
    assert isBusDay is True
    startDate = '2023-06-03'
    mydatetime64 = Misc.toDate(startDate)
    isBusDay = Misc.isBusinessDay(mydatetime64)
    assert isBusDay is False
