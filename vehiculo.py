

class Vehiculo:
    def __init__(self, marca:str, modelo:str, anio:int):
        self.__marca = marca
        self.modelo = modelo
        self.anio = anio

        #metodos   comportamientos son metodos
        #getter setter
        def get_marca(self):
            return self.__marca
        
        def set__marca(self, new_marca:str):
            self.__marca = new_marca


        def mostrar(self):
            print(self.__marca modelo, self.anio)

##auto = Vehiculo("audi", "g3", 1999)

class Auto(Vehiculo):
    def __init__(self, marca, modelo, anio, puertas):
        super().__init__(marca, modelo, anio)

        self.__puertas = puertas  # '__'  datos privados

    def get_puertas(self):
        return self.puertas
    
    def set_puertas(self, puerta):
        self.puertas = puerta

    def mostrar(self):
        print(self.marca, self.modelo, self.anio, self.puertas)
    
auto_1 = Auto("toyota", "corolla", 2022, 4)

print(auto_1.mostrar())