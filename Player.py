class Player:
    
    def __init__(self, lastname):
        self.lastname = lastname
        self.stamina = (100, 100)
        
    def position(self, position):
        self.position = position
        
    def stats(self, stats=None):
        if stats is None:
            print('No stats passed.')
        else:
            self.stats = stats
        
    def increase_stamina(self, modifier):
        self.stamina[0] = self.stamina[0] + modifier, self.stamina[1]
        
    def reduce_stamina(self, modifier):
        self.stamina[0] = self.stamina[0] - modifier, self.stamina[1]
        
    def increase_base_stamina(self, modifier):
        self.staminae[1] = self.stamina[0], self.stamina[1] + modifier
        
    def reduce_base_stamina(self, modifier):
        self.stamina = self.stamina[0], self.stamina[1] - modifier
             
    def __repr__(self):
        return f'({self}, {self.lastname} Obj)'
    
    def __str__(self):
        return f'{self.lastname}'
    
    def get_stamina(self):
        return self.stamina[0]
    
    def get_stamina_base(self):
        return self.stamina[1]
    
    def replenish_stamina(self):
        self.stamina = self.stamina[1], self.stamina[1]
        
class Forward(Player):
    #TODO: create forward stats?
    pass

class Defense(Player):
    #TODO: create defense stats?
    pass
    
# center_1 = Player('Crosby')
# center_1.position('Center_Forward')
# print(center_1.get_stamina())
# print(center_1)
# print(center_1.position)
# center_1.reduce_base_stamina(2)
# print(center_1.get_stamina())
