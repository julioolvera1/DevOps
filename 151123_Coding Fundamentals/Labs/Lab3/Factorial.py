user_input=int(input('Please enter an integer:\t'))

## Calculate the factorial of the number entered by the user
## and store the result in a variable called result
result=1
factorial=user_input
factorials_list=[]

while factorial>0:
    factorials_list.append(factorial)
    result=result*factorial
    factorial=factorial-1

## Display the result
print(f'The list of factorials of {user_input} is {factorials_list}')
print(f'The factorial of {user_input} is {result}')

