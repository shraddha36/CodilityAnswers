a=(input("enter no."))
cube_add=0
for i in a:
    cube=int(i)**3
    cube_add+=cube
if int(a)==cube_add:
    print(True)
else:
    
    print(False)

"""
a=int(input("enter no."))
cube_add=0
num=a

while num>0:
    c=num%10
    cube_add+=c**3
    num //=10
if a==cube_add:
    print(True)
else:
    print(False)
"""
"""153%10=3
153//10=15"""
