import yfinance as yf
import pytest
from MarketData.FundList import FundList


def test_MarketData():
    fundList = FundList()
    fund = fundList.GetFund("Artemis")
    startDate = '2023-06-01'
    endDate = '2023-06-03'
    data = yf.download(fund.ISIN, startDate, endDate)
    assert data['Close'][0] == pytest.approx(102.72)
