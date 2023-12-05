import pytest
from Base.BaseDataHelper import BaseDataHelper
from MarketData.FundList import Fund


def test_LoadCSV():
    startDate = '2023-11-01'
    endDate = '2023-12-01'
    fund = Fund("GB00B5N99561", "Artemis Global Income Fund Inc")
    helper = BaseDataHelper("/Data/Yahoo/TestData/", fund.fullName + "_" + startDate + "_" + endDate + ".csv")
    helper.LoadCSVtoDF()
    data = helper.GetDataFrame()
    assert data['Close'][0] == pytest.approx(109.19)
