from Base.BaseDataHelper import BaseDataHelper
import pytest
from MarketData.FundList import Fund
from MarketData.FundDataAnalyser import FundAnalyser


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
