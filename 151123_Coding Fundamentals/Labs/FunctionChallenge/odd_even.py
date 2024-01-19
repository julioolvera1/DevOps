'''
Write a function that accepts a number as user input and returns whether the number is odd or even. 
'''

def odd_even(num):

    ## if it can be divided by 2, without a remainder, it's even
    if num%2==0:
        print(f'{num} is even')
    else:
        print(f'{num} is odd')

    return None


if __name__ == '__main__':

    num=int(input('Please enter a number: '))

    odd_even(num)