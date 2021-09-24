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

def Pulgon(hec):
    acefato = .7
    agua = 120
    kg_acefato = acefato*hec
    print("los kg de acefato son", kg_acefato)
    agua_hec = (kg_acefato*agua)/acefato
    return agua_hec

def Nematodos(hec):
    fenamifos = 7
    fenamifos_agua = fenamifos*hec
    return fenamifos_agua

def menu():
    print("1. Mildui")
    print("2. Mosca de la remalacha")
    print("3. Pulgon")
    print("4. Nematodos")
    plaga = int(input("Escoge tu plaga a tratar"))
    while plaga>=5:
        print("Error, seleccione un numero de los mostrados en pantalla")
        plaga = int(input("Escoge tu plaga a tratar"))
   
         
    if plaga == 1:
        semilla = float(input("Dame los Kg de semilla "))
        while semilla<0:
            print("Error, ingrese numero positivo")
            semilla = float(input("Dame los Kg de semilla "))
        res = Mildui(semilla)
        print("Los kilogramos necesarios son: ", res)
    if plaga == 2:
        hec = float(input("Dame el numero de hectareas "))
        while hec<0:
            print("Error, ingrese numero positivo")
            hec = float(input("Dame el numero de hectareas "))
        res = Mosca(hec)
        print("Los litros de agua con diazinon necesarios son: ", res)
    if plaga == 3:
        hec = float(input("Dame el numero de hectareas "))
        while hec<0:
            print("Error, ingrese numero positivo")
            hec = float(input("Dame el numero de hectareas "))
        res = Pulgon(hec)
        print("Los litros de agua con acefato necesarios son:", res)
    if plaga == 4:
        hec = float(input("Dame el numero de hectareas "))
        while hec<0:
            print("Error, ingrese numero positivo")
            hec = float(input("Dame el numero de hectareas "))
        res = Nematodos(hec)
        print("Los litros de fenamifos necesarios son:", res)
        



menu()

