from MarketData import MarketDataHelper
from MarketData.FundList import Fund
from MarketData.MarketDataPlotter import MarketDtaPlotter
import Globals.Functions as gf
import Globals.Variables as gv

fund = Fund("GB00B5N99561", "Artemis Global Income Fund Inc")
# Much quicker to save data first for multiple runs
fromYahoo = False
data = gf.getData(fund, gv.startDate, gv.endDate, fromYahoo)
data = data.reset_index()
helper = MarketDataHelper(data, gv.startDate, gv.endDate)
plotter = MarketDtaPlotter(helper)
plotter.PlotSNS("Date", "Close", fund.fullName)
