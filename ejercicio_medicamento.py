

from medicamento import Medicamento


paracetamol = Medicamento()
precio = int(input("ingresa un valor"))

true_false = paracetamol.validar_mayor_a_0(precio)

if true_false:
    print("precio valido")

else:
    print("precio no valido")