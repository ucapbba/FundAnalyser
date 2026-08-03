import Globals.Variables as gv
from MarketData.Fund import Fund
from Report.ReportGenerator import FundReportGenerator


# Fakes for xlwt's Workbook/Sheet, recording write()/col().width calls so the
# report-building logic can be tested without touching xlwt or the filesystem.
class FakeSheet:
    def __init__(self):
        self.cells = {}
        self.col_widths = {}

    def write(self, row, col, value):
        self.cells[(row, col)] = value

    def col(self, index):
        return _FakeColumn(self, index)


class _FakeColumn:
    def __init__(self, sheet, index):
        self._sheet = sheet
        self._index = index

    @property
    def width(self):
        return self._sheet.col_widths.get(self._index)

    @width.setter
    def width(self, value):
        self._sheet.col_widths[self._index] = value


class FakeBook:
    def __init__(self):
        self.sheets = {}

    def add_sheet(self, name):
        sheet = FakeSheet()
        self.sheets[name] = sheet
        return sheet


def MakeFund(fullName, **indicators):
    fund = Fund(ISIN="GB00000000", fullName=fullName)
    fund.indicators = indicators
    return fund


def test_CreateWarningsSheet_flagsFundWithNoIndicators():
    fund = Fund(ISIN="GB00000000", fullName="No Indicators Fund")
    reportGenerator = FundReportGenerator({"NoIndicators": fund})
    book = FakeBook()

    reportGenerator.CreateWarningsSheet(book)

    sheet = book.sheets["Warnings"]
    assert sheet.cells[(1, 0)] == "NoIndicators"
    assert sheet.cells[(1, 1)] == "No Indicators found for fund"


def test_CreateWarningsSheet_flagsLowGrowthHighVolatilityAndHighAllotment():
    fund = MakeFund(
        "Risky Fund",
        **{
            gv.ABS_GROWTH: gv.MIN_GROWTH - 1,
            gv.VOL: gv.MAX_VOL + 1,
            gv.AVE_VALUE: gv.MAX_VAL + 1,
        },
    )
    reportGenerator = FundReportGenerator({"Risky": fund})
    book = FakeBook()

    reportGenerator.CreateWarningsSheet(book)

    messages = [value for (row, col), value in book.sheets["Warnings"].cells.items() if col == 1 and row != 0]
    assert "abs growth is below 10%" in messages
    assert "volatility is high" in messages
    assert "High allotment in fund" in messages


def test_CreateWarningsSheet_flagsLowAllotment():
    fund = MakeFund(
        "Small Fund",
        **{
            gv.ABS_GROWTH: 5,
            gv.VOL: 1,
            gv.AVE_VALUE: gv.MIN_VAL - 1,
        },
    )
    reportGenerator = FundReportGenerator({"Small": fund})
    book = FakeBook()

    reportGenerator.CreateWarningsSheet(book)

    messages = [value for (row, col), value in book.sheets["Warnings"].cells.items() if col == 1 and row != 0]
    assert messages == ["Low allotment in fund"]


def test_CreateWarningsSheet_noWarningsForHealthyFund():
    fund = MakeFund(
        "Healthy Fund",
        **{
            gv.ABS_GROWTH: 5,
            gv.VOL: 1,
            gv.AVE_VALUE: 500,
        },
    )
    reportGenerator = FundReportGenerator({"Healthy": fund})
    book = FakeBook()

    reportGenerator.CreateWarningsSheet(book)

    dataRows = [row for row, _ in book.sheets["Warnings"].cells if row != 0]
    assert dataRows == []


def test_CreateIndicatorsSheet_writesHeaderAndFundRow():
    fund = MakeFund("Some Fund", **{gv.MEAN: 100.0, gv.ABS_GROWTH: 5.0})
    reportGenerator = FundReportGenerator({"SomeFund": fund})
    book = FakeBook()

    reportGenerator.CreateIndicatorsSheet(book)

    sheet = book.sheets["Indicators"]
    assert sheet.cells[(0, 0)] == "Fund"
    assert sheet.cells[(0, 1)] == gv.MEAN
    assert sheet.cells[(0, 2)] == gv.ABS_GROWTH
    assert sheet.cells[(1, 0)] == "SomeFund"
    assert sheet.cells[(1, 1)] == 100.0
    assert sheet.cells[(1, 2)] == 5.0
    assert sheet.col_widths[0] == gv.COL_WIDTH
