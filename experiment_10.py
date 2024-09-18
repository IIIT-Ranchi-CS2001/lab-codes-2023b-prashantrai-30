num = int(input("Enter a Number:"))
temp = num
sum=0
while(temp>0):
    sum+=temp%10
    temp//=10
print("Sum is:",sum)