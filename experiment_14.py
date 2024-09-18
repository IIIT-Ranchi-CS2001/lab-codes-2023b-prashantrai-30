string = str(input("Enter a string:"))
char = str(input("Enter character to find:"))
count=0
for i in string:
    if(i == char):
        count+=1
print(count)
