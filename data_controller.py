import os
import sys
import controller_functions as cfn
import tools
import datetime
import pandas as pd
import json

datafilename = '../male_odi_combined_infos.csv'

dataframe = pd.read_csv(datafilename, on_bad_lines='skip')
dataframe["date"] = pd.to_datetime(dataframe["date"])
dataframe = dataframe.sort_values(by = "date")

aus_home = cfn.series_number(cfn.date_range(cfn.teams(dataframe, anyteam_1 = "Australia"), start_date = datetime.datetime(2013,12,1), end_date = datetime.datetime(2014,4,1)), 3)

print(aus_home)
