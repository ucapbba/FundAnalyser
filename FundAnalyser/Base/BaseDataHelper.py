'''
BaseDataHelper (:mod:`FundAnalyser.Base.BaseDataHelper`)
========================================================

.. currentmodule:: FundAnalyser.Base.BaseDataHelper

The :mod:`FundAnalyser.Base.BaseDataHelper` module provides functionality data manipulation
Functions
---------

.. autoclass:: BaseDataHelper

'''


import string
from numpy import ndarray, void, loadtxt
from pandas import DataFrame
import os

import pandas as pd


class BaseDataHelper:
    """For importing and manipulating file data"""
    myDataFrame: DataFrame
    myArray: ndarray

    def __init__(self, _path: string, _fname: string, _myDataFrame: DataFrame = None):
        self.path = _path
        self.filename = _fname
        self.myDataFrame = _myDataFrame
    
    def CreateDataFrame(self):
        '''
        Creates a dataframe from a Numpy array
        '''
        df = DataFrame(self.myArray)
        self.myDataFrame = df

    def GetDataFrame(self):
        '''
        Return internal dataframe member
        '''
        return self.myDataFrame

    def GetFilePath(self) -> string:
        '''
        return filepath
        '''
        return self.path + self.filename

    def LoadToArray(self) -> void:
        '''
        Populate array data from filepath
        '''
        cwd = os.getcwd()
        filePath = self.GetFilePath()
        self.myArray = loadtxt(cwd + filePath)
        
    def LoadCSVtoDF(self):
        '''
        Create dataframe from a CSV
        '''
        cwd = os.getcwd()
        filePath = self.GetFilePath()
        self.myDataFrame = pd.read_csv(cwd + filePath)

    def SaveDataFrame(self) -> void:
        '''
        Save dataframe
        '''
        cwd = os.getcwd()
        filePath = self.GetFilePath()
        self.myDataFrame.to_csv(cwd + filePath)
        
    def TruncateArray(self, size: int) -> void:
        '''
        Truncates the array up to size
        '''
        newArray = self.myArray[:size]
        self.myArray = newArray

    def GetArray(self) -> ndarray:
        '''
        Return array member variable
        '''
        return self.myArray
