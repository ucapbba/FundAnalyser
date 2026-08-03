from numpy import ndarray, void, loadtxt
from pandas import DataFrame
import os

import pandas as pd


class BaseDataHelper:
    """For importing and manipulating file data"""
    data_frame: DataFrame
    array: ndarray

    def __init__(self, path: str, fname: str, data_frame: DataFrame | None = None):
        self.path = path
        self.filename = fname
        self.data_frame = data_frame

    def create_data_frame(self):
        df = DataFrame(self.array)
        self.data_frame = df

    def get_data_frame(self):
        return self.data_frame

    def get_file_path(self) -> str:
        return self.path + self.filename

    def load_to_array(self) -> void:
        cwd = os.getcwd()
        file_path = self.get_file_path()
        self.array = loadtxt(cwd + file_path)

    def load_csv_to_df(self):
        cwd = os.getcwd()
        file_path = self.get_file_path()
        self.data_frame = pd.read_csv(cwd + file_path)

    def save_data_frame(self) -> void:
        cwd = os.getcwd()
        file_path = self.get_file_path()
        self.data_frame.to_csv(cwd + file_path)

    def truncate_array(self, size: int) -> void:
        new_array = self.array[:size]
        self.array = new_array

    def get_array(self) -> ndarray:
        return self.array
