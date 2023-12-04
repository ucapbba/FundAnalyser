import string


class Fund:
    ISIN: string
    fullName: string

    def __init__(self, _ISIN, _fullName):
        self.ISIN = _ISIN
        self.fullName = _fullName


class FundList:
    myDict: dict

    def __init__(self):
        self.myDict = {}
        self.myDict["Van"] = Fund("GB00B5B74S01", "Vanguard U.S. Equity Index Fund")
        self.myDict["M&G Global"] = Fund("GB00B700F033", "M&G Global Government Bond Fund")
        self.myDict["Artemis"] = Fund("GB00B5N99561", "Artemis Global Income Fund Inc")

    def GetFundList(self) -> list:
        return self.myList

    def GetFund(self, fundKey: str) -> Fund:
        return self.myDict[fundKey]
