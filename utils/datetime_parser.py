from datetime import datetime, timedelta

import pytz
from dateutil import parser


def get_date_from_datetime_str(date_str):
    datetime_obj = convert_str_to_datetime(date_str)
    return datetime_obj.date()


def get_time_from_datetime_str(date_str):
    datetime_obj = convert_str_to_datetime(date_str)
    return datetime_obj.time()


def convert_str_to_datetime(date_str):
    return parser.parse(date_str)


def get_current_datetime():
    return datetime.now().astimezone(pytz.utc)


def get_next_expiry_date_by_seconds(seconds):
    return get_current_datetime() + timedelta(seconds=seconds)
