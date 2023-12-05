from Base.BaseDataHelper import BaseDataHelper
from MarketData.FundList import Fund
import Globals.Functions as gf
import Globals.Variables as gv

fund = Fund("GB00B5N99561", "Artemis Global Income Fund Inc")

fromYahoo = True
data = gf.getData(fund, gv.startDate, gv.endDate, fromYahoo)
helper = BaseDataHelper("/Data/Yahoo/", fund.fullName + "_" + gv.startDate + "_" + gv.endDate + ".csv", data)
helper.SaveDataFrame()
