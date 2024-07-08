import pandas as pd


def preprocess(csv_file, api_data):
    #drivers_df = pd.read_csv('../Data/drivers.csv')
    df = pd.DataFrame(csv_file)
    combined_df = pd.merge(api_data, df, on='driver_number', how='left')
    combined_df.fillna(0, inplace=True)
    return combined_df


def preprocess_sessions(csv_file, session_data):
    #drivers_df = pd.read_csv('../Data/drivers.csv')
    df = pd.DataFrame(csv_file)
    combined_df = pd.merge(session_data, df, on='session_key', how='left')
    combined_df.fillna(0, inplace=True)
    return combined_df