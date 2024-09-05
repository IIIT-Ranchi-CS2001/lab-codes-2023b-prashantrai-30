'''
WAP to find 
1> Area and Perimeter of triangle when all three sides are given.Use heron's formula area=> A=(s(s-a)(s-b)(s-c))^1/2 and perimetr=> s=(a+b+c)/2
2> Find all three angles of triangle given in (1)
display input data and result in proper format
'''

import math
side1 = int(input("Enter first side:"))
side2 = int(input("Enter second side:"))
side3 = int(input("Enter third side:"))

perimeter = (side1+side2+side3)
semiperimeter = (perimeter/2)

area = (math.sqrt(semiperimeter*((semiperimeter-side1)*(semiperimeter-side2)*(semiperimeter-side3))))
firstAngle = math.degrees(math.acos(((side2**2)+(side3**2)-(side1**2))/(2*side2*side3)))
secondAngle = math.degrees(math.acos(((side1**2)+(side3**2)-(side2**2))/(2*side1*side3)))
thirdAngle = 180-firstAngle-secondAngle
print("Area of Triangle:",area)
print("Perimeter of Triangle:",perimeter)
print("First Angle of Triangle:",firstAngle)
print("Second Angle of Triangle:",secondAngle)
print("Third Angle of Triangle:",thirdAngle)



