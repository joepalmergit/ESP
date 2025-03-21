from datetime import datetime
import pandas as pd

def date_format_valid(date, date_format):
    """Check if a given date string conforms to a specified date format"""
    valid = True

    try:
        pd.to_datetime(date, format=date_format)

    except ValueError:
        valid = False

    return valid

def parse_date(date, date_format):
    """Parse a date string into a datetime object using a specified format"""
    parsed_date = datetime.strptime(date, date_format)

    return parsed_date

def date_range_valid(date_1, date_2):
    """"Validate that the first date is earlier than the second date"""
    valid = False

    if date_1 < date_2:
        valid = True

    return valid
