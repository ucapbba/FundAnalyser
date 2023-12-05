from MarketData.FundList import FundList
import Globals.Functions as gf
import Globals.Variables as gv
from Report.ReportGenerator import FundReportGenerator

fundList = FundList()
gf.PopulateAllFundData(gv.startDate, gv.endDate, fundList)
# gf.PlotAllFundData(fundList)
fundList = gf.GetAllFundIndicators(fundList)
reportGenerator = FundReportGenerator(fundList)
reportGenerator.WriteToExcel("FundReport.xls")
