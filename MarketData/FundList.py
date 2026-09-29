from collections import UserDict
from MarketData.Fund import Fund


class BaseFundList(UserDict):
    def get_fund(self, fund_key: str) -> Fund:
        return self[fund_key]


class QuantumCompanyList(BaseFundList):
    def __init__(self):
        super().__init__()
        self["IonQ"] = Fund(isin="US46222L1089", full_name="IonQ")
        # Trapped-ion quantum computers. Generally regarded as one of the strongest pure-play quantum companies commercially.
        self["Rigetti"] = Fund(isin="US76655K1034", full_name="Rigetti Computing")
        # Superconducting-qubit quantum computers.
        self["D-Wave"] = Fund(isin="US26740W1099", full_name="D-Wave Quantum")
        # Quantum annealing systems, plus gate-model quantum efforts.
        self["Quantum"] = Fund(isin="US74766W1080", full_name="Quantum Computing Inc")
        # Smaller company focused on quantum hardware, software, and photonics. Often grouped with the others as one of the major public US quantum stocks


class QuantumAdjacentCompanyList(BaseFundList):
    """Large diversified tech companies with significant quantum computing efforts, not pure-play quantum stocks."""
    def __init__(self):
        super().__init__()
        self["IBM"] = Fund(isin="US4592001014", full_name="IBM")
        #self["Alphabet"] = Fund(isin="US02079K3059", full_name="Alphabet (Google) Class A")
        self["Microsoft"] = Fund(isin="US5949181045", full_name="Microsoft")
        self["Intel"] = Fund(isin="US4581401001", full_name="Intel")
        self["NVIDIA"] = Fund(isin="US67066G1040", full_name="NVIDIA")


class FundList(BaseFundList):
    def __init__(self):
        super().__init__()
        self["7IM"] = Fund(isin="GB00B1LBG003", full_name="7IM Sustainable Balance Fund C Inc")
        self["abrdn Latin"] = Fund(isin="GB00B4R0SD95", full_name="abrdn Latin American Equity Fund")
        self["abrdn UK"] = Fund(isin="GB00BRK2VS91", full_name="abrdn UK Income Equity Fund")
        self["abrdn UK sus"] = Fund(isin="GB00B131GH54", full_name="abrdn UK Sus & Resp Investment Equity")
        self["Artemis"] = Fund(isin="GB00B5N99561", full_name="Artemis Global Income Fund Inc")
        self["Artemis small"] = Fund(isin="GB00BMMV5766", full_name="Artemis US Smaller Companies Fund")
        self["Aviva"] = Fund(isin="GB00BYYZ2464", full_name="Aviva Investors UK Property Feeder Inc Fund 2 GBP Inc")
        self["Baillie Gifford"] = Fund(isin="GB00B1W0GF10", full_name="Baillie Gifford High Yield Bond")
        self["Barclays Global"] = Fund(isin="GB00B4WZMX77", full_name="Barclays Global Core Fund")
        self["Barings German"] = Fund(isin="GB00B8DDY871", full_name="Barings German Growth Trust")
        self["Barings Korea"] = Fund(isin="GB00B8DD3Y69", full_name="Barings Korea Trust")
        self["Black Gold"] = Fund(isin="GB00B5ZNJ896", full_name="Blackrock Gold General Fund")
        self["Black Natural"] = Fund(isin="GB00B6865B79", full_name="BlackRock Natural Resources Fund D Acc")
        self["CT Global Bond"] = Fund(isin="GB00B8C2M701", full_name="CT Global Bond Fund")
        self["CT Global Real"] = Fund(isin="GB00BJ05NG47", full_name="CT Global Real Estate Securities")
        # self["Fidelity Emerging"] = Fund(isin="GB00BJ05NG47", full_name="Fidelity Index Pacific ex Japan Fund") #Missing
        self["Fidelity Pacific"] = Fund(isin="GB00BHZK8G51", full_name="Fidelity Index Pacific ex Japan Fund")
        self["Fidelity Sustainable"] = Fund(isin="GB00BQBG6R76", full_name="Fidelity Sustainable Emerging Markets Equity Fund")
        self["GS Emerging"] = Fund(isin="LU0858288516", full_name="Goldman Sachs Emerging Markets Equity Portfolio R Inc GBP")
        self["GS India"] = Fund(isin="LU0858290173", full_name="Goldman Sachs India Equity Portfolio R Inc GBP")
        self["HSBC Europe"] = Fund(isin="GB00B80QGH28", full_name="HSBC European Index Fund Accumulation C")
        self["HSBC FTSE 100"] = Fund(isin="GB00B80QFR50", full_name="HSBC FTSE 100 Index")
        self["HSBC All World"] = Fund(isin="GB00BMJJJG09", full_name="HSBC FTSE All World Index Fund")
        self["HSBC Japan"] = Fund(isin="GB00B80QGN87", full_name="HSBC Japan Index")
        self["HSBC Gilt"] = Fund(isin="GB00B80QG276", full_name="HSBC UK Gilt Index Fund")
        self["HSBC World"] = Fund(isin="GB00B7L42X66", full_name="HSBC World Selection Cautious Portfolio")
        self["Invesco Pacific"] = Fund(isin="GB00BJ04K596", full_name="Invesco Pacific Fund (UK) Y (Acc)")
        self["Invesco China"] = Fund(isin="GB00BJ04HS18", full_name="Invesco China Equity Fund (UK)")
        self["JPM Emerging"] = Fund(isin="GB00BNTD9T28", full_name="JPM Emerging Europe Equity II", units=10000)
        self["Jupiter Global"] = Fund(isin="GB00B4PF5918", full_name="Jupiter Global Emerging Markets Fund")
        self["Jupiter Merlin"] = Fund(isin="GB00B4WDT300", full_name="Jupiter Merlin Monthly Income Select")
        self["L&G World Sus"] = Fund(isin="GB00B28PVN01", full_name="Legal & General Future World Sust UK Eq Foc I Class Acc")
        self["L&G Index"] = Fund(isin="GB00B88Y0217", full_name="Legal & General Multi-Index 4 Fund")
        self["M&G Global Emerging"] = Fund(isin="GB00B4TL2D89", full_name="M&G Emerging Markets Bond Fund")
        self["M&G Global Gov"] = Fund(isin="GB00B700F033", full_name="M&G Global Government Bond Fund")
        self["M&G Global Macro"] = Fund(isin="GB00B78PGS53", full_name="M&G Global Macro Bond Fund")
        self["91 Gold"] = Fund(isin="GB00B1XFGM25", full_name="Ninety One Global Gold Fund")
        self["91 Income"] = Fund(isin="GB00BF4JM237", full_name="Ninety One Global Total Return Credit Fund I GBP Inc2")
        self["Money Market"] = Fund(isin="GB00B8XYYQ86", full_name="Royal London Short Term Money Market Fund")
        self["Schroder Asian"] = Fund(isin="GB00B559X853", full_name="Schroder Asian Income Fund")
        self["Schroder High Yield"] = Fund(isin="GB00B5143284", full_name="Schroder High Yield Opportunities Fund", units=0.1)
        self["UBS S&P 500"] = Fund(isin="GB00BMN91T34", full_name="UBS S&P 500 Index Fund")
        self["Van U.S Equity"] = Fund(isin="GB00B5B74S01", full_name="Vanguard U.S. Equity Index Fund")
        self["Van Gilt"] = Fund(isin="GB00B4M89245", full_name="Vanguard U.K. Long Duration Gilt Index Fund")


