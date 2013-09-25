import sys
#print sys.argv

# 1. get list of the arguments to python
my_list = sys.argv[1:]
#my_list = sys.argv
#my_list = my_list[1:len(my_list)]

# 2. sort the list

my_list.sort()

# 3. join all the words except the last

#my_list_last=my_list[-1]
#my_list_firstpart=my_list[0:-1]

#my_len=len(my_list)
#my_list_firstpart=my_list[0:(my_len-1)]
#joined_list=', '.join(my_list_firstpart)

joined_list=','.join(my_list[0:-1])

# 4. capitalise the first letter

joined_list=joined_list.capitalize()


# 5. append the word "and" and the last word


joined_list += ' and ' + my_list[-1] + '.'
#joined_list += my_list_last
#joined_list += "."

# 6. print the results
print joined_list

