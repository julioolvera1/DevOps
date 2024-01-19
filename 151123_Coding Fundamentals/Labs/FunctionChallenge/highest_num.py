'''
Write a function that takes 3 numbers as arguments, and returns the highest number.
'''

def highest_num(num1, num2, num3):

    list_nums=[num1, num2, num3]

    max_num=max(list_nums)

    return max_num


if __name__ == '__main__':

    num1=int(input('Please enter the first number: '))
    num2=int(input('Please enter the second number: '))
    num3=int(input('Please enter the third number: '))

    max_num=highest_num(num1, num2, num3)

    print(f'The highest number is {max_num}')