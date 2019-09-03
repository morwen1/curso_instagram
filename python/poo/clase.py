class HolaMundo():
    def hola(self):
        return "hola"
    def mundo(self) :
        return"mundo"

class Saludo(HolaMundo):
    def completar(self):
        return "como estas"

obj = Saludo()
print(obj.hola() ,obj.completar())
