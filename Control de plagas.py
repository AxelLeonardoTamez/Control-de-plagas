Folpet = 150
Semilla = 100

print("Ha elegido mildui por tratamiento químico")
print("Quimico es:Folpet")
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