# count=0
# while count<5:
#     name=input("What's your name?")1
#     print(f'{name} is awesome')
#     count=count+1


# for count in range(5):
#     name=input("What's your name?")
#     print(f'{name} is awesome')


names = [input("What's your name?") for count in range(5)]
_ = [print(f'{name} is awesome') for name in names]

# names = [print(f"{input('What is your name?')} is awesome") for count in range(5)]
