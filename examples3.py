
# boundary cases in testing code
# compare aerial photos of farm land 80's to present

# Use package called nose in python

# has a series of test files
# write functions begining with test_

# run nosetests from command line (not even in python)
# it will run all the tests and send a report

# how many tests, think about the boundary cases
# i.e. choose cost effective tests

# example dna_starts_with
# test_starts_with_itself()
# dna ='actgt'

# test_starts_with_single_base_pair()
# test_dna_is_shorter_than_query()

# write tests for dna_starts_with  in a seperate folder name the file test_dna_starts.py
# redirect terminal to the test folder and run the rests from the command line by typing the command nosetests
# do not forget to call the functions at the end of your py program

#I found that it's possible to import a function file (so you don't need to cut/paste the function definition into your test file). I put "import py_functions" (the name of my function file) at the top of the test_dna_starts_with.py file, and then ran nosetests from my code (not test) directory (the location of my function file). But I pointed nosetests to the test directory by running "nosetests ./test/" -- this seems to work for me

# import doctests 
# these test are embedded in the functions


########## In R!
# to do the same in R
# many - here's for example RUnit http://cran.r-project.org/web/packages/RUnit/index.html
# or "testthat" http://cran.r-project.org/web/packages/testthat/index.html

# You may find Diego's slides on dropcanvas helpful. See pg 30 (ish) of unit_diego.pdf


