


class Silla:
    #metodo == "funcion"
    #atributo de clase
    respaldo = True
    def __init__(self,cant_patas:int,material:str,color:str, precio:float):
        #aributos
        self.cant_patas = cant_patas
        self.material = material
        self.color = color
        self.precio = precio

    def mostrar_silla(self):
        print(f"""
              
la silla tiene : {self.cant_patas} patas
es de : {self.material}
el color es : {self.color}  
el precio es : {self.precio}     
              
""" )

silla_1 = Silla()
print(silla_1)   #instanciando 