
from nucleotideContent import nucleotideContent
Tests =[
['ACGTGT', {'A':1,'C':1,'G':2,'T':2}],
['CAGGTT', {'A':1,'C':1,'G':2,'T':2}]
]
# could put in more tests i.e. lower case, NA's, N's, other letters.

passes = 0    
for (i, (seq, bases)) in enumerate(Tests):    
    if nucleotideContent(seq) == bases: 
        passes += 1    
    else:    
        print('test %d failed' %i)    
    
print '%d/%d tests passed' %(passes, len(Tests))


