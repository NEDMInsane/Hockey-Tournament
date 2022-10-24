#Generation Script to generate Team names and Player Names.
from random import randint as rand
import csv

team_names_file = 'TeamNames.csv'
team_name_list = []
player_names_file = 'PlayerNames.csv'
player_name_list = []


def team_name_init():
    #Generate Team name list
    global team_name_list
    with open(team_names_file, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        next(reader) #We dont want the header.
        for line in reader:
            team_name_list.append(line)
            
def player_name_init():
    #Generate Player name list
    global player_name_list
    with open(player_names_file, 'r') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        next(reader) #We dont want the header.
        for line in reader:
            player_name_list.append(line[1])           
            
def gen_team_name():
    #Output a team name.
    global team_name_list
    if len(team_name_list) < 1:
        team_name_init()
    rnum = rand(0, len(team_name_list) - 1)
    team_name = team_name_list.pop(rnum)
    return team_name


def player_name_gen():
    #Output a Player name.
    global player_name_list
    if len(player_name_list) < 1:
        player_name_init()
    rnum = rand(0, len(player_name_list) - 1)
    player_name = player_name_list.pop(rnum)
    return player_name
