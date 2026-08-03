import os
from MarketData.FundList import FundList
import xlwt
import Globals.Variables as gv


class FundReportGenerator:
    fund_list: FundList

    def __init__(self, fund_list: FundList):
        self.fund_list = fund_list

    def write_to_excel(self, filename):
        book = xlwt.Workbook()
        filename = filename + "_" + "_" + gv.start_date + "_" + gv.end_date + ".xls"
        self.create_indicators_sheet(book)
        self.create_warnings_sheet(book)
        cwd = os.getcwd()
        book.save(cwd + "/Data/Reports/" + filename)

    def create_warnings_sheet(self, book: xlwt.Workbook):
        sh_warnings = book.add_sheet("Warnings")
        sh_warnings.write(0, 0, "Fund")
        sh_warnings.write(0, 1, "Warning Messages")
        row = 1
        for fund_key, fund in self.fund_list.items():
            if not fund.indicators:
                sh_warnings.write(row, 0, fund_key)
                sh_warnings.write(row, 1, "No Indicators found for fund")
                row += 1
                continue
            if fund.indicators[gv.ABS_GROWTH] < gv.MIN_GROWTH:
                sh_warnings.write(row, 0, fund_key)
                sh_warnings.write(row, 1, "abs growth is below 10%")
                row += 1
            if fund.indicators[gv.VOL] > gv.MAX_VOL:
                sh_warnings.write(row, 0, fund_key)
                sh_warnings.write(row, 1, "volatility is high")
                row += 1
            if fund.indicators[gv.AVE_VALUE] > gv.MAX_VAL:
                sh_warnings.write(row, 0, fund_key)
                sh_warnings.write(row, 1, "High allotment in fund")
                row += 1
            if fund.indicators[gv.AVE_VALUE] < gv.MIN_VAL:
                sh_warnings.write(row, 0, fund_key)
                sh_warnings.write(row, 1, "Low allotment in fund")
                row += 1
        sh_warnings.col(0).width = 5000
        sh_warnings.col(1).width = 10000

    def create_indicators_sheet(self, book: xlwt.Workbook):
        sh_indicators = book.add_sheet("Indicators")
        row = 0
        column = 1
        for fund_key, fund in self.fund_list.items():
            if row == 0:  # add column names
                sh_indicators.write(0, 0, "Fund")
                for indicator_key, indicator in fund.indicators.items():
                    sh_indicators.write(0, column, indicator_key)
                    column += 1
                row = 1
            column = 0
            sh_indicators.write(row, column, fund_key)
            column += 1
            for indicator_key, indicator in fund.indicators.items():
                sh_indicators.write(row, column, indicator)
                column += 1

            row += 1

        for column in range(6):
            sh_indicators.col(column).width = gv.COL_WIDTH
