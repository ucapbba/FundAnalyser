import yfinance as yf
import pytest
from MarketData.FundList import FundList


def test_MarketData():
    fundList = FundList()
    fund = fundList.get_fund("Artemis")
    startDate = '2026-06-01'
    endDate = '2026-06-03'
    data = yf.download(fund.isin, startDate, endDate)
    # yfinance returns MultiIndex columns (Price, Ticker); flatten so 'Close' is a plain column
    data.columns = data.columns.get_level_values(0)
    assert data['Close'].iloc[0] == pytest.approx(2.4528)
