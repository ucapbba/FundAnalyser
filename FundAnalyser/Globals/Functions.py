'''
Global Functions (:mod:`FundAnalyser.Globals.Functions`)
========================================================

.. currentmodule:: FundAnalyser.Globals.Functions

The :mod:`FundAnalyser.Globals.Functions` module is the main work centre of the repository


Functions
---------

.. autofunction:: PopulateAllFundData
.. autofunction:: GetAllFundIndicators
.. autofunction:: getData

'''


import string
import numpy as np
from pandas import DataFrame
from FundAnalyser.MarketData.FundDataAnalyser import FundAnalyser
from FundAnalyser.MarketData.FundList import FundList
from FundAnalyser.MarketData.FundList import Fund
from FundAnalyser.MarketData.MarketDataPlotter import MarketDtaPlotter
from FundAnalyser.MarketData.MarketDataHelper import MarketDataHelper
from FundAnalyser.Base.BaseDataHelper import BaseDataHelper
import yfinance as yf


def PopulateAllFundData(startDate: string, endDate: string, fundList: FundList) -> np.void:
    '''Responsible for looping over the FundList and getting the market data
    
    Parameters
    ----------
    startDate : string in the form 'YYYY-MM-DD'
    endDate : string in the form 'YYYY-MM-DD'
    fundList : the class FundList contains the list of funds
    
    ''' 
    for fundKey, fund in fundList.myDict.items():
        fund = fundList.GetFund(fundKey)
        print("Processing key " + fundKey)
        data = getData(fund, startDate, endDate)
        data = data.reset_index()
        dataHelper = MarketDataHelper(data, startDate, endDate)
        if dataHelper.IsEmpty():
            print("Problem accessing Yahoo data for " + fundKey)
            print("")
            continue
        dataHelper.HasFullDatesRange()
        fund.setDataHelper(dataHelper)
        print(" ")


def PlotAllFundData(fundList: FundList) -> np.void:
    for fundKey, fund in fundList.myDict.items():
        if fund.dataHelper is None:
            continue
        plotter = MarketDtaPlotter(fund.dataHelper)
        plotter.PlotSNS("Date", "Close", fund.fullName)
        # plotter.plotScatter("Date", "Close", fund.fullName)


def GetAllFundIndicators(fundList: FundList) -> FundList:
    '''Responsible for looping over the FundList and calculting the indicators''' 
    for fundKey, fund in fundList.myDict.items():
        if fund.dataHelper is None:
            continue
        analyser = FundAnalyser(fund)
        mean = analyser.closeMean
        absGrowth = analyser.GetAbsGrowth()
        growthOnMean = analyser.GetGrowthOnMean()
        vol = analyser.GetVolatility()
        # analyser.AddRollingAverage()
        fund.SetIndicators(mean, absGrowth, growthOnMean, vol)
        print(fund.fullName + " " + str(absGrowth) + " " + str(growthOnMean) + " " + str(vol))
    return fundList


def getData(fund: Fund, startDate, endDate, fromYahoo=True) -> DataFrame:
    '''Gets the data for a single fund''' 
    if fromYahoo is True:
        try:
            data = yf.download(fund.ISIN, startDate, endDate)
            return data
        except BaseException:
            print("Problem accessing Yahoo data for " + fund.fullName)
    else:
        helper = BaseDataHelper("/Data/Yahoo/", fund.fullName + "_" + startDate + "_" + endDate + ".csv")
        helper.LoadCSVtoDF()
        return helper.GetDataFrame()
