def func(x):
    return x**3 - x**2 + 2

def deriveFunc(x):
    return 3*x*x - 2*x
def newtonRaphson(x):
    h = func(x)/deriveFunc(x)

    while abs(h)>=0.0001:
        h = func(x)/deriveFunc(x)
        x = x-h
    print("The value of the root is: ", "%.2f" %x)

x0 = -20
newtonRaphson(x0)