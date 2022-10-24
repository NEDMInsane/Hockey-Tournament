class Line():
    
    def __init__(self, left, center, right, ld, rd):
        #Pass in player objects to fill out a complete line
        self.left = left
        self.center = center
        self.right = right
        self.ld = ld
        self.rd = rd
    
    @classmethod    
    def from_list(cls, line_list):
    
        return cls(line_list[0], line_list[1], line_list[2], line_list[3], line_list[4])
        
    def __repr__(self):
        return f'{self}, {self.left}, {self.center}, {self.right}, {self.ld}, {self.rd}'
    
    def __str__(self):
        return f'This line --> Left Wing: {self.left}, Center: {self.center}, Right Wing: {self.right}, Left Defence: {self.ld}, Right Defence: {self.rd}'    
    
    #TODO: add more functionality