#Sam has been dumped by his girlfriend so he's gone into the local milk 
#bar to drown his sorrows. He has a budget, and there's a choice of three (or more) 
#milkshakes, 
#differently priced. The barman says, "What can I fix you?" and Sam can reply with a 
#number corresponding 
#to the relevant flavour - this list is displayed every iteration. 
#If he enters Q, he quits and leaves; the barman wishes him well in his search for love. 
#If he orders but can't pay he's thrown out.

sams_budget=50
sam_enough_budget=None
# input_from_sam='P'

milkshake_prices={
    'chocolate':5,
    'vanilla':8,
    'berries':7,
    'apple':2,
    # 'tequila':49,
}

milkshakes_list=list(milkshake_prices.keys())

counter=0
while (sams_budget > 0):
    print('='*65)

    if sams_budget <= 0:
        print(f'Your budget is gone, sorry!')
    else:
        print(f'Your budget is {sams_budget}')
        print(f'This is the price list: {milkshake_prices}')

    sams_order=input(f'\nWhat can I fix you? Write flavour as: \n {milkshakes_list}\n')
    print('-'*65)

    if sams_order not in milkshakes_list:
        if sams_order =='Q':
            break
        print(f'This flavour is not available, try again!')
        continue

    sams_order_cost=milkshake_prices[sams_order]
    print(f'Your selection costs: {sams_order_cost}')

    ## Update the condition for budget
    sam_enough_budget = sams_order_cost < sams_budget

    if sam_enough_budget == False:
        print("You don't have enough money for this flavour, choose a different one, you have 3 attempts")
        counter=counter+1
        if counter>3:
            break
        continue

    sams_budget=sams_budget-sams_order_cost

    print(f'Your budget is now {sams_budget}')

    print('\nPress Q to exit the bar\n')
    print('='*65)

    