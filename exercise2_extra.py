# given two sentences, find the # of letters they have in common, and
#the number of letters that are unique to each
#e.g.:
#string1 = 'a sentence'
#string2 = 'a different sentence'
#print (# of letters in common)
#print (# of letters unique to sentence 1)
#print (# of letters unique to sentence 2)


import sys
my_sentences=sys.argv[1:]
first_sentence=my_sentences[0]
second_sentence=my_sentences[1]

first_letters=set(''.join(first_sentence).upper())


