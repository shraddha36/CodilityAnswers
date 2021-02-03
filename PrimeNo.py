def primeno(num):
    
    if num==2 or num==3 or num==5 or num==7:
        return("it is prime no.")
    else:
        if num%3 !=0 or num%5 !=0 or num%7 !=0 or num%2 !=0:
            return("it is prime no.")
        return("it is not a prime no.")
print(primeno(5))

"""
def primeno(num):
    count=0
    for i in range(2,num+1):
        
        if num%i==0:
            count+=1
        if num%i==0 and count>1:
            return("not a prime no.")
        
    return("prime no.")
print(primeno(12),"12")
print(primeno(13),"13")
print(primeno(14),"14")
print(primeno(15),"15")
print(primeno(16),"16")
print(primeno(17),"17")
print(primeno(18),"18")"""
