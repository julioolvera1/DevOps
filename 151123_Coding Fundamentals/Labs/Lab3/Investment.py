'''
Calculate how many years it will take an 
initial investment of £100 to grow 
to a target value of £1000 if the interest rate is 10%.
'''

initial_investment = float(input('Enter initial investment:\t'))

target_value = float(input('Enter target value:\t'))

interest_rate = float(input('Enter interest rate:\t'))

## Calculate increase in value per year
# new_value_year1 = initial_investment * (1 + interest_rate/100) 


## Calculate the number of years

## Start at year 0 (present)
years = 0
new_value = initial_investment
while new_value < target_value:
    ## Annual increase in value
    new_value = new_value * (1 + interest_rate/100)
    years = years + 1
    print(f'Year {years}: {new_value}')

print(f'Total number of years required to grow from {initial_investment} to {target_value} at {interest_rate}% is {years}')
