'''
Write a function that converts a user inputted string into uppercase. 
'''

def str_convert(string):

    string_upper=string.upper()

    return string_upper


if __name__ == '__main__':

    string=input('Please enter a string: ')

    print(f'Your string in uppercase is {str_convert(string)}')