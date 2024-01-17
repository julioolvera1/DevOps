'''
input a grade and calculate the grade 
but this time you'll take into account the different levels of studies.
'''

exam_mark = int(input('Enter exam mark:'))

## Exam mark  must be an integer between 1 and 100 
## otherwise display an error message

if exam_mark < 1 or exam_mark > 100:
    print('Error: marks must be between 1 and 100')

else:

    student_level = int(input('Enter student level (1 or 2):'))

    if student_level==1:
        if exam_mark >= 71:
            print('Distinction')
        elif exam_mark >= 61:
            print('Merit')
        elif exam_mark >= 50:
            print('Pass')
        else:
            print('Fail')
    
    elif student_level==2:
        if exam_mark >= 66:
            print('Distinction')
        elif exam_mark >= 51:
            print('Merit')
        elif exam_mark >= 40:
            print('Pass')
        else:
            print('Fail')

