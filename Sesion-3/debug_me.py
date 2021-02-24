# --- Find the error!


def g(a, b):
    return a - b


def f(a, b, c, d):
    t0 = a + b - g(a, 0)
    t1 = g(c, d)
    try:
        t3 = 2 * (t0 / t1)
        return t0 + 2*t1 + t3*t3
    except ZeroDivisionError:
        return "You cannot calculate that"


# -- Main program
print("Result 1: ", f(5, 2, 5, 0))
print("Result 2: ", f(0, 2, 3, 3))
print("Result 3: ", f(1, 3, 2, 3))
print("Result 4: ", f(1, 9, 22.0, 3))

#we get that there´s an error in line eleven --> File "C:\Users\natip\PycharmProjects\PINE-Practices\Sesion-3\debug_me.py", line 11, in f
#    t3 = 2 * (t0 / t1)
# File "C:\Users\natip\PycharmProjects\PINE-Practices\Sesion-3\debug_me.py", line 17, in <module>
#    print("Result 2: ", f(0, 2, 3, 3))
#so we need to use the debug to see when that error happens
# we can solve it with a try or with if c != d:



# THIS IS WHAT WE HAD IN THE BEGINNING
# --- Find the error!


#def g(a, b):
#    return a - b


#def f(a, b, c, d):
#    t0 = a + b - g(a, 0)
#    t1 = g(c, d)
#    t3 = 2 * (t0 / t1)
#    return t0 + 2*t1 + t3*t3


# -- Main program
#print("Result 1: ", f(5, 2, 5, 0))
#print("Result 2: ", f(0, 2, 3, 3))
#print("Result 3: ", f(1, 3, 2, 3))
#print("Result 4: ", f(1, 9, 22.0, 3))