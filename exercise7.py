
# Given a string 'filename', write a function which opens that file, iterates over all sequences, and writes a bit of stats about each sequence:

#print the name of each sequence
#count of Ns
#GC content

# import file called sys.py
import sys
# get the second argument from the command line ( the first will be the file exercise7.py )
f_name=str(sys.argv[1])

def get_Ns_GC(filename):
    fasta_file=open(filename, 'r')
    line = fasta_file.readline()
    while line != '':
        if line.startswith(">"):
            seq_name=line.lstrip(">").rstrip("\n")
            print seq_name 
        else:
            GC, numN = GCcontent(line)
            print GC, numN
        line = fasta_file.readline()
                


def GCcontent(dna):
    if not isinstance(dna,str):     # could have used isstring(dnaif !isinstance
        str(dna)
    countN = dna.count('N')
    dna.replace('N',"")
    numGs = dna.count('G')
    numCs = dna.count('C')
    GC_content = (numGs + numCs)/float(len(dna))
    return(GC_content,countN)

get_Ns_GC(f_name)


