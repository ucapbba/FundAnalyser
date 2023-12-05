from Base.BaseDataHelper import BaseDataHelper
import pytest
from MarketData.FundList import Fund
from MarketData.FundDataAnalyser import FundAnalyser


def GetFundDataHelper():
    startDate = '2023-11-01'
    endDate = '2023-12-01'
    fund = Fund("GB00B5N99561", "Artemis Global Income Fund Inc")
    helper = BaseDataHelper("/Data/Yahoo/TestData/", fund.fullName + "_" + startDate + "_" + endDate + ".csv")
    helper.LoadCSVtoDF()
    helper.myDataFrame.reset_index()
    fund.setDataHelper(helper)
    return fund


def test_mean():
    fund = GetFundDataHelper()
    analyser = FundAnalyser(fund)
    mean = analyser.closeMean
    assert mean == pytest.approx(111.70, rel=1e-2)


def test_AbsGrowth():
    fund = GetFundDataHelper()
    analyser = FundAnalyser(fund)
    growth = analyser.GetAbsGrowth()
    assert growth == pytest.approx(2.674, rel=1e-2)

    
def test_GrowthOnMean():
    fund = GetFundDataHelper()
    analyser = FundAnalyser(fund)
    growth = analyser.GetGrowthOnMean()
    assert growth == pytest.approx(0.435, rel=1e-2)


def test_Vol():
    fund = GetFundDataHelper()
    analyser = FundAnalyser(fund)
    vol = analyser.GetVolatility()
    assert vol == pytest.approx(0.0084712, rel=1e-4)
