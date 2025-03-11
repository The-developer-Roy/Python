def f(x):
    return  x**3 - 5*x - 9

def secant(x0, x1, e, N):
    print("\n\n*** SECANT METHOD IMPLEMENTATION ***")
    step = 1
    condition = True
    while condition:
        if f(x0) == f(x1):
            print("Divide by zero error!")
            break
        x2 = x0 - (x1-x0)*f(x0)/(f(x1) - f(x0))
        print("Iteration-%d, x2 = %0.6f and f(x2) = %0.6f" % (step, x2, f(x2)))
        x0 = x1
        x1 = x2
        step = step + 1

        if step > N:
            print("Npt Convergent!")
            break
        
        condition = abs(f(x2)) > e
    
    print("Required root is: %0.8f" %x2)

x0 = input("Enter First Guess: ")
x1 = input("Enter second  guess: ")
e = input("Tolerable error: ")
N = input("Maximum step: ")

x0 = float(x0)
x1 = float(x1)
e = float(e)
N = int(N)

secant(x0, x1, e, N)