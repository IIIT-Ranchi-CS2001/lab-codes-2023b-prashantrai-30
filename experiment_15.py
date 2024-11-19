string = str(input("Enter a string:"))
l = string.split()
for i in l:
    if i==i[::-1]:
        print(i)