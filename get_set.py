

class Cuenta_banco:
    def __init__(self,saldo):
        self._saldo = saldo
    def saldo(self):                     
        self._saldo #sirve para leer datos, el estado.
    

    @saldo.setter
    def saldo(self, saldo):
        if saldo < 0:
            print("saldo negativo no es posible")
        self._saldo = saldo

        

cuenta = Cuenta_banco(1000)  #llama al get
cuenta._saldo = 2000        #llama al set
print(cuenta._saldo)