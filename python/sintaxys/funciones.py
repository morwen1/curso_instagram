def holamundo(argumentos=None):
    return "hola mundo"



def torque(rpm=int , hp=int):
    t= rpm/hp
    return t

def torque_variations(endrpm , rpm=0 ,list_torque = []):
    t = torque(rpm=rpm ,hp= 300)
    list_torque.append(t)
    if rpm == endrpm:
        return t , list_torque
    else:
        return torque_variations(endrpm, rpm = rpm+1 , list_torque=list_torque)

torque , listas_torques = torque_variations(endrpm=900)
print(torque , '\n' , listas_torques)
