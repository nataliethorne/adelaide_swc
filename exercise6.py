
# get IPouts from header

#import sys
#search_me=sys.argv

search_me = "IPouts"

# 13th column
pitching = open('Pitching.csv', 'r')
line = pitching.readline()

header_values = line.split(",")
col_num=int(header_values.index(search_me))

linecount = 0
ipout = list()
while line != '':
    line = pitching.readline()
    line_list = line.split(",")
    value = float(line_list[col_num])
    ipout.append(value)

print ipout

