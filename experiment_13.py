string = str(input("Enter a string:"))
c=0
for char in string:
    if not((char >='a' and char <='z')or(char >= 'A' and char <= 'Z') or (char >='0' and char <='9')):
        c+=1
if(c>0):
    print(False)
else:
    print(True)
    