from Base.BaseDataHelper import BaseDataHelper
import pytest
from MarketData.FundList import Fund
from MarketData.FundDataAnalyser import FundAnalyser
from pandas import DateOffset


def GetFundDataHelper():
    startDate = '2023-11-01'
    endDate = '2023-12-01'
    fund = Fund(isin="GB00B5N99561", full_name="Artemis Global Income Fund Inc")
    helper = BaseDataHelper("/Data/Yahoo/TestData/", fund.full_name + "_" + startDate + "_" + endDate + ".csv")
    helper.load_csv_to_df()
    helper.data_frame.reset_index()
    fund.set_data_helper(helper)
    return fund


def test_mean():
    fund = GetFundDataHelper()
    analyser = FundAnalyser(fund)
    mean = analyser.close_mean
    assert mean == pytest.approx(111.70, rel=1e-2)


def test_AbsGrowth():
    fund = GetFundDataHelper()
    analyser = FundAnalyser(fund)
    growth = analyser.get_abs_growth()
    assert growth == pytest.approx(2.674, rel=1e-2)


def test_GrowthOnMean():
    fund = GetFundDataHelper()
    analyser = FundAnalyser(fund)
    growth = analyser.get_growth_on_mean()
    assert growth == pytest.approx(0.435, rel=1e-2)


def test_Vol():
    fund = GetFundDataHelper()
    analyser = FundAnalyser(fund)
    vol = analyser.get_volatility()
    assert vol == pytest.approx(0.0084712, rel=1e-4)


def GetSyntheticFund():
    # weekdays from 2025-01-01 to 2026-01-15; close rises by 1 each trading day from 100
    from pandas import DataFrame, bdate_range
    from MarketData.MarketDataHelper import MarketDataHelper
    dates = bdate_range("2025-01-01", "2026-01-15")
    data = DataFrame({"Date": dates, "Close": [100.0 + i for i in range(len(dates))]})
    fund = Fund(isin="TEST", full_name="Synthetic")
    fund.set_data_helper(MarketDataHelper(data, "2025-01-01", "2026-01-16"))
    return fund, data


def test_ChangeSincePreviousClose():
    fund, data = GetSyntheticFund()
    last = data["Close"].iloc[-1]
    change = FundAnalyser(fund).get_change_since_previous_close()
    assert change == pytest.approx((last - (last - 1)) / (last - 1) * 100)


def test_ChangeOverWeek():
    # 2026-01-15 is a Thursday; a week earlier is Thursday 2026-01-08, 5 trading days back
    fund, data = GetSyntheticFund()
    last = data["Close"].iloc[-1]
    change = FundAnalyser(fund).get_change_over(DateOffset(weeks=1))
    assert change == pytest.approx((last - (last - 5)) / (last - 5) * 100)


def test_ChangeOverYearUsesLastCloseOnOrBefore():
    # a year before 2026-01-15 is 2025-01-15 (Wednesday) -> its close is used
    fund, data = GetSyntheticFund()
    then = data.loc[data["Date"] == "2025-01-15", "Close"].iloc[0]
    last = data["Close"].iloc[-1]
    change = FundAnalyser(fund).get_change_over(DateOffset(years=1))
    assert change == pytest.approx((last - then) / then * 100)


def test_ChangeOverTooLongReturnsNone():
    fund, _ = GetSyntheticFund()
    assert FundAnalyser(fund).get_change_over(DateOffset(years=5)) is None


def test_PeriodChangesIncludesFiveYearsAsNoneWhenTooShort():
    # synthetic data only covers ~1 year, so the 5-year change can't be worked out
    import Globals.Variables as gv
    fund, _ = GetSyntheticFund()
    changes = FundAnalyser(fund).get_period_changes()
    assert list(changes) == [gv.CHANGE_DAY, gv.CHANGE_WEEK, gv.CHANGE_MONTH, gv.CHANGE_YEAR, gv.CHANGE_5YEAR]
    assert changes[gv.CHANGE_5YEAR] is None


def test_RowsWithoutCloseAreIgnored():
    # Yahoo can return the latest row with no close; changes should use the last real close
    import numpy as np
    fund, data = GetSyntheticFund()
    data.loc[data.index[-1], "Close"] = np.nan
    analyser = FundAnalyser(fund)
    last = data["Close"].iloc[-2]
    assert analyser.close_data.iloc[-1] == last
    assert analyser.get_change_since_previous_close() == pytest.approx((last - (last - 1)) / (last - 1) * 100)
    assert analyser.get_change_over(DateOffset(weeks=1)) is not None
