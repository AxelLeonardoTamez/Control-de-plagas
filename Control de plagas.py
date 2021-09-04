def Mildui(semilla):
    f = 150
    semillas = 100
    fer = f*semilla/semillas
    return fer

def Mosca(hec):
    diazinon = .9
    lq = hec * diazinon
    print("Los litros de Diazinon son:", lq)
    la = lq * 100 / diazinon
    return la


def menu():
    print("1. Mildui")
    print("2. Mosca de la remalacha")
    print("3. Pulgon")
    print("4. Nematodos")
    op = int(input("Escoge tu plaga a tratar"))
    if op == 1:
        semilla = float(input("Dame los Kg de semilla "))
        res = Mildui(semilla)
        print("Los kilogramos necesarios son: ", res)
    if op == 2:
        hec = float(input("Dame el numero de hectareas "))
        res = Mosca(hec)
        print("Los litros de agua con diazinon necesarios son: ", res)



menu()

"""
Folpet = 150
Semilla = 100

print("Ha elegido mildui por tratamiento químico")
print("Quimico es:Folpet")
Kg = int(input("Kg de semillas que va a utilizar"))
def kg_fertilizante_ha(kg, folpet, semilla)
fertilizante = (Folpet*Kg)/Semilla
return fertilizante



Kg = int(input("Kg de semillas que va a utilizar"))
fertilizante = (Folpet*Kg)/Semilla
print("Los Kg necesarios de fertilizante por ha son",fertilizante)

Acefato = .7
Agua= 120

print("Ha elegido pulgones por tratamiento químico")
print("Quimico es: Acefato")
Hectareas = float(input("Numero de hectareas que va a fertilizar"))
Kg = (Acefato*Hectareas)
print("Los kilogramos necesarios son",Kg)
Litros= (Kg*Agua)/Acefato
print("Los litros de agua por ha necesarios son", Litros)


Diazinon = .9


print("Ha elegido mosca de la remolacha por tratamiento químico")
print("Quimico es:Diazinon")
Hectareas = float(input("Numero de hectareas que va a fertilizar"))
Litros = (Hectareas*Diazinon)
print("Los litros de Diazinon nesesarios son", Litros)
Lagua = (Litros*100)/Diazinon
print("Diluidos en", Lagua)

"""

