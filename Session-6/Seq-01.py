class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases):
        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.strbases = strbases
        print("New sequence created!")

    def __str__(self): #this method is useful to print the object
        """Method called when the object is being printed"""
        # -- We just return the string with the sequence
        return self.strbases

    def len(self): #this method is useful if someone wants to know the length of th sequence
        """Calculate the length of the sequence"""
        return len(self.strbases)

class Gene(Seq): #this is inheritance (the gene class inherits the behaviour and methods of the seq class). when we define the g objects, it jumps into the init method of the seq class
    """This class is derived from the Seq Class
       All the objects of class Gene will inherite
       the methods from the Seq class
    """
    def __init__(self, strbases, name=""): #name of the gene
        # -- Call first the Seq initilizer and then the Gene init method
        super().__init__(strbases) #As the Gene is also a Seq, for creating a Gene first we should call the init function from the Seq class. We do it by calling the super().init(strbases) method
        self.name = name
        print("New gene created")

    def __str__(self): #we can override (re-implement the methods used in the seq class)
        """Print the Gene name along with the sequence"""
        return self.name + "-" + self.strbases

# Main program
# Create objects of the class Seq
s1 = Seq("AGTACACTGGT")
s2 = Seq("CGTAAC")
g = Gene("CGTAAC", "FRAT1")

# -- Printing the objects
print(f"Sequence 1: {s1}")
print(f"  Length: {s1.len()}")
print(f"Sequence 2: {s2}")
print(f"  Length: {s2.len()}")
print(f"Gene: {g}")
print(f"  Length: {g.len()}")