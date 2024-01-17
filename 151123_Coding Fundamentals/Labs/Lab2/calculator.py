number1=float(input('Enter first number:'))
number2=float(input('Enter second number:'))

print('Available operations')

print('1.Add (+)')
print('2.Subtract (-)')
print('3.Multiply (*)')
print('4.Divide (/)')
print('5.Square (s)')

operation=input('Enter operation:')

if operation=='+':
    result=number1+number2
elif operation=='-':
    result=number1-number2
elif operation=='*':
    result=number1*number2
elif operation=='/':
    result=number1/number2
elif operation=='s':
    result=number1**2
else:
    print('Invalid operation')
    result=None

print('Result is:',result)