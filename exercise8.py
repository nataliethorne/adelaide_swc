#Test dna_starts_with
#True id second argument is a preifs of the first 
#False otherwise

#dna_starts_with('actggt','act') => True
#dna_starts_with('actggt','act') => False


def dna_starts_with(input_dna,start_dna):
    return input_dna[0:len(start_dna)]==start_dna
#    return input_dna.startswith(start_dna)


