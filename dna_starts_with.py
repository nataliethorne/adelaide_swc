class UnknownBaseException(Exception)
    pass


# start with the function you want to test
def dna_starts_with(st1,st2):
    '''
    Input a dna string see if it starts with string 2.

    >>> dna_starts_with('actgt','actgt')
    True

    >>> dna_starts_with('a','a')
    True

    >>> try: dna_starts_with('ANT', 'A')
    ... except Exception as e: print e
    ... 
    Contains invalid bases

    >>> dna_starts_with('ANT','A')
    Traceback (most recent call last):
    ...
    Exception: Contains invalid bases

    >>> dna_starts_with("ag","agtc")
    Traceback (most recent call last):
    ...
    Exception: string 2 is longer than string 1

    '''

    if len(st2) > len(st1):
        raise Exception("string 2 is longer than string 1")

    if 'N' in st1:
        raise UnknownBaseException()
    return st1[0:len(st2)]==st2

    try:
        dna_starts_with('N','a')
    except UnknownBaseException as e: print "contains N"


# in order for doctests to work
if __name__ == '__main__':
    import doctest
    doctest.testmod()


# dir() to look at methods for a function
# IOError() to see what functions it works for

# for exceptions better to use try: and except IOError as e: print "wrong"

# can create our own exception class

