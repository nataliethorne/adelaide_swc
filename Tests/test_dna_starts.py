
# start with the function you want to test
def dna_starts_with(st1,st2):
    if 'N' in st1:
        raise Exception("Contains invalid bases")
    return st1[0:len(st2)]==st2

# now the test function for the function you want to test
def test_dna_starts_with_itself():
    dna='acgtgtcgat'
    assert dna_starts_with(dna, dna)

def test_dna_starts_with_single_base_pair():
    dna='acgt'
    assert dna_starts_with(dna,'a')

def test_dna_is_shorter_than_query():
    dna='gtca'
    assert not dna_starts_with(dna,"gtcat")

#def test_contains_invalid_bases():
#    dna='gtNa'
#    assert  

# now implement the tests
test_dna_starts_with_itself()
test_dna_starts_with_single_base_pair()
test_dna_is_shorter_than_query()

# then go to this directory and type nosetests into the command line
