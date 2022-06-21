import os
import sys
import json
import tools
import datetime

format_file = 'file_format.json'
file_format = json.load(open(format_file))


###############################################################################
### function that returns true only if all supplied team values are equal to
### the row of data supplied
###     input:  row = row of data (list)
###             home_team = desired home team (string)
###             away_team = desired away team (string)
###             anyteam_1/2 = desired team home or away (string)
###     output: True if all conditions are met or no conditions supplied
###             False if any condition is not met
###############################################################################
def teams(row,
        home_team = None,
        away_team = None,
        anyteam_1 = None,
        anyteam_2 = None):

    if (home_team == away_team == anyteam_1 == anyteam_2 == None):
        return True

    home_index = file_format["home_team"]
    away_index = file_format["away_team"]

    if (home_team != None and row[home_index] != home_team):
        return False

    if (away_team != None and row[away_index] != away_team):
        return False

    if (any_team_1 != None and anyteam_1 not in (home_team,away_team)):
        return False

    if (anyteam_2 != None and anyteam_2 not in (home_team,away_team)):
        return False

    return True


###############################################################################
### function that returns true only if match in row is from desired date range
###     input:  row = row of data (list)
###             start_date = earliest desired date (datetime)
###             end_date = latest desired date (datetime)
###     output: True if all conditions are met or no conditions supplied
###             False if any condition is not met
###############################################################################
def date_range(row,
        start_date = None,
        end_date = None):

    if (start_date == end_date == None):
        return True

    date_index = file_format["date"]

    row_date = tools.convert_to_date_ymd(row)

    if (start_date != None and row_date < start_date):
        return False

    if (end_date != None and row_date > end_date):
        return False

    return True


###############################################################################
### function that returns true only if match is won by desired team
###     input:  row = row of data (list)
###             winning = desired winning team (string)
###             not_winning = team not desired to win (string)
###     output: True if all conditions are met or no conditions supplied
###             False if any condition is not met
###############################################################################
def winner(row,
        winning = None,
        not_winning = None):

    if (winning == not_winning == None):
        return True

    winner_index = file_format["winner"]

    if (winning != None and row[winner_index] != winning):
        return False

    if (not_winning != None and row[winner_index] == not_winning):
        return False

    return True


###############################################################################
### function that returns true only if match takes place in desired location
###     input:  row = row of data (list)
###             venue = desired ground match is played at (string)
###             city = desired city match is played at (string)
###     output: True if all conditions are met or no conditions supplied
###             False if any condition is not met
###############################################################################
def location(row,
        venue = None,
        city = None):

    if (venue == city == None):
        return True

    venue_index = file_format["venue"]
    city_index = file_format["city"]

    if (venue != None and row[venue_index] != venue):
        return False

    if (city != None and row[city_index] != city):
        return False

    return True


###############################################################################
### function that returns true only if match is desired number in series
###     input:  row = row of data (list)
###             series_no = desired series match number (int)
###     output: True if all conditions are met or no conditions supplied
###             False if any condition is not met
###############################################################################
def series_number(row,
        series_no = None):

    if (series_no == None):
        return True

    series_no_index = file_format["series_number"]

    if (series_no != None and row[series_no_index] != series_no):
        return False

    return True
