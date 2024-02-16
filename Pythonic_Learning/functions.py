## Optional arguments

def my_function(name, age, *opt):

    print(f'Name: {name}')
    print(f'Age: {age}')
    for idx,arg in enumerate(opt,1):
        print(f'Optional {idx}: {arg}')



if __name__ == '__main__':
    print('module_as_script.py executed as a script')
    my_function('John', 25)

else:
    print('functions.py imported as a module')
    print(f'Here is the list of functions: {dir()}')
