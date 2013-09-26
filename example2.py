
###########################
# how to write a function
###########################

def sum_two_numbers(first_number,second_number):
    result = first_number + second_number
    return(result)

print sum_two_numbers(4,9)


# you can have namespaces too

# given a string 'dna', replace all 'N', return the GC-content

def GCcontent(dna):
    if not isinstance(dna,str):     # could have used isstring(dnaif !isinstance
        str(dna)
    # don't expect N's in DNA sequence, remove them before counting GC content
    dna.replace('N',"")
    numGs = dna.count('G')
    numCs = dna.count('C')
    # get proportion of G's and C's, remember to introduce a float into the calculation so that division will give float result
    GC_content = (numGs + numCs)/float(len(dna))
    # you can return multiple objects from the function
    return(GC_content,len(dna))

# This is how to save the mulitple results from calling GCcontent
dna, len_dna = GCcontent("GCTAGAGACTNTGNAC")


# A useful small function for changing the first element in a list to something
def change_list(a_list, to_change="I changed this"):
    a_list[0] = to_change

# examples of how to use change_list function
a = [1,2,3,4]
change_list(list(a))
change_list(a, "something else")
print a



    
