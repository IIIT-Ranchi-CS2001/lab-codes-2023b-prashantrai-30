import math
a = int(input("enter a:"))
b = int(input("enter b:"))
c = int(input("enter c:"))

d = b**2 - 4*a*c

if(d==0):
    r1 = -b/2*a
    print("roots are:",r1,r1)

if(d>0):
    r1 = ((-b+math.sqrt(d))/2*a)
    r2 = ((-b-math.sqrt(d))/2*a)
    print("roots are",r1,r2)

if(d<0):
    real = (-b/(2*a))
    img = ((math.sqrt(-d))/2*a)
    print("real:",real)
    print("imaginary:",img)



