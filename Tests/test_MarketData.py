import pytest
from MarketData.FundList import FundList
import pandas as pd

def test_MarketData(monkeypatch):
    fund_list = FundList()
    fund = fund_list.get_fund("Artemis")

    columns = pd.MultiIndex.from_tuples([("Close", fund.isin)], names=["Price", "Ticker"])
    fake_data = pd.DataFrame({("Close", fund.isin): [2.4528]}, columns=columns)

    import Globals.Functions as gf
    monkeypatch.setattr(gf.yf, "download", lambda *args, **kwargs: fake_data)

    data = gf.get_data(fund, "2026-06-01", "2026-06-03")
    data.columns = data.columns.get_level_values(0)

    assert data["Close"].iloc[0] == pytest.approx(2.4528)