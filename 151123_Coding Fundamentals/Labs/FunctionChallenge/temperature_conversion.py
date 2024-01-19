'''
Write a function that takes a temperature in degrees Celsius as user-input and converts to Fahrenheit.
'''

def temp_conversion(temp_celsius):

    temp_fahrenheit=(temp_celsius*9/5)+32

    return temp_fahrenheit


if __name__ == '__main__':

    temp_celsius=float(input('Please enter a temperature in degrees Celsius: '))

    temp_fahrenheit=temp_conversion(temp_celsius)

    print(f'{temp_celsius} degrees Celsius is {temp_fahrenheit} degrees Fahrenheit')