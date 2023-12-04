import yfinance as yf
from MarketData.FundList import FundList
from MarketData.MarketDataHelper import MarketDataHelper
from MarketData.MarketDataPlotter import MarketDtaPlotter

fundList = FundList()
fund = fundList.GetFund("Artemis")
startDate = '2023-06-01'
endDate = '2023-12-01'

data = yf.download(fund.ISIN, startDate, endDate)

data = data.reset_index()
dataHelper = MarketDataHelper(data, startDate, endDate)
hasFullDatesRange = dataHelper.HasFullDatesRange()

plotter = MarketDtaPlotter(dataHelper)
plotter.PlotSNS("Date", "Close", fund.fullName)
plotter.plotScatter("Date", "Close", fund.fullName)
