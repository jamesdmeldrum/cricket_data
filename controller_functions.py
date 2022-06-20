import os
import sys
import json
import tools
import datetime

format_file = 'file_format.json'
file_format = json.load(open(format_file))

###########################################################
### Function to narrow data to teams involved
### input:  f = list of rows from data file
###         rest of args: country name in string format
### output: list of rows with data narrowed down
###########################################################
def teams(f,
        home_team = None,
        away_team = None,
        any_team_1 = None,
        any_team_2 = None):

    if (home_team == away_team == any_team_1 == any_team_2 == None):
        return f

    returnlist = []

    home_index = file_format["home_team"]
    away_index = file_format["away_team"]

    for row in f:
        row_list = tools.convert_raw_row(row)

        if (row_list[home_index] in (any_country1, any_country2, home_country))
        and (row_list[away_index] in (any_country1, any_country2, away_country)):
            returnlist.append(row)

    return returnlist

###########################################################
### Function to narrow data to wining teams
### input:  f = list of rows from data file
###         team = name of winning team in string format
### output: list of rows with data narrowed down
###########################################################
def winner(f,
        team = None):

    if (team == None):
        return f

    returnlist = []

    winner_index = file_format["winner"]

    for row in f:
        row_list = tools.convert_raw_row(row)

        if (row_list[winner_index] == team):
            returnlist.append(row)

    return returnlist

###########################################################
### Function to narrow data to venue played at
### input:  f = list of rows from data file
###         ground = name of ground match is played at in string format
### output: list of rows with data narrowed down
###########################################################
def venue(f,
        ground = None):

    if (ground == None):
        return f

    returnlist = []

    venue_index = file_format["venue"]

    for row in f:
        row_list = tools.convert_raw_row(row)

        if (row_list[venue_index] == ground):
            returnlist.append(row)

    return returnlist

###########################################################
### Function to narrow data to date range
### input:  f = list of rows from data file
###         start_date = earliest match date in datetime format
###         end_date = latest match date in datetime format
### output: list of rows with data narrowed down
###########################################################
def date(f,
        start_date = None,
        end_date = None):

    if (start_date == end_date == None):
        return f

    returnlist = []

    date_index = file_format["date"]

    for row in f:
        row_list = tools.convert_raw_row(row)

        row_date = tools.convert_to_date_ymd(row_list[date_index])

        if (start_date != None):
            if (end_date != None):
                if (row_date >= start_date)
                    and (row_date <= end_date):
                    returnlist.append(row)
            else:
                if (row_date >= start_date):
                    returnlist.append(row)
        else if (end_date != None):
            if (row_date <= end_date):
                returnlist.append(row)

    return returnlist
