## Optional arguments

def my_function(name, age, *opt):

    print(f'Name: {name}')
    print(f'Age: {age}')
    for idx,arg in enumerate(opt,1):
        print(f'Optional {idx}: {arg}')



if __name__ == '__main__':
    my_function('John', 25)
