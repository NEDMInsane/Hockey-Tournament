import Team
import Player
import Line
import Gens
#Generate a full team that consists of 3 lines
#Each line consists of 5 Players.
#Each player gets a position, 3 as forwards, 2 as defence.
#TODO: Add a goalie......

def set_player_position(player_list):
    #Set the player as a player object(FWD or DEF)
    line_list = []
    for ply in player_list:
        if len(line_list) < 2:
            ply = Player.Forward(ply)
            ply.position('Forward')
            line_list.append(ply)
        else:
            ply = Player.Defense(ply)
            ply.position('Defence')
            line_list.append(ply)
    #print(f'line_list = {line_list} its lenth is {len(line_list)}.')
    return Line.Line.from_list(line_list)
        
def add_lines_to_team(team_name, lines):
    team_name = Team.Team(team_name, lines[0], lines[1], lines[2])
    #print(team_name)
    return team_name

def create_team():
    team_name = Gens.gen_team_name()
    player_list = []
    line = []
    
    while len(line) != 3:
        while len(player_list) != 5:
            player_list.append(Gens.player_name_gen())
        line.append(set_player_position(player_list))
        player_list = []
    
    return add_lines_to_team(team_name, line)