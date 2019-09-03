#estructuras ciclicas con for y while

#1 for

for i in range(10):
    print("for ",i)


i = 0 
while i < 10 :
    print("while " ,i)
    i+=1

for i in range(100):
    
    _ = i * i-1
    if _ >= 400 :
        break
    if _ >= 200:
        continue
    
    print(_)