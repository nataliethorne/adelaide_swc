#Given an string (a sentence), find out how many unique letters A-Z it #contains, capital and lwoer case shouldnt be double-counted

#'AaAa'

#input: some string
#input_string = 'some string here'
#print (the number of unique letters in the string)

import sys
input_string = sys.argv[1:]
string1 = input_string[0]
string2 = input_string[1]

letters1 = set(string1.lower())
all_permitted_letters=set('abcdefghijklmnopqrstuvwxyz')
letters1=letters.intersection(all_letters)

letters2 = set(string2.lower())
letters2=letters.intersection(all_letters)

in_common = len(letters1.intersections(letters2))

print in_common
print(len(letters1) - in_common

print len(set(letters))

