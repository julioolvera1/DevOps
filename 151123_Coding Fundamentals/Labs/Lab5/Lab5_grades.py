'''
Your task is to present some statistics on the following students' grades that are read from a file.
'''
import statistics as stat

## Grades as string
data="100,30,53,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51,72,59,14,50,55,32,23,24,25,37,28,39,30,33,35,40,34,41,43,94,95,59,98,99,44,45,47,48,49,53,61,63,69,75,77,60,83"

grades=data.split(",")

## Up until this point the grades are strings. We need to convert them to integers
grades_num=[int(grade) for grade in grades]

min_grade=min(grades_num)
max_grade=max(grades_num)

print(f'The minimum grade is {min_grade}')
print(f'The maximum grade is {max_grade}')

average_grade=sum(grades_num)/len(grades_num)
average_grade=round(average_grade,2)
print(f'The average grade is {average_grade:.2f}')

average_grade=stat.mean(grades_num)
print(f'The average grade is {average_grade:.2f}')

median_grade=stat.median(grades_num)
print(f'The median grade is {median_grade:.2f}')






