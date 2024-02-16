class Rabbit():
    LOCATION = 'Carrot Patch'
    def __init__(self, size, danger):
        self.size = size
        self.danger = danger

r1=Rabbit('small',True)
print(f'The rabbit, located in the {r1.LOCATION} is {r1.size} and {r1.danger}')

# class Knight():

#     def __init__(self, name, title, color):
#         self.name = name
#         self.title = title
#         self.color = color

#     @property
#     def name(self):
#         return self.name

#     @property
#     def color(self):
#         return self.color
    
#     @color.setter
#     def color(self, color):
#         self.color = color

# k1 = Knight('John', 'Sir', 'Blue')
# print(f'{k1.name} {k1.title} {k1.color} Knight')
# k1.color = 'Red'





