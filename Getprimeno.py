def primeno(a,b):
    for num in range(a,b):
        if all(num%i!=0 for i in range(2,num)):
            print(num)
primeno(100,150)
