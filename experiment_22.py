string = str(input("Enter a string:"))
dict = {}
for char in string:
    if char in dict:
        dict[char] +=1
    else:
        dict[char] = 1

for i in dict.items():
    print(i)