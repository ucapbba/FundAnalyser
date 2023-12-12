import string
from Base.BasePlotter import BasePlotter
import matplotlib.pyplot as plt
import seaborn as sns


class MarketDtaPlotter(BasePlotter):
    def PlotSNS(self, col1: string, col2: string, title="", fontsize=10, pointsize=1):
        plt.figure(figsize=(14, 5))
        sns.set_style("ticks")
        sns.lineplot(data=self.helper.GetDataFrame(), x=col1, y=col2, color='firebrick')
        sns.despine()
        plt.title(title, size='x-large', color='blue')
        plt.show()
