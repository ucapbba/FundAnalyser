from collections import UserDict

from MarketData.Fund import Fund


class FundList(UserDict):
    def __init__(self):
        super().__init__()
        self["7IM"] = Fund(ISIN="GB00B1LBG003", fullName="7IM Sustainable Balance Fund C Inc")
        self["abrdn Latin"] = Fund(ISIN="GB00B4R0SD95", fullName="abrdn Latin American Equity Fund")
        self["abrdn UK"] = Fund(ISIN="GB00BRK2VS91", fullName="abrdn UK Income Equity Fund")
        self["abrdn UK sus"] = Fund(ISIN="GB00B131GH54", fullName="abrdn UK Sus & Resp Investment Equity")
        self["Artemis"] = Fund(ISIN="GB00B5N99561", fullName="Artemis Global Income Fund Inc")
        self["Artemis small"] = Fund(ISIN="GB00BMMV5766", fullName="Artemis US Smaller Companies Fund")
        self["Aviva"] = Fund(ISIN="GB00BYYZ2464", fullName="Aviva Investors UK Property Feeder Inc Fund 2 GBP Inc")
        self["Baillie Gifford"] = Fund(ISIN="GB00B1W0GF10", fullName="Baillie Gifford High Yield Bond")
        self["Barclays Global"] = Fund(ISIN="GB00B4WZMX77", fullName="Barclays Global Core Fund")
        self["Barings German"] = Fund(ISIN="GB00B8DDY871", fullName="Barings German Growth Trust")
        self["Barings Korea"] = Fund(ISIN="GB00B8DD3Y69", fullName="Barings Korea Trust")
        self["Black Gold"] = Fund(ISIN="GB00B5ZNJ896", fullName="Blackrock Gold General Fund")
        self["Black Natural"] = Fund(ISIN="GB00B6865B79", fullName="BlackRock Natural Resources Fund D Acc")
        self["CT Global Bond"] = Fund(ISIN="GB00B8C2M701", fullName="CT Global Bond Fund")
        self["CT Global Real"] = Fund(ISIN="GB00BJ05NG47", fullName="CT Global Real Estate Securities")
        # self["Fidelity Emerging"] = Fund(ISIN="GB00BJ05NG47", fullName="Fidelity Index Pacific ex Japan Fund") #Missing
        self["Fidelity Pacific"] = Fund(ISIN="GB00BHZK8G51", fullName="Fidelity Index Pacific ex Japan Fund")
        self["Fidelity Sustainable"] = Fund(ISIN="GB00BQBG6R76", fullName="Fidelity Sustainable Emerging Markets Equity Fund")
        self["GS Emerging"] = Fund(ISIN="LU0858288516", fullName="Goldman Sachs Emerging Markets Equity Portfolio R Inc GBP")
        self["GS India"] = Fund(ISIN="LU0858290173", fullName="Goldman Sachs India Equity Portfolio R Inc GBP")
        self["HSBC Europe"] = Fund(ISIN="GB00B80QGH28", fullName="HSBC European Index Fund Accumulation C")
        self["HSBC FTSE 100"] = Fund(ISIN="GB00B80QFR50", fullName="HSBC FTSE 100 Index")
        self["HSBC All World"] = Fund(ISIN="GB00BMJJJG09", fullName="HSBC FTSE All World Index Fund")
        self["HSBC Japan"] = Fund(ISIN="GB00B80QGN87", fullName="HSBC Japan Index")
        self["HSBC Gilt"] = Fund(ISIN="GB00B80QG276", fullName="HSBC UK Gilt Index Fund")
        self["HSBC World"] = Fund(ISIN="GB00B7L42X66", fullName="HSBC World Selection Cautious Portfolio")
        self["Invesco Pacific"] = Fund(ISIN="GB00BJ04K596", fullName="Invesco Pacific Fund (UK) Y (Acc)")
        self["Invesco China"] = Fund(ISIN="GB00BJ04HS18", fullName="Invesco China Equity Fund (UK)")
        self["JPM Emerging"] = Fund(ISIN="GB00BNTD9T28", fullName="JPM Emerging Europe Equity II", units=10000)
        self["Jupiter Global"] = Fund(ISIN="GB00B4PF5918", fullName="Jupiter Global Emerging Markets Fund")
        self["Jupiter Merlin"] = Fund(ISIN="GB00B4WDT300", fullName="Jupiter Merlin Monthly Income Select")
        self["L&G World Sus"] = Fund(ISIN="GB00B28PVN01", fullName="Legal & General Future World Sust UK Eq Foc I Class Acc")
        self["L&G Index"] = Fund(ISIN="GB00B88Y0217", fullName="Legal & General Multi-Index 4 Fund")
        self["M&G Global Emerging"] = Fund(ISIN="GB00B4TL2D89", fullName="M&G Emerging Markets Bond Fund")
        self["M&G Global Gov"] = Fund(ISIN="GB00B700F033", fullName="M&G Global Government Bond Fund")
        self["M&G Global Macro"] = Fund(ISIN="GB00B78PGS53", fullName="M&G Global Macro Bond Fund")
        self["91 Gold"] = Fund(ISIN="GB00B1XFGM25", fullName="Ninety One Global Gold Fund")
        self["91 Income"] = Fund(ISIN="GB00BF4JM237", fullName="Ninety One Global Total Return Credit Fund I GBP Inc2")
        self["Money Market"] = Fund(ISIN="GB00B8XYYQ86", fullName="Royal London Short Term Money Market Fund")
        self["Schroder Asian"] = Fund(ISIN="GB00B559X853", fullName="Schroder Asian Income Fund")
        self["Schroder High Yield"] = Fund(ISIN="GB00B5143284", fullName="Schroder High Yield Opportunities Fund", units=0.1)
        self["UBS S&P 500"] = Fund(ISIN="GB00BMN91T34", fullName="UBS S&P 500 Index Fund")
        self["Van U.S Equity"] = Fund(ISIN="GB00B5B74S01", fullName="Vanguard U.S. Equity Index Fund")
        self["Van Gilt"] = Fund(ISIN="GB00B4M89245", fullName="Vanguard U.K. Long Duration Gilt Index Fund")

    def GetFund(self, fundKey: str) -> Fund:
        return self[fundKey]
