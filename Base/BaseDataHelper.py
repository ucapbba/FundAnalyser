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
        df = DataFrame(self.myArray)
        self.myDataFrame = df

    def GetDataFrame(self):
        return self.myDataFrame

    def GetFilePath(self) -> string:
        return self.path + self.filename

    def LoadToArray(self) -> void:
        cwd = os.getcwd()
        filePath = self.GetFilePath()
        self.myArray = loadtxt(cwd + filePath)
        
    def LoadCSVtoDF(self):
        cwd = os.getcwd()
        filePath = self.GetFilePath()
        self.myDataFrame = pd.read_csv(cwd + filePath)

    def SaveDataFrame(self) -> void:
        cwd = os.getcwd()
        filePath = self.GetFilePath()
        self.myDataFrame.to_csv(cwd + filePath)
        
    def TruncateArray(self, size: int) -> void:
        newArray = self.myArray[:size]
        self.myArray = newArray

    def GetArray(self) -> ndarray:
        return self.myArray
