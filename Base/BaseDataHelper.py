import string
from numpy import ndarray, void, loadtxt
from pandas import DataFrame
import os


class BaseDataHelper:
    """For importing and manipulating file data"""
    myDataFrame: DataFrame
    myArray: ndarray

    def __init__(self, _path: string, _fname: string):
        self.path = _path
        self.filename = _fname

    def CreateDataFrame(self):
        df = DataFrame(self.myArray)
        self.myDataFrame = df

    def GetDataFrame(self):
        return self.myDataFrame

    def GetFilePath(self) -> string:
        return self.path + self.filename

    def LoadToArray(self) -> void:
        cwd = os.getcwd()
        filePath = BaseDataHelper.GetFilePath(self)
        self.myArray = loadtxt(cwd + filePath)

    def TruncateArray(self, size: int) -> void:
        newArray = self.myArray[:size]
        self.myArray = newArray

    def GetArray(self) -> ndarray:
        return self.myArray
