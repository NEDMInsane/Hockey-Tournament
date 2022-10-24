from random import randint
import TeamCreator
#TODO: Add more functionality, players and teams have stats and staminas, teams have actual seeds based on skill.
#Instead of randomly assiging scores, run a simulation of a game using stats and fatigues.

def create_tournament():
    #Full tournament consists of 32 teams. 1st plays last.
    seeds = []
    while len(seeds) < 32:
        new_seed = TeamCreator.create_team()
        seeds.append(new_seed)
    #print(f'Tournament = {seeds}')
    return seeds


def play_round(matchup):
    #Play a round
    scores = {}
    winners = []
    for teams in matchup:
        #Give each matchup team a score
        scores[teams[0]] = randint(0, 5)
        scores[teams[1]] = randint(0, 5)
        #If the first team, in the tuple, wins add them to winner
        if scores[teams[0]] > scores[teams[1]]:
            winners.append(teams[0])
        #If the second team, in the tuple, wins add them to the winner
        elif scores[teams[0]] < scores[teams[1]]:
            winners.append(teams[1])
        #If they Tie add them both back to the winners
        else:
            winners.append(teams[0])
            winners.append(teams[1])
    return winners
    

def play_tournament(seeds):
    #TODO: Play all teams to pick a winner.
    #If seeds are more than 1 teams still need to play, if seeds is 1 that means a winner is picked.
    while len(seeds) > 1:
        rounds = len(seeds) // 2
        matchups = []
        i = 0
        while i != rounds:
                #Match each team correctly, first plays last, second play second to last, etc.
                matchups.append((seeds[i], seeds[len(seeds) - 1 - i]))
                i = i + 1
        #give matchup to play_round and repopulate the seeds with the winners from the round.
        seeds = play_round(matchups)
    return seeds

winner = play_tournament(create_tournament())
print(f'{winner[0].team_name} Won!')
print(f'{winner[0].print_team()}')