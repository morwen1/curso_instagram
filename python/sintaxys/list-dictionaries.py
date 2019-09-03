import random as rd #importaciones de librerias
#listas y dicionarios 
x = [] #lista vacia
x = [1,2,3,4] #lista con datos
y = [rd.randint(0,i) for i in range(600)] #list comprehesion
#operaciones en la listas
print(x[0]) #llamada por indices
x[0]=9 #asignacion por indices
x.remove(3) #eliminacion
x.append(12) #agrega al ultimo lugar

print(x)

#explicacion de list comprehesion 

print(y[0:30]) #slices


#dictionaries 
data = {
    'dato_one' : "hola mundo",
    'vaca':"una vaca vestida de uniforme",
    'cantidad':2,
    'meme' :False
}
print(data['meme'] , data['vaca'])
data.pop('meme')
print(data)
data['nuevo_dato'] = "hi!"
print(data)