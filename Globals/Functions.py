import numpy as np
from pandas import DataFrame
from MarketData.FundList import FundList
from MarketData.FundList import Fund
from MarketData.MarketDataPlotter import MarketDtaPlotter
from MarketData.MarketDataHelper import MarketDataHelper
from Base.BaseDataHelper import BaseDataHelper
import yfinance as yf


def PopulateAllFundData(startDate, endDate, fundList: FundList) -> np.void:
    for fundKey, fund in fundList.myDict.items():
        fund = fundList.GetFund(fundKey)
        print("Processing key " + fundKey)
        data = getData(fund, startDate, endDate)
        data = data.reset_index()
        dataHelper = MarketDataHelper(data, startDate, endDate)
        if dataHelper.IsEmpty():
            print("Problem accessing Yahoo data for " + fundKey)
            continue
        dataHelper.HasFullDatesRange()
        fund.setDataHelper(dataHelper)


def PlotAllFundData(fundList: FundList) -> np.void:
    for fundKey, fund in fundList.myDict.items():
        if fund.dataHelper is None:
            continue
        plotter = MarketDtaPlotter(fund.dataHelper)
        plotter.PlotSNS("Date", "Close", fund.fullName)
        # plotter.plotScatter("Date", "Close", fund.fullName)


def getData(fund: Fund, startDate, endDate, fromYahoo=True) -> DataFrame:
    if fromYahoo is True:
        try:
            data = yf.download(fund.ISIN, startDate, endDate)
        except BaseException:
            print("Problem accessing Yahoo data for " + fund.fullName)
            return data
        else:
            helper = BaseDataHelper("/Data/Yahoo/", fund.fullName + "_" + startDate + "_" + endDate + ".csv")
            helper.LoadCSVtoDF()
            return helper.GetDataFrame()
