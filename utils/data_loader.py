import pandas as pd


def load_driver_data(csv_path='Data/drivers.csv'):
    return pd.read_csv(csv_path)


def combine_dataframes(dfs):
    return pd.concat(dfs, axis=1)