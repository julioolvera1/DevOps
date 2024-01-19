'''
Write a function that has a list with some common passwords as strings (stored as a variable) inside it. 
Have an input statement that asks the user for a password. 
If the input matches any string from the list print Use a safer password {password} is compromised, 
else print password is safe. 
'''

list_common_passwords=[
    'password',
    'password123',
    '123456',
    'mypassword',
    'opensesame',
]


def check_password(password):

    if password in list_common_passwords:
        print(f'Use a safer password, {password} is compromised!!')
    else:
        print('Password is safe')


if __name__ == '__main__':

    password=input('Please enter a password: ')
    check_password(password)
