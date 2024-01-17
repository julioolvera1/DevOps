'''
Calculate the average of three exam marks  
- If the average mark is: o >= 65 output a "Pass" 
- If it is  < 65 output a "Fail"  
'''

# Input the marks for a student for Math, English and ICT exams.    
# Marks should be an integer between 0 and 100. 
# Use a for loop until the user enters a valid mark.

while True:
    math_mark=int(input('Enter Math mark:\t'))
    if math_mark>=0 and math_mark<=100:
        break
    else:
        print('Please enter a valid mark between 0 and 100')
    
while True:
    english_mark=int(input('Enter English mark:\t'))
    if english_mark>=0 and english_mark<=100:
        break
    else:
        print('Please enter a valid mark between 0 and 100')

while True:
    ict_mark=int(input('Enter ICT mark:\t'))
    if ict_mark>=0 and ict_mark<=100:
        break
    else:
        print('Please enter a valid mark between 0 and 100')

# Calculate the average of the three marks
average_mark = (math_mark + english_mark + ict_mark) / 3
print(f'Average mark is {average_mark}')

if average_mark >= 65:
    print('Overall result: Pass')
else:
    print('Overall result: Fail')