# The lists below use Yahoo symbols rather than ISINs in the isin field; Yahoo accepts either.

class IndexList(BaseFundList):
    """Major stock market indices."""
    def __init__(self):
        super().__init__()
        self["FTSE 100"] = Fund(isin="^FTSE", full_name="FTSE 100")
        self["FTSE 250"] = Fund(isin="^FTMC", full_name="FTSE 250")
        self["S&P 500"] = Fund(isin="^GSPC", full_name="S&P 500")
        self["Dow Jones"] = Fund(isin="^DJI", full_name="Dow Jones Industrial Average")
        self["Nasdaq"] = Fund(isin="^IXIC", full_name="Nasdaq Composite")
        self["Euro Stoxx 50"] = Fund(isin="^STOXX50E", full_name="Euro Stoxx 50")
        self["DAX"] = Fund(isin="^GDAXI", full_name="DAX")
        self["CAC 40"] = Fund(isin="^FCHI", full_name="CAC 40")
        self["Nikkei 225"] = Fund(isin="^N225", full_name="Nikkei 225")
        self["Hang Seng"] = Fund(isin="^HSI", full_name="Hang Seng")


class BondList(BaseFundList):
    """Government bonds, tracked through ETFs: their price moves the opposite way to yields."""
    def __init__(self):
        super().__init__()
        self["UK Gilts"] = Fund(isin="IGLT.L", full_name="UK Gilts (iShares Core UK Gilts)")
        self["UK Gilts 0-5yr"] = Fund(isin="IGLS.L", full_name="UK Gilts 0-5yr (iShares)")
        self["UK Index-Linked Gilts"] = Fund(isin="INXG.L", full_name="UK Index-Linked Gilts (iShares)")
        self["US Treasury 1-3yr"] = Fund(isin="SHY", full_name="US Treasury 1-3yr (iShares SHY)")
        self["US Treasury 7-10yr"] = Fund(isin="IEF", full_name="US Treasury 7-10yr (iShares IEF)")
        self["US Treasury 20+yr"] = Fund(isin="TLT", full_name="US Treasury 20+yr (iShares TLT)")
        self["US TIPS"] = Fund(isin="TIP", full_name="US Inflation-Linked Treasuries (iShares TIP)")
        self["German Bunds"] = Fund(isin="IS0L.DE", full_name="German Bunds (iShares Germany Govt Bond)")
        self["German Bunds 10yr+"] = Fund(isin="EXX6.DE", full_name="German Bunds 10.5yr+ (iShares eb.rexx)")


class CommodityList(BaseFundList):
    """Commodities, as front-month futures prices (these jump slightly when contracts roll over)."""
    def __init__(self):
        super().__init__()
        self["Gold"] = Fund(isin="GC=F", full_name="Gold")
        self["Silver"] = Fund(isin="SI=F", full_name="Silver")
        self["Platinum"] = Fund(isin="PL=F", full_name="Platinum")
        self["Copper"] = Fund(isin="HG=F", full_name="Copper")
        self["Brent Crude"] = Fund(isin="BZ=F", full_name="Brent Crude Oil")
        self["WTI Crude"] = Fund(isin="CL=F", full_name="WTI Crude Oil")
        self["Natural Gas"] = Fund(isin="NG=F", full_name="Natural Gas (US)")
        self["Wheat"] = Fund(isin="ZW=F", full_name="Wheat")
        self["Corn"] = Fund(isin="ZC=F", full_name="Corn")
        self["Coffee"] = Fund(isin="KC=F", full_name="Coffee")
