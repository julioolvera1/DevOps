## Weight conversion app

weight_orig=float(input('Please enter weight as a number:\t'))
weight_units=input('Please enter whether using [kg] or [lb]:\t')

weight_units=weight_units.lower()

if weight_units == 'kg':
    weight_converted=weight_orig*2.20462
    print(f'Your weight in lbs is {weight_converted:.2f}')

elif weight_units == 'lb':
    weight_converted=weight_orig*0.453592
    print(f'Your weight in kg is \t{weight_converted:.2f}')

else:
    print(f'The weight units are not supported please try again!')
    



