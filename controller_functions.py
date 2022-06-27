import os
import sys
import json
import tools
import datetime
import pandas as pd

format_file = 'file_format.json'
file_format = json.load(open(format_file))


###############################################################################
# function that returns rows of data that feature given teams
#     input:  dat = dataframe
#             home_team = desired home team (string)
#             away_team = desired away team (string)
#             anyteam_1/2 = desired team home or away (string)
#     output: all rows of data that meet given conditions
###############################################################################
def teams(dat,
        home_team = None,
        away_team = None,
        anyteam_1 = None,
        anyteam_2 = None):

    returndat = dat.copy()

    if (home_team == away_team == anyteam_1 == anyteam_2 == None):
        return dat

    if (home_team != None):
        returndat = returndat[returndat["home_team"] == home_team]

    if (away_team != None):
        returndat = returndat[returndat["away_team"] == away_team]

    if (anyteam_1 != None):
        returndat_a = returndat[returndat["home_team"] == anyteam_1]
        returndat_b = returndat[returndat["away_team"] == anyteam_1]
        returndat = returndat_a.append(returndat_b)

    if (anyteam_2 != None):
        returndat_a = returndat[returndat["home_team"] == anyteam_2]
        returndat_b = returndat[returndat["away_team"] == anyteam_2]
        returndat = returndat_a.append(returndat_b)

    return returndat.sort_values(by = "date")


###############################################################################
### function that returns true only if match in row is from desired date range
###     input:  row = row of data (list)
###             start_date = earliest desired date (datetime)
###             end_date = latest desired date (datetime)
###     output: True if all conditions are met or no conditions supplied
###             False if any condition is not met
###############################################################################
def date_range(dat,
        start_date = None,
        end_date = None):

    if (start_date == end_date == None):
        return dat

    returndat = dat.copy()

    if (start_date != None):
        returndat = returndat[returndat["date"] >= start_date]

    if (end_date != None):
        returndat = returndat[returndat["date"] <= end_date]

    return returndat


###############################################################################
### function that returns true only if match is won by desired team
###     input:  row = row of data (list)
###             winning = desired winning team (string)
###             not_winning = team not desired to win (string)
###     output: True if all conditions are met or no conditions supplied
###             False if any condition is not met
###############################################################################
def winner(dat,
        winning = None,
        not_winning = None):

    if (winning == not_winning == None):
        return dat

    returndat = dat.copy()

    if (winning != None):
        returndat = returndat[returndat["winner"] == winning]

    if (not_winning != None):
        returndat = returndat[returndat["winner"] != not_winning]

    return returndat


###############################################################################
### function that returns true only if match takes place in desired location
###     input:  row = row of data (list)
###             venue = desired ground match is played at (string)
###             city = desired city match is played at (string)
###     output: True if all conditions are met or no conditions supplied
###             False if any condition is not met
###############################################################################
def location(dat,
        venue = None,
        city = None):

    if (venue == city == None):
        return dat

    returndat = dat.copy()

    if (venue != None):
        returndat = returndat[returndat["venue"] == venue]

    if (city != None):
        returndat = returndat[returndat["city"] == city]

    return returndat


###############################################################################
### function that returns true only if match is desired number in series
###     input:  row = row of data (list)
###             series_no = desired series match number (int)
###     output: True if all conditions are met or no conditions supplied
###             False if any condition is not met
###############################################################################
def series_number(dat,
        series_no = None):

    if (series_no == None):
        return dat

    returndat = dat.copy()

    if (series_no != None):
        returndat = returndat[returndat["series_number"] == series_no]

    return returndat
