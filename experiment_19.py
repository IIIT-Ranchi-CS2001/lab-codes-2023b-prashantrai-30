import ast,math
coordinate1 = ast.literal_eval(input("enter coordinate of first point"))
coordinate2 = ast.literal_eval(input("enter coordinate of second point"))

distance = math.sqrt((coordinate1[0]-coordinate1[0])**2+(coordinate1[1]-coordinate2[1])**2+(coordinate1[2]-coordinate2[2])**2)
print(distance)
