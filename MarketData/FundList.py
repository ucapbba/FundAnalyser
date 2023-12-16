from MarketData.Fund import Fund


class FundList:
    myDict: dict

    def __init__(self):
        self.myDict = {}
        self.myDict["7IM"] = Fund("GB00B1LBG003", "7IM Sustainable Balance Fund C Inc")
        self.myDict["abrdn Latin"] = Fund("GB00B4R0SD95", "abrdn Latin American Equity Fund")
        self.myDict["abrdn UK"] = Fund("GB00BRK2VS91", "abrdn UK Income Equity Fund")
        self.myDict["abrdn UK sus"] = Fund("GB00B131GH54", "abrdn UK Sus & Resp Investment Equity")
        self.myDict["Artemis"] = Fund("GB00B5N99561", "Artemis Global Income Fund Inc")
        self.myDict["Artemis small"] = Fund("GB00BMMV5766", "Artemis US Smaller Companies Fund")
        self.myDict["Aviva"] = Fund("GB00BYYZ2464", "Aviva Investors UK Property Feeder Inc Fund 2 GBP Inc")
        self.myDict["Baillie Gifford"] = Fund("GB00B1W0GF10", "Baillie Gifford High Yield Bond")
        self.myDict["Barclays Global"] = Fund("GB00B4WZMX77", "Barclays Global Core Fund")
        self.myDict["Barings German"] = Fund("GB00B8DDY871", "Barings German Growth Trust")
        self.myDict["Barings Korea"] = Fund("GB00B8DD3Y69", "Barings Korea Trust")
        self.myDict["Black Gold"] = Fund("GB00B5ZNJ896", "Blackrock Gold General Fund")
        self.myDict["Black Natural"] = Fund("GB00B6865B79", "BlackRock Natural Resources Fund D Acc")
        self.myDict["CT Global Bond"] = Fund("GB00B8C2M701", "CT Global Bond Fund")
        self.myDict["CT Global Real"] = Fund("GB00BJ05NG47", "CT Global Real Estate Securities")
        # self.myDict["Fidelity Emerging"] = Fund("GB00BJ05NG47", "Fidelity Index Pacific ex Japan Fund") #Missing
        self.myDict["Fidelity Pacific"] = Fund("GB00BHZK8G51", "Fidelity Index Pacific ex Japan Fund")
        self.myDict["Fidelity Sustainable"] = Fund("GB00BQBG6R76", "Fidelity Sustainable Emerging Markets Equity Fund")
        self.myDict["GS Emerging"] = Fund("LU0858288516", "Goldman Sachs Emerging Markets Equity Portfolio R Inc GBP")
        self.myDict["GS India"] = Fund("LU0858290173", "Goldman Sachs India Equity Portfolio R Inc GBP")
        self.myDict["HSBC Europe"] = Fund("GB00B80QGH28", "HSBC European Index Fund Accumulation C")
        self.myDict["HSBC FTSE 100"] = Fund("GB00B80QFR50", "HSBC FTSE 100 Index")
        self.myDict["HSBC All World"] = Fund("GB00BMJJJG09", "HSBC FTSE All World Index Fund")
        self.myDict["HSBC Japan"] = Fund("GB00B80QGN87", "HSBC Japan Index")
        self.myDict["HSBC Gilt"] = Fund("GB00B80QG276", "HSBC UK Gilt Index Fund")
        self.myDict["HSBC World"] = Fund("GB00B7L42X66", "HSBC World Selection Cautious Portfolio")
        self.myDict["Invesco Pacific"] = Fund("GB00BJ04K596", "Invesco Pacific Fund (UK) Y (Acc)")
        self.myDict["Invesco China"] = Fund("GB00BJ04HS18", "Invesco China Equity Fund (UK)")
        self.myDict["JPM Emerging"] = Fund("GB00BNTD9T28", "JPM Emerging Europe Equity II", 10000)
        self.myDict["Jupiter Global"] = Fund("GB00B4PF5918", "Jupiter Global Emerging Markets Fund")
        self.myDict["Jupiter Merlin"] = Fund("GB00B4WDT300", "Jupiter Merlin Monthly Income Select")
        self.myDict["L&G World Sus"] = Fund("GB00B28PVN01", "Legal & General Future World Sust UK Eq Foc I Class Acc")
        self.myDict["L&G Index"] = Fund("GB00B88Y0217", "Legal & General Multi-Index 4 Fund")
        self.myDict["M&G Global Emerging"] = Fund("GB00B4TL2D89", "M&G Emerging Markets Bond Fund")
        self.myDict["M&G Global Gov"] = Fund("GB00B700F033", "M&G Global Government Bond Fund")
        self.myDict["M&G Global Macro"] = Fund("GB00B78PGS53", "M&G Global Macro Bond Fund")
        self.myDict["91 Gold"] = Fund("GB00B1XFGM25", "Ninety One Global Gold Fund")
        self.myDict["91 Income"] = Fund("GB00BF4JM237", "Ninety One Global Total Return Credit Fund I GBP Inc2")
        self.myDict["Money Market"] = Fund("GB00B8XYYQ86", "Royal London Short Term Money Market Fund")
        self.myDict["Schroder Asian"] = Fund("GB00B559X853", "Schroder Asian Income Fund")
        self.myDict["Schroder High Yield"] = Fund("GB00B5143284", "Schroder High Yield Opportunities Fund", 0.1)
        self.myDict["UBS S&P 500"] = Fund("GB00BMN91T34", "UBS S&P 500 Index Fund")
        self.myDict["Van U.S Equity"] = Fund("GB00B5B74S01", "Vanguard U.S. Equity Index Fund")
        self.myDict["Van Gilt"] = Fund("GB00B4M89245", "Vanguard U.K. Long Duration Gilt Index Fund")

    def GetFundList(self) -> list:
        return self.myList

    def GetFund(self, fundKey: str) -> Fund:
        return self.myDict[fundKey]
