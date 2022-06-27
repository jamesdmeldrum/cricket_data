import os
import sys
import datetime


def convert_raw_row(row):
    return row.strip("\n").split(",")

def convert_to_date_ymd(string_date):
    date_list = string_date.split("/")
    print(string_date, date_list)

    return datetime.datetime(int(date_list[0]),int(date_list[1]),int(date_list[2]))
