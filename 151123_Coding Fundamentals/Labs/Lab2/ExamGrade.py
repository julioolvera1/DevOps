'''
write code to input a grade between 1 and 100 
and display the exam grade according to a set of rules.
'''

exam_mark = int(input('Enter exam mark:'))

## Exam mark  must be an integer between 1 and 100 
## otherwise display an error message

if exam_mark < 1 or exam_mark > 100:
    print('Error: marks must be between 1 and 100')
elif exam_mark >= 71:
    print('Distinction')
elif exam_mark >= 61:
    print('Merit')
elif exam_mark >= 50:
    print('Pass')
else:
    print('Fail')




