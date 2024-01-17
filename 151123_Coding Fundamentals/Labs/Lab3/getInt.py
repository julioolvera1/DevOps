'''
Ask the user to input an integer between a minimum and maximum values.
If the user fails to enter an acceptable value for three times then you stop asking!
'''

min_value=int(input('Enter minimum value:\t'))
max_value=int(input('Enter maximum value:\t'))

count_attempts=0
while True:
    user_input=int(input('Please enter an integer:\t'))

    if (user_input<=min_value or user_input>=max_value):
        print('The value entered is outside of the limits of min and max values. Please try again!')
        count_attempts=count_attempts+1
        if count_attempts==3:
            print(None)
            break
    else:
        print(f'{user_input} is within the limits of min and max values, thanks!')
        break
        


