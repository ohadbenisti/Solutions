
p = {'apple':10.0, 'banana': 6.5, 'milk':6.90, 'orange':7, 'milk':5, 'cofee':9.8}
sL=[('apple',3),('milk',2),('orange', 3),('cofee', 4), ('banana', 55), ('strawberry', 16)]
pL=p.items()
pK=p.keys()
pV=p.values()

sum=0
for i in range(len(sL)):
    if (sL[i][0] in p):
        sum+= (p[sL[i][0]] * sL[i][1])
        
for i in range(len(sL)):
    if not(sL[i][0] in p):
        print("The item '", sL[i][0], "' is not exist in the market.")
        print("Sorry!")
        print()
        print()

print("The purchase amount is:", sum, 'NIS.')
print("Thank you!")
print()
print()
