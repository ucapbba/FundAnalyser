from MarketData.FundList import FundList
import Globals.Functions as gf
import Globals.Variables as gv

fundList = FundList()
gf.PopulateAllFundData(gv.startDate, gv.endDate, fundList)
gf.PlotAllFundData(fundList)
