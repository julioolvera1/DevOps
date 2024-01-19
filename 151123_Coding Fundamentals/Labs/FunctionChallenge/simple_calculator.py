'''
Write a function that takes 2 numbers as user input and then adds/subtracts/multiplies them and prints out the results.
Eg; if user enters 10 and 5 the print-out should read "sum is x, sub is y and multiply is z".
'''


def calculate(num1, num2):

    num_sum=num1+num2

    num_sub=num1-num2

    num_mult=num1*num2

    print(f'Sum is {num_sum}, sub is {num_sub} and multiply is {num_mult}')

    return num_sum, num_sub, num_mult


if __name__ == '__main__':

    num1=int(input('Please enter the first number: '))
    num2=int(input('Please enter the second number: '))

    calculate(num1,num2)