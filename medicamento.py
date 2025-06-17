

class Medicamento:
    descuento = 0.05          #atributos de clase
    iva = 0.19

#instacian obj 

#paracetamol = Medicamento()
#print(paracetamol)


m1 = Medicamento()
m2 = Medicamento()

if m1.iva == m2.iva and m1.descuento == m2.descuento:
    print("todas las instancias son iguales")
    print(f"el iva es : {Medicamento.iva}")  #sin instanciar
    print(f"el descuento es : {Medicamento.descuento}")