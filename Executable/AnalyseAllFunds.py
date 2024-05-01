from FundAnalyser.MarketData.FundList import FundList
import FundAnalyser.Globals.Functions as gf
import FundAnalyser.Globals.Variables as gv
from FundAnalyser.Report.ReportGenerator import FundReportGenerator

fundList = FundList()
gf.PopulateAllFundData(gv.startDate, gv.endDate, fundList)
# gf.PlotAllFundData(fundList)
fundList = gf.GetAllFundIndicators(fundList)
reportGenerator = FundReportGenerator(fundList)
reportGenerator.WriteToExcel("FundReport")
