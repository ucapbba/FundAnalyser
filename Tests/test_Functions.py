import pandas as pd
import pytest
from Base.BaseDataHelper import BaseDataHelper
from MarketData.Fund import Fund
import Globals.Functions as funcs
import Globals.Variables as gv


def GetFundWithDataHelper():
    startDate = '2023-11-01'
    endDate = '2023-12-01'
    fund = Fund(ISIN="GB00B5N99561", fullName="Artemis Global Income Fund Inc")
    helper = BaseDataHelper("/Data/Yahoo/TestData/", fund.fullName + "_" + startDate + "_" + endDate + ".csv")
    helper.LoadCSVtoDF()
    fund.setDataHelper(helper)
    return fund


def MakePriceFrame(closeValues):
    # mimics the shape yfinance returns: DatetimeIndex named "Date", plain columns
    index = pd.date_range('2023-01-02', periods=len(closeValues), freq='B', name='Date')
    return pd.DataFrame({'Close': closeValues}, index=index)


# GetAllFundIndicators is keyed off dict.items(), so a plain dict stands in for
# FundList (also dict-like) regardless of its internal fund universe.
def test_GetAllFundIndicators_populatesIndicatorsForFundWithData():
    fund = GetFundWithDataHelper()
    fundList = {"Artemis": fund}

    funcs.GetAllFundIndicators(fundList)

    assert fund.indicators[gv.MEAN] == pytest.approx(111.70, rel=1e-2)
    assert fund.indicators[gv.ABS_GROWTH] == pytest.approx(2.674, rel=1e-2)
    assert fund.indicators[gv.GROWTH_MEAN] == pytest.approx(0.435, rel=1e-2)
    assert fund.indicators[gv.VOL] == pytest.approx(0.0084712, rel=1e-4)
    assert fund.indicators[gv.UNITS] == fund.units


def test_GetAllFundIndicators_skipsFundWithoutDataHelper():
    fund = Fund(ISIN="GB00000000", fullName="No Data Fund")
    fundList = {"NoData": fund}

    funcs.GetAllFundIndicators(fundList)

    assert fund.indicators == {}


def test_getData_fromYahoo_returnsDownloadedData(monkeypatch):
    expected = MakePriceFrame([1.0, 2.0])
    monkeypatch.setattr(funcs.yf, "download", lambda isin, startDate, endDate: expected)
    fund = Fund(ISIN="GB00000000", fullName="Some Fund")

    data = funcs.getData(fund, '2023-01-01', '2023-02-01')

    assert data is expected


def test_getData_fromYahoo_swallowsExceptionAndReturnsNone(monkeypatch):
    def raiseError(isin, startDate, endDate):
        raise ValueError("Yahoo unavailable")

    monkeypatch.setattr(funcs.yf, "download", raiseError)
    fund = Fund(ISIN="GB00000000", fullName="Some Fund")

    data = funcs.getData(fund, '2023-01-01', '2023-02-01')

    assert data is None


def test_getData_fromCSV_usesBaseDataHelper(monkeypatch):
    class FakeDataHelper:
        def __init__(self, path, filename):
            self.path = path
            self.filename = filename

        def LoadCSVtoDF(self):
            self.myDataFrame = pd.DataFrame({'Close': [1.0, 2.0]})

        def GetDataFrame(self):
            return self.myDataFrame

    monkeypatch.setattr(funcs, "BaseDataHelper", FakeDataHelper)
    fund = Fund(ISIN="GB00000000", fullName="Some Fund")

    data = funcs.getData(fund, '2023-01-01', '2023-02-01', fromYahoo=False)

    assert list(data['Close']) == [1.0, 2.0]


def test_PopulateAllFundData_setsDataHelperWhenDataReturned(monkeypatch):
    monkeypatch.setattr(funcs, "getData", lambda fund, startDate, endDate: MakePriceFrame([1.0, 2.0, 3.0]))
    fund = Fund(ISIN="GB00000000", fullName="Some Fund")
    fundList = {"SomeFund": fund}

    funcs.PopulateAllFundData('2023-01-02', '2023-01-05', fundList)

    assert fund.dataHelper is not None
    assert list(fund.dataHelper.GetDataFrame()['Close']) == [1.0, 2.0, 3.0]


def test_PopulateAllFundData_skipsFundWhenDataIsEmpty(monkeypatch):
    monkeypatch.setattr(funcs, "getData", lambda fund, startDate, endDate: MakePriceFrame([]))
    fund = Fund(ISIN="GB00000000", fullName="Some Fund")
    fundList = {"SomeFund": fund}

    funcs.PopulateAllFundData('2023-01-02', '2023-01-05', fundList)

    assert fund.dataHelper is None


def test_PlotAllFundData_onlyPlotsFundsWithDataHelper(monkeypatch):
    calls = []

    class FakePlotter:
        def __init__(self, dataHelper):
            self.dataHelper = dataHelper

        def PlotSNS(self, x, y, title):
            calls.append((x, y, title))

    monkeypatch.setattr(funcs, "MarketDtaPlotter", FakePlotter)
    fundWithData = GetFundWithDataHelper()
    fundWithoutData = Fund(ISIN="GB00000000", fullName="No Data Fund")
    fundList = {"HasData": fundWithData, "NoData": fundWithoutData}

    funcs.PlotAllFundData(fundList)

    assert calls == [("Date", "Close", fundWithData.fullName)]
