#first, we define our class
class dog:
    #then we define the init function. It creates one instance of the class, it is a constructor
    def __init__(self, name, age): #the self is mandatory, it is like a handler of the object (the object would be ares/toby)
        self.name = name
        self.age = age

    def set_name(self, name):
        self.name = name
        print("This is {{, and i´m sitting down here".format(self.name))

    #def set_age(self, name):
    #def rollover(self):
    def sitdown(self):
        print("Yes, I will sit down")

ares = dog('ares', 10)
toby = dog('toby', 21)
#when there´s an object (ares/toby) python goes to the class and goes automatically to the init

#if we wnat to change the data for the object we can do: (here we change the name and the age for the object ares)
#ares.name = 'trueno'
#ares.age = 1
#Instead of changing it like that, we can use the set_name function
#for the set_name function:
ares.set_name('trueno')
ares.set_name(10)

#for the sttdown function
ares = dog.sitdown()