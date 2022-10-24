class Team():
    
    def __init__(self, team_name, line_1, line_2, line_3):
        #for simplicity each team will consist of 3 full lines.
        self.team_name = team_name
        self.line_1 = line_1
        self.line_2 = line_2
        self.line_3 = line_3
        
    def __repr__(self):
        #, {self.line_1}, {self.line_2}, {self.line_3}
        return f'{self}'
    
    def __str__(self):
        #Returns just the team name, If you want the full team list, use print_team.
        return f'Team :{self.team_name}'
    
    def print_team(self):
        return f"""This team({self.team_name}) contains - 
                    Line 1: {self.line_1}; 
                    Line 2: {self.line_2}; 
                    Line 3: {self.line_3}"""
    
    #Added for more functionality, If a team needs a line, it can be added (up to 3 lines)
    def add_line(self, line):
        if self.line_1 == None:
            self.line_1 = line
        elif self.line_2 == None:
            self.line_2 = line
        elif self.line_3 == None:
            self.line_3 = line
        else:
            print('All lines for this team are full.')
    
    #Check how many lines the team has.        
    def get_num_lines(self):
        if self.line_1 == None:
            return None
        elif self.line_1 != None and self.line_2 == None:
            return 1
        elif self.line_1 != None and self.line_2 != None and self.line_3 == None:
            return 2
        else:
            return 3
   
    #TODO: Add more functionality