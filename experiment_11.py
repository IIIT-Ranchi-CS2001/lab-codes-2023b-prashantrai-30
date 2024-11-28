num = int(input("Enter the value of n:")) #n => number of term
a = 0
b = 1
print(a)
while(num>1):
    temp = a
    a=b
    b=a+temp
    print(b," ")
    num-=1

    