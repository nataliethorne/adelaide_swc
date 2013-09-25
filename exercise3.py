#Exercise 3:
input_string = "GATCAGTCGATCGACTGCTAGCTAGCTAGTACGGCGTATA"

#create a dictionary in the following format:


#{'G': (# of occurences in the string),
#'A': ...
#}


numGs = input_string.count('G')
numCs = input_string.count('C')
numTs = input_string.count('T')
numAs = input_string.count('A')

seq_dict = {'G':numGs,'C':numCs, 'T':numTs, 'A':numAs}

GC_content = (numGs + numCs)/float(len(input_string))

#print the dictionary

print seq_dict

print GC_content
