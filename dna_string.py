
# gc_content
# base_count('G')
# reverse_complement
# G<->C
# T<->A


# useage:  
# import dna_string
# x = dna_string.DNAString("GATCC")
# x.gc_content()
# x.reverse_complement()


class DNAString:

    def __init__(self, sequence):   # sequence needs to be initially passed to self using init
        self.sequence = sequence
        #self.gc = gc_content()
        #self.rc = reverse_complement()
        #self.bases = {"A":base_count("A"), "T":base_count("T"),"G":base_count("G"),"C":base_count("C")}   

    def gc_content(self):
        '''Count GC content as a proportion of non N bases'''
        countN = self.base_count('N')
        new_self = self.sequence.replace('N',"")
        return (self.base_count("G") + self.base_count("C"))/float(len(new_self))
       

    def base_count(self,base):
        return self.sequence.count(base)

    def reverse_complement(self):
        rc_self=self.sequence
        rc_self=rc_self.replace("A","t")
        rc_self=rc_self.replace("T","a")
        rc_self=rc_self.replace("G","c")
        rc_self=rc_self.replace("C","g")
        rc_self=rc_self[::-1].upper()    # 5:2:-1  goes 2 to 5 and then -1 indicates going in a reverse direction
        return rc_self


