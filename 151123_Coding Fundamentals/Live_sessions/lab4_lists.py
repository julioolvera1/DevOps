'''
Practice using Lists through a series of 7 small exercises in order to become familiar with Lists
'''

ages = [12,18,33,84,45,67,12,82,95,16,
    10,23,43,29,40,34,30,16,44,69,70,74,38,
    65,36,83,50,11,79,64,78,37,3,8,68,22,4,
    60,33,82,45,23,5,18,28,99,17,81,14,88,
    50,19,59,7,44,93,35,72,25,63,11,69,11,
    76,10,60,30,14,21,82,47,6,21,88,46,78,
    92,48,36,28,51]


ages_length = len(ages)

for idx,age in enumerate(ages,0):
    print(f'Original age: {age}')
    ages[idx]=age+1
    print(f'New age: {ages[idx]}')

    if (age>16 and age < 65):
        print(f'Age {age} is between 16 and 65')
    else:
        print(f'Age {age} is not between 16 and 65, removing from list')
        ages.pop(idx)


count_1625=0
for age in ages:
    if (age>=16 and age<=25):
        count_1625=count_1625+1

print(f'There are {count_1625} ages between 16 and 25')

ages.sort()
print(ages)

proportion_1625=(count_1625/len(ages))*100
print(f'The proportion of ages between 16 and 25 is {proportion_1625}%')

