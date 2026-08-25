import numpy as np
from pandas import DataFrame
from concurrent.futures import ThreadPoolExecutor, as_completed
from MarketData.FundDataAnalyser import FundAnalyser
from MarketData.FundList import FundList
from MarketData.FundList import Fund
from MarketData.MarketDataPlotter import MarketDtaPlotter
from MarketData.MarketDataHelper import MarketDataHelper
from Base.BaseDataHelper import BaseDataHelper
import yfinance as yf


def _fetch_fund_data(fund_key, fund, start_date, end_date):
    data = get_data(fund, start_date, end_date)
    data = data.reset_index()
    # yfinance returns MultiIndex columns (Price, Ticker); flatten so 'Date'/'Close' are plain columns
    data.columns = data.columns.get_level_values(0)
    market_cap = get_market_cap(fund)
    return fund_key, fund, data, market_cap


def populate_all_fund_data(start_date, end_date, fund_list: FundList, max_workers: int = 8) -> np.void:
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {}
        for fund_key, fund in fund_list.items():
            print(f"Submitted: {fund_key}")
            futures[executor.submit(_fetch_fund_data, fund_key, fund, start_date, end_date)] = fund_key

        for future in as_completed(futures):
            fund_key = futures[future]
            try:
                fund_key, fund, data, market_cap = future.result()
            except BaseException as e:
                print(f"[{fund_key}] FAILED: {e}")
                continue

            fund.set_market_cap(market_cap)
            data_helper = MarketDataHelper(data, start_date, end_date)
            if data_helper.is_empty():
                print(f"[{fund_key}] FAILED: empty data from Yahoo")
                continue
            data_helper.has_full_dates_range()
            fund.set_data_helper(data_helper)
            print(f"[{fund_key}] OK")


def plot_all_fund_data(fund_list: FundList) -> np.void:
    for fund_key, fund in fund_list.items():
        if fund.data_helper is None:
            continue
        plotter = MarketDtaPlotter(fund.data_helper)
        plotter.plot_sns("Date", "Close", fund.full_name)
        # plotter.plot_scatter("Date", "Close", fund.full_name)


def get_all_fund_indicators(fund_list: FundList) -> FundList:
    for fund_key, fund in fund_list.items():
        if fund.data_helper is None:
            continue
        analyser = FundAnalyser(fund)
        mean = analyser.close_mean
        abs_growth = analyser.get_abs_growth()
        growth_on_mean = analyser.get_growth_on_mean()
        vol = analyser.get_volatility()
        # analyser.add_rolling_average()
        fund.set_indicators(mean, abs_growth, growth_on_mean, vol)
        print(fund.full_name + " " + str(abs_growth) + " " + str(growth_on_mean) + " " + str(vol))
    return fund_list


def get_data(fund: Fund, start_date, end_date, from_yahoo=True) -> DataFrame:
    if from_yahoo is True:
        try:
            data = yf.download(fund.isin, start_date, end_date, progress=False)
            return data
        except BaseException:
            print("Problem accessing Yahoo data for " + fund.full_name)
    else:
        helper = BaseDataHelper("/Data/Yahoo/", fund.full_name + "_" + start_date + "_" + end_date + ".csv")
        helper.load_csv_to_df()
        return helper.get_data_frame()


def get_market_cap(fund: Fund):
    # mutual funds have no market cap; yfinance returns None for those tickers rather than raising
    try:
        return yf.Ticker(fund.isin).fast_info.get("marketCap")
    except BaseException:
        return None