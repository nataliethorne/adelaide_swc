# read the content of the pg76.txt line by line
# get the length of each line and aggregate it
# Get the total number of lines in a file

page = open('pg76.txt', 'r')
line = page.readline()

linesum = 0
numlines = 0
while line != '':
    numlines +=1
    linesum = linesum + len(line)
    line = page.readline()

print "Number of characters on the page is " + str(linesum) + "."
print "Number of lines on the page is " + str(numlines) + "."

page.close()
