import pandas as pd
import pytest
from Base.BaseDataHelper import BaseDataHelper
from MarketData.Fund import Fund
import Globals.Functions as funcs
import Globals.Variables as gv


def GetFundWithDataHelper():
    startDate = '2023-11-01'
    endDate = '2023-12-01'
    fund = Fund(isin="GB00B5N99561", full_name="Artemis Global Income Fund Inc")
    helper = BaseDataHelper("/Data/Yahoo/TestData/", fund.full_name + "_" + startDate + "_" + endDate + ".csv")
    helper.load_csv_to_df()
    fund.set_data_helper(helper)
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

    funcs.get_all_fund_indicators(fundList)

    assert fund.indicators[gv.MEAN] == pytest.approx(111.70, rel=1e-2)
    assert fund.indicators[gv.ABS_GROWTH] == pytest.approx(2.674, rel=1e-2)
    assert fund.indicators[gv.GROWTH_MEAN] == pytest.approx(0.435, rel=1e-2)
    assert fund.indicators[gv.VOL] == pytest.approx(0.0084712, rel=1e-4)
    assert fund.indicators[gv.UNITS] == fund.units


def test_GetAllFundIndicators_skipsFundWithoutDataHelper():
    fund = Fund(isin="GB00000000", full_name="No Data Fund")
    fundList = {"NoData": fund}

    funcs.get_all_fund_indicators(fundList)

    assert fund.indicators == {}


def test_getData_fromYahoo_returnsDownloadedData(monkeypatch):
    expected = MakePriceFrame([1.0, 2.0])
    monkeypatch.setattr(funcs.yf, "download", lambda *args, **kwargs: expected)
    fund = Fund(isin="GB00000000", full_name="Some Fund")

    data = funcs.get_data(fund, '2023-01-01', '2023-02-01')

    assert data is expected


def test_getData_fromYahoo_swallowsExceptionAndReturnsNone(monkeypatch):
    def raiseError(*args, **kwargs):
        raise ValueError("Yahoo unavailable")

    monkeypatch.setattr(funcs.yf, "download", raiseError)
    fund = Fund(isin="GB00000000", full_name="Some Fund")

    data = funcs.get_data(fund, '2023-01-01', '2023-02-01')

    assert data is None


def test_getData_fromCSV_usesBaseDataHelper(monkeypatch):
    class FakeDataHelper:
        def __init__(self, path, filename):
            self.path = path
            self.filename = filename

        def load_csv_to_df(self):
            self.data_frame = pd.DataFrame({'Close': [1.0, 2.0]})

        def get_data_frame(self):
            return self.data_frame

    monkeypatch.setattr(funcs, "BaseDataHelper", FakeDataHelper)
    fund = Fund(isin="GB00000000", full_name="Some Fund")

    data = funcs.get_data(fund, '2023-01-01', '2023-02-01', from_yahoo=False)

    assert list(data['Close']) == [1.0, 2.0]


def test_PopulateAllFundData_setsDataHelperWhenDataReturned(monkeypatch):
    monkeypatch.setattr(funcs, "get_data", lambda fund, startDate, endDate: MakePriceFrame([1.0, 2.0, 3.0]))
    fund = Fund(isin="GB00000000", full_name="Some Fund")
    fundList = {"SomeFund": fund}

    funcs.populate_all_fund_data('2023-01-02', '2023-01-05', fundList)

    assert fund.data_helper is not None
    assert list(fund.data_helper.get_data_frame()['Close']) == [1.0, 2.0, 3.0]


def test_PopulateAllFundData_skipsFundWhenDataIsEmpty(monkeypatch):
    monkeypatch.setattr(funcs, "get_data", lambda fund, startDate, endDate: MakePriceFrame([]))
    fund = Fund(isin="GB00000000", full_name="Some Fund")
    fundList = {"SomeFund": fund}

    funcs.populate_all_fund_data('2023-01-02', '2023-01-05', fundList)

    assert fund.data_helper is None


def test_PlotAllFundData_onlyPlotsFundsWithDataHelper(monkeypatch):
    calls = []

    class FakePlotter:
        def __init__(self, dataHelper):
            self.dataHelper = dataHelper

        def plot_sns(self, x, y, title):
            calls.append((x, y, title))

    monkeypatch.setattr(funcs, "MarketDtaPlotter", FakePlotter)
    fundWithData = GetFundWithDataHelper()
    fundWithoutData = Fund(isin="GB00000000", full_name="No Data Fund")
    fundList = {"HasData": fundWithData, "NoData": fundWithoutData}

    funcs.plot_all_fund_data(fundList)

    assert calls == [("Date", "Close", fundWithData.full_name)]
