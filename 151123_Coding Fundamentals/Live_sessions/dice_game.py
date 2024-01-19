import dice

total=0
for i in range(2):
    dice_result=dice.roll_dice()
    print(f'You rolled a {dice_result}')

    total+=dice_result
print(f'Total is {total}')