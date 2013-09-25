
# how to write a function

def sum_two_numbers(first_number,second_number):
    result = first_number + second_number
    return(result)

print sum_two_numbers(4,9)


# you can have namespaces too

# given a string 'dna', replace all 'N', return the GC-content

def GCcontent(dna):
    if not isinstance(dna,str):     # could have used isstring(dnaif !isinstance
        str(dna)
    dna.replace('N',"")
    numGs = dna.count('G')
    numCs = dna.count('C')
    GC_content = (numGs + numCs)/float(len(dna))
    return(GC_content,len(dna))

dna, len_dna = GCcontent("GCTAGAGACTNTGNAC")



def change_list(a_list, to_change="I changed this"):
    a_list[0] = to_change

a = [1,2,3,4]
change_list(list(a))
change_list(a, "something else")
print a



    
