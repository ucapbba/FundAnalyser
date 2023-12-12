import string
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from Base.BaseDataHelper import BaseDataHelper
import matplotlib


class BasePlotter():
    """Generic base plotting functions"""
    def __init__(self, _helper: BaseDataHelper):
        self.helper = _helper

    def plotScatter(self, col1: string, col2: string, title="", fontsize=10, pointsize=1):
        df = self.helper.GetDataFrame()
        Xarray = np.asarray(df[col1])
        Yarray = np.asarray(df[col2])
        fig, ax = plt.subplots()
        plt.title(title, fontsize=fontsize)
        plt.xlabel(col1, fontsize=fontsize)
        plt.ylabel(col2, fontsize=fontsize)
        plt.xticks(fontsize=fontsize)
        plt.yticks(fontsize=fontsize)
        ax.scatter(Xarray, Yarray, s=pointsize)
        plt.show()

    def plot2Scatter(self, col1: string, col2: string, col3: string, col4: string, title="", fontsize=15):
        df = self.helper.GetDataFrame()
        Xarray = np.asarray(df[col1])
        Yarray = np.asarray(df[col2])
        X2array = np.asarray(df[col3])
        Y2array = np.asarray(df[col4])
        fig = plt.figure()
        ax1 = fig.add_subplot(221)
        ax2 = fig.add_subplot(222)
        ax1.scatter(Xarray, Yarray, s=0.001, color="purple")
        ax2.scatter(X2array, Y2array, s=0.001, color="purple")
        # axis
        ax1.set_xlabel(col1, fontsize=fontsize)
        ax1.set_ylabel(col2, fontsize=fontsize)
        ax2.set_xlabel(col3, fontsize=fontsize)
        plt.show()

    def PlotColourMesh(self, title=""):
        font = {'family': 'serif',
                'weight': 'normal',
                'size': 10}
        matplotlib.rc('font', **font)  # increase all font size
        fig, ax = plt.subplots(1, 1, figsize=(14, 8))
        XRESI = self.helper.XRESI
        YRESI = self.helper.YRESI
        ZRESI = self.helper.ZRESI
        _min = self.helper.min
        _max = self.helper.max
        ax.pcolormesh(XRESI, YRESI, ZRESI, norm=LogNorm(vmin=_min, vmax=_max),\
                      rasterized=True, shading='gouraud')
        ax.set(title=title)
        plt.axis('off')
        plt.show()
