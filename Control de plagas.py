def menu():
    print("1. Caracteristicas Mildui")
    print("2. Caracteristicas Mosca de la remolacha")
    print("3. Caracteristicas Pulgon")
    print("4. Caracteristicas Nematodos")
    plaga = int(input("Escoge tu plaga a tratar"))
    while plaga>=5:
        print("Error, seleccione un numero de los mostrados en pantalla")
        plaga = int(input("Escoge tu plaga a tratar"))
        
    if plaga == 1:
        print("forma fisica = 0, Ubicacion en la planta = 1, Daños causados = 2")
        mildui = ["Manchas amarillas","En las hojas","Seca las hojas"]
        dato = int(input("Ingrese el numero del dato que quiera saber"))
        print(mildui[dato])
         
    if plaga == 2:
         print("forma fisica = 0, Ubicacion en la planta = 1, Daños causados = 2")
         mosca = ["Insecto","Dentro de las hojas","El tejido afectado se vuelve translucido"]
         dato = int(input("Ingrese el numero del dato que quiera saber"))
         print(mosca[dato])
        
    if plaga == 3:
         print("forma fisica = 0, Ubicacion en la planta = 1, Daños causados = 2")
         pulgon = ["Insecto","Entre las hojas","Se come la hoja"]
         dato = int(input("Ingrese el numero del dato que quiera saber"))
         print(pulgon[dato])
        
    if plaga == 4:
         print("forma fisica = 0, Ubicacion en la planta = 1, Daños causados = 2")
         nematodos = ["Gusano microscopico","En la raiz","Dañan las raices"]
         dato = int(input("Ingrese el numero del dato que quiera saber"))
         print(nematodos[dato])
         
menu()         
    
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
    while plaga>=6:
        print("Error, seleccione un numero de los mostrados en pantalla")
        plaga = int(input("Escoge tu plaga a tratar"))
   
         
    if plaga == 1:
        semilla = float(input("Dame los Kg de semilla "))
        while semilla<0:
            print("Error, ingrese numero positivo")
            semilla = float(input("Dame los Kg de semilla "))
        res = Mildui(semilla)
        print("Los kilogramos necesarios son: ", res)
        print("forma fisica = 0, Ubicacion en la planta = 1, Daños causados = 2")

    elif plaga == 2:
        hec = float(input("Dame el numero de hectareas "))
        while hec<0:
            print("Error, ingrese numero positivo")
            hec = float(input("Dame el numero de hectareas "))
        res = Mosca(hec)
        print("Los litros de agua con diazinon necesarios son: ", res)
    elif plaga == 3:
        hec = float(input("Dame el numero de hectareas "))
        while hec<0:
            print("Error, ingrese numero positivo")
            hec = float(input("Dame el numero de hectareas "))
        res = Pulgon(hec)
        print("Los litros de agua con acefato necesarios son:", res)
    elif plaga == 4:
        hec = float(input("Dame el numero de hectareas "))
        while hec<0:
            print("Error, ingrese numero positivo")
            hec = float(input("Dame el numero de hectareas "))
        res = Nematodos(hec)
        print("Los litros de fenamifos necesarios son:", res)
        


menu()



         

