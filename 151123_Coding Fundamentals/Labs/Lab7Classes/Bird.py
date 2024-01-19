'''
Create 3 classes, A bird parent class and then an Owl and Dodo class.
'''


class Bird:

    def __init__(self, name, species, color, can_fly):
        self.name=name
        self.species=species
        self.color=color
        self.can_fly=can_fly

    


class Owl(Bird):
    
    def __init__(self, name, species, color, can_fly, eye_color):
        super().__init__(name, species, color, can_fly)
        self.eye_color=eye_color
    

class Dodo(Bird):

    def __init__(self, name, species, color, can_fly, beak_size):
        super().__init__(name, species, color, can_fly)
        self.beak_size=beak_size


if __name__ == '__main__':

    ## Create an instance of the Owl class
    owl1=Owl('Hedwig', 'Snowy Owl', 'White', True, 'Yellow')
    print(f'{owl1.name} is a {owl1.species} and has {owl1.eye_color} eyes')

    ## Create an instance of the Dodo class
    dodo1=Dodo('Dod', 'Ancient Bird', 'Brown', False, 'Large')
    print(f'{dodo1.name} is a {dodo1.species} and has a {dodo1.beak_size} beak')



