import os
import sys
import datetime


def convert_raw_row(row):
    return row.strip("\n").split(",")

def convert_to_date_ymd(string_date):
    date_list = string_date.split("/")

    return datetime.datetime(date_list[0],date_list[1],date_list[2])
