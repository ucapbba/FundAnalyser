from MarketData.Fund import Fund
from MarketData.FundList import FundList


def test_FundList_isDictLikeAndIterable():
    fundList = FundList()

    assert len(fundList) > 0
    assert isinstance(fundList["Artemis"], Fund)
    for fundKey, fund in fundList.items():
        assert isinstance(fundKey, str)
        assert isinstance(fund, Fund)


def test_FundList_GetFund_matchesItemAccess():
    fundList = FundList()

    assert fundList.GetFund("Artemis") is fundList["Artemis"]
