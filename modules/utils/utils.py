# modules/utils/utils.py

import os
from datetime import datetime, timedelta


def get_last_date_downloaded(path):
    '''
    Return the last downloaded date, based on the CSV files in the directory.
    If no files are found, return the current month in "YYYY-MM-DD" format.
    '''
    current_month = datetime(datetime.today().year, datetime.today().month, 1).date()
    
    if not os.path.isdir(path):
        return current_month

    csv_files = sorted(f for f in os.listdir(path) if f.endswith(".csv"))
    if not csv_files:
        return current_month

    last_file = csv_files[-1]
    last_date_str = last_file.split("_")[-1].replace(".csv", "")
    last_date = datetime.strptime(last_date_str, "%Y-%m-%d").date()

    next_date = last_date + timedelta(days=1)
    return next_date


def get_dates_to_download(start_date):
    """Cria lista de datas a partir da última baixada até hoje"""
    dates_to_download = []
    today = datetime.today().date()
    
    while start_date <= today:
        dates_to_download.append(start_date.strftime("%Y-%m-%d"))
        start_date += timedelta(days=1)
    
    return dates_to_download