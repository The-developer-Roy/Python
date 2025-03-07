#armstrong number

n = int(input("Enter number: "))

t=n

sum=0

while(n!=0):
    i, f = 1, 1
    r = n%10
    while(i<=r):
        f*=i
        i+=1
    sum+=f
    n//=10
if(t==sum):
    print(t, "is strong number")
else:
    print(t, "is not strong number")