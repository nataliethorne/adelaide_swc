# create a script that accepts an integer
import sys

input_int = int(sys.argv[1])

mod_int = input_int % 2

# could also do elif

if mod_int == 0:
    print "is even"  # must be indented
else:
    print "is odd"


if input_int > 0 and input_int < 100:
    print "between 0 and 100" 

# for loop in python

fruits = ['apple','orange','strawberry']

for fruit in fruits:
    print "I am a " + fruit + "."

for fruit in fruits:
    print "number of letters in " + fruit + " is " + str(len(fruit)) + "."


# while loops
# line by line, read in each line and do analysis

reader = open('fruits.txt', 'r')
line = reader.readline()
#print line

while line != '':  # is empty string then it's the end of the file
    print line
    line = reader.readline()



#
iter = 0
while iter < 10
    iter += 1


