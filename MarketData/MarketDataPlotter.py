import matplotlib.pyplot as plt
import seaborn as sns
from Base.BasePlotter import BasePlotter


class MarketDtaPlotter(BasePlotter):
    def plot_sns(self, col1: str, col2: str, title="", fontsize=10, pointsize=1):
        plt.figure(figsize=(14, 5))
        sns.set_style("ticks")
        sns.lineplot(data=self.helper.get_data_frame(), x=col1, y=col2, color='firebrick')
        sns.despine()
        plt.title(title, size='x-large', color='blue')
        plt.show()
