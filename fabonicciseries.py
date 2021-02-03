a=int(input("enter first no. of fabonicci series "))
b=int(input("enter second no. of fabonicci series "))
n=int(input("count of it "))

print(a,b,end=" ")

while n-2:
    print(n)
    c=a+b
    a=b
    b=c
    print(b,end=" ")
    n-=1
