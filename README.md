# FundAnalyser

See [Example.ipynb](https://github.com/ucapbba/FundAnalyser/blob/main/Example.ipynb) for example usage

See sample report for fund comparison and warning sheet See sample report in [Data/Reports/FundReport.xls](https://github.com/ucapbba/FundAnalyser/blob/b62e5dc04e58542541ce6073d98dbc514e63740d/Data/Reports/FundReport.xls)

Uses yahoo price data to generate simple reports in Excel 

Add funds in FundList (ISIN used to ask Yahoo) - the units can be passed to analyse actual position value
Add additional analysers in FundDataAnalysers and then add these as indicators in the Fund - these indicators will be published to the report
The report contains the indicators and a warnings tab populated based on acceptable global values (e.g. max vol, max loss etc)


