a=(input("enter no."))
cube_add=0
for i in a:
    cube=int(i)**3
    cube_add+=cube
if int(a)==cube_add:
    print(True)
else:
    
    print(False)
