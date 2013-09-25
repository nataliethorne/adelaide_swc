# define data structures

# rodents
# add comment here
# class a blueprint for what is in the object
# defines the methods that can be used
# tag ID: A8025
# size (oz)
# sightings per month

# is_large (large means > 5 oz)
# is_small (small means < 3 oz)
# capture(month)

# in python use: import rodent
# x = rodent.Rodent()
# dir(x)

# first create empty methods then fill up over time

class Rodent:

    def __init__(self, tag_id, size):
        self.tag_id = tag_id
        self.size = size
        self.sightings_per_month = {}   # i.e. '1':5  month 1 had 5 sightings

    def is_large(self):
        # return True if size is > 5 oz   useage: x.is_large()
        return(self.size > 5)              
    
    def is_small(self):
        # return True if size is < 3 oz
        return(self.size < 3)

    def plot(self):
        # return the letter of the plot at which this rodent was first captured
        return(self.tag_id[0])

    def capture(self, month):
        # I've captured this rodent once a month  useage: x.capture(2)
        if month not in self.sightings_per_month:
            self.sightings_per_month[month] = 0
        self.sightings_per_month[month] += 1
