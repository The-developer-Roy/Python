# Program to calculate a student's grade

m1 = int(input("Enter mark of first subject: "))
m2 = int(input("Enter mark of second subject: "))
m3 = int(input("Enter mark of third subject: "))
m4 = int(input("Enter mark of fourth subject: "))
m5 = int(input("Enter mark of fifth subject: "))

p = (m1+m2+m3+m4+m5/3)

if (p>90):
    print("Grade-A")
elif (p>80 and p<=90):
    print("Grade-B")
elif (p>60 and p<=80):
    print("Grade-C")
elif (p>60 and p<=45):
    print("Grade-D")
else:
    print("Fail")

