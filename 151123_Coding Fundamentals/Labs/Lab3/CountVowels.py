'''
Input a word (a string).
Counts how many vowels are in the word.   
'''

word=input('Enter a word:\t')

vowels=['a','e','i','o','u']

count_vowels=0
for letter in word:
    if letter in vowels:
        print(f'\t{letter}')
        count_vowels=count_vowels+1

print(f'The number of vowels in {word} is {count_vowels}')
