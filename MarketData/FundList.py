from MarketData.Fund import Fund


class FundList:
    myDict: dict

    def __init__(self):
        self.myDict = {}
        self.myDict["Artemis"] = Fund("GB00B5N99561", "Artemis Global Income Fund Inc")
        self.myDict["BlackGold"] = Fund("GB00B5ZNJ896", "Blackrock Gold General Fund")
        self.myDict["GS India"] = Fund("LU0858290173", "Goldman Sachs India Equity Portfolio R Inc GBP")
        self.myDict["HSBC Europe"] = Fund("GB00B80QGH28", "HSBC European Index Fund Accumulation C")
        self.myDict["HSBC All World"] = Fund("GB00BMJJJG09", "HSBC FTSE All World Index Fund")
        self.myDict["Invesco Pacific"] = Fund("GB00BJ04K596", "Invesco Pacific Fund (UK) Y (Acc)")
        self.myDict["Invesco China"] = Fund("GB00BJ04HS18", "Invesco China Equity Fund (UK)")
        self.myDict["M&G Global Gov"] = Fund("GB00B700F033", "M&G Global Government Bond Fund")
        self.myDict["M&G Global Macro"] = Fund("GB00B78PGS53", "M&G Global Macro Bond Fund")
        self.myDict["Van U.S Equity"] = Fund("GB00B5B74S01", "Vanguard U.S. Equity Index Fund")
        self.myDict["Van Gilt"] = Fund("GB00B4M89245", "Vanguard U.K. Long Duration Gilt Index Fund")

    def GetFundList(self) -> list:
        return self.myList

    def GetFund(self, fundKey: str) -> Fund:
        return self.myDict[fundKey]
