import time
from urllib.error import HTTPError
from urllib.parse import quote
from urllib.request import urlopen
import json
import pandas as pd


def get_intervals(session_key, interval):
    url = f'https://api.openf1.org/v1/intervals?session_key={session_key}&interval<{interval}'
    for i in range(5):
        try:
            response = urlopen(url)
            data = json.loads(response.read().decode('utf-8'))
            df = pd.DataFrame(data)
            return df
        except HTTPError as e:
            if e.code == 429:
                sleep_time = 2 ** i
                print(f"HTTP 429: Too Many Requests. Retrying in {sleep_time} seconds...")
                time.sleep(sleep_time)


def get_laps(session_key, driver_number, lap_number):
    url = f'https://api.openf1.org/v1/laps?session_key={session_key}&driver_number={driver_number}&lap_number={lap_number}'
    for i in range(5):
        try:
            response = urlopen(url)
            data = json.loads(response.read().decode('utf-8'))
            df = pd.DataFrame(data)
            return df
        except HTTPError as e:
            if e.code == 429:  # Too Many Requests
                sleep_time = 1 * (2 ** i)
                print(f"HTTP 429: Too Many Requests. Retrying in {sleep_time} seconds...")
                time.sleep(sleep_time)
            else:
                raise
    print(f"Failed to retrieve data for driver {driver_number}, lap {lap_number} after {5} attempts in session key {session_key}.")
    return pd.DataFrame()


def get_pit_data(session_key):
    url = f'https://api.openf1.org/v1/pit?session_key={session_key}'
    for i in range(5):
        try:
            response = urlopen(url)
            data = json.loads(response.read().decode('utf-8'))
            df = pd.DataFrame(data)
            return df
        except HTTPError as e:
            if e.code == 429:
                sleep_time = 2 ** i
                print(f"HTTP 429: Too Many Requests. Retrying in {sleep_time} seconds...")
                time.sleep(sleep_time)
            else:
                raise
    print(f"Failed to retrieve data for session {session_key}, after 5 attempts.")
    return pd.DataFrame()


def get_position(meeting_key, driver_number, position):
    response = urlopen(
        f'https://api.openf1.org/v1/position?meeting_key={meeting_key}&driver_number={driver_number}&position<={position}')
    data = json.loads(response.read().decode('utf-8'))
    df = pd.DataFrame(data)
    return df


def get_session(session_name, year):
    # response = urlopen(
    #     f'https://api.openf1.org/v1/sessions?country_name={country_name}&session_name=Sprint&year={year}')
    # data = json.loads(response.read().decode('utf-8'))
    # df = pd.DataFrame(data)
    # return df

    session_name_encoded = quote(session_name)
    url = f'https://api.openf1.org/v1/sessions?session_name={session_name_encoded}&year={year}'
    for i in range(5):
        try:
            response = urlopen(url)
            data = json.loads(response.read().decode('utf-8'))
            df = pd.DataFrame(data)
            return df
        except HTTPError as e:
            if e.code == 429:
                sleep_time = 2 ** i
                print(f"HTTP 429: Too Many Requests. Retrying in {sleep_time} seconds...")
                time.sleep(sleep_time)
            else:
                raise
    print(f"Failed to retrieve data for session {session_name}, {year} after 5 attempts.")
    return pd.DataFrame()


def get_stints(session_key):
    url = f'https://api.openf1.org/v1/stints?session_key={session_key}'
    for i in range(5):
        try:
            response = urlopen(url)
            data = json.loads(response.read().decode('utf-8'))
            df = pd.DataFrame(data)
            return df
        except HTTPError as e:
            if e.code == 429:
                sleep_time = 2 ** i
                print(f"HTTP 429: Too Many Requests. Retrying in {sleep_time} seconds...")
                time.sleep(sleep_time)
            else:
                raise
    print(f"Failed to retrieve data for session {session_key}, after 5 attempts.")
    return pd.DataFrame()


def get_weather(meeting_key, wind_direction, track_temperature):
    url = f'https://api.openf1.org/v1/weather?meeting_key={meeting_key}&wind_direction>={wind_direction}&track_temperature>={track_temperature}'
    for i in range(5):
        try:
            response = urlopen(url)
            data = json.loads(response.read().decode('utf-8'))
            df = pd.DataFrame(data)
            return df
        except HTTPError as e:
            if e.code == 429:
                sleep_time = 2 ** i
                print(f"HTTP 429: Too Many Requests. Retrying in {sleep_time} seconds...")
                time.sleep(sleep_time)
