import pytest
from Base.BaseDataHelper import BaseDataHelper
from MarketData.FundList import Fund


def test_LoadCSV():
    startDate = '2023-11-01'
    endDate = '2023-12-01'
    fund = Fund(isin="GB00B5N99561", full_name="Artemis Global Income Fund Inc")
    helper = BaseDataHelper("/Data/Yahoo/TestData/", fund.full_name + "_" + startDate + "_" + endDate + ".csv")
    helper.load_csv_to_df()
    data = helper.get_data_frame()
    assert data['Close'][0] == pytest.approx(109.19)
