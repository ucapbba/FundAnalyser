import os
from MarketData.FundList import FundList
import xlwt
import Globals.Variables as gv

class FundReportGenerator:
    fundList: FundList
    
    def __init__(self, _fundList: FundList):
        self.fundList = _fundList
    
    def WriteToExcel(self, filename):
        book = xlwt.Workbook()
        filename = filename+"_"+"_"+gv.startDate+"_"+gv.endDate+".xls"
        self.CreateIndicatorsSheet(book)
        self.CreateWarningsSheet(book)
        
        cwd = os.getcwd()
        book.save(cwd + "/Data/Reports/" + filename)

    def CreateWarningsSheet(self, book: xlwt.Workbook):
        shWarnings = book.add_sheet("Warnings")
        shWarnings.write(0, 0, "Fund")
        shWarnings.write(0, 1, "Warning Messages")
        row = 1
        for fundKey, fund in self.fundList.myDict.items():
            if bool(fund.indicators) is False:
                shWarnings.write(row, 0, fundKey)
                shWarnings.write(row, 1, "No Indicators found for fund")
                row += 1
                continue
            if fund.indicators["absGrowth"] < -10:
                shWarnings.write(row, 0, fundKey)
                shWarnings.write(row, 1, "abs growth is below 10%")
                row += 1
            if fund.indicators["volatility"] > 10:
                shWarnings.write(row, 0, fundKey)
                shWarnings.write(row, 1, "volatility is high")
                row += 1

    def CreateIndicatorsSheet(self, book: xlwt.Workbook):
        shIndicators = book.add_sheet("Indicators")
        row = 0
        column = 1
        for fundKey, fund in self.fundList.myDict.items():
            if row == 0:  # add column names
                shIndicators.write(0, 0, "Fund")
                for indicatorKey, indicator in fund.indicators.items():
                    shIndicators.write(0, column, indicatorKey)
                    column += 1
                row = 1
            column = 0
            shIndicators.write(row, column, fundKey)
            column += 1
            for indicatorKey, indicator in fund.indicators.items():
                shIndicators.write(row, column, indicator)
                column += 1
            row += 1
