x = True 

print(x)

if x :
    print("if uno")

if x == True:
    print("if dos")

if x==list :
    print("if tres")

if x == "hola":
    print("if cuatro")

#####################################################

d = "una vaca vestida de uniforme"


if "vaca" in d :
    print("se encotro vaca")

list_d = d.split()
for i in list_d :
    if i=="vaca"  or i == "uniforme" and i == str :
        print("si es vaca")