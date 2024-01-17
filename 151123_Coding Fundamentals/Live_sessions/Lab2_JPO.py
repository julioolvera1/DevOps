'''
In this lab you'll gain the experience of using conditional 
if…elif control flow statements in Python. 
'''

person_age=int(input('What is your age?'))

if person_age >= 18:
    print('You are in category A')
elif person_age >= 16:
    print('You are in category B')
else:
    print('You are in category C')


