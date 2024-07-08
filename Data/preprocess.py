import pandas as pd


def preprocess_sessions(drivers_csv, session_data):
    drivers_df = pd.read_csv(drivers_csv)
    combined_df = pd.merge(session_data, drivers_df, on='session_key', how='left')
    combined_df.fillna(0, inplace=True)
    return combined_df


def preprocess(main_df, api_data, suffix='_api'):
    combined_df = pd.merge(main_df, api_data, on='driver_number', how='left', suffixes=('', suffix))
    combined_df.fillna(0, inplace=True)
    return combined_df
