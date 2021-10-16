



def menu1():
    print("Bienvenido al solucionador de plagas, a continuación se muestran las plagas que disponemos con información:\n")
    print("1. Caracteristicas Mildui")
    print("2. Caracteristicas Mosca de la remolacha")
    print("3. Caracteristicas Pulgon")
    print("4. Caracteristicas Nematodos")
    plaga = int(input("Elige plaga a conocer\n"))
    while plaga not in [1, 2, 3, 4]:
        print("Error, seleccione un numero de los mostrados en pantalla")
        plaga = int(input("Elige plaga a conocer\n"))

    if plaga == 1:
        print("Ha elegido Mildui")
        print("0 - Forma física\n"
              "1 - Ubicación en la planta\n"
              "2 - Daños causados")
        mildui = [["forma física", "Manchas amarillas"], ["ubicación en la planta", "En las hojas"],["daños causado", "Seca las hojas"]]
        dato = int(input("Ingrese el numero del dato que quiera saber\n"))
        print("El dato de " + mildui[dato][0] + " es: ")
        print(mildui[dato][1])
        cambio_menu()


    elif plaga == 2:
        print("Ha elegido Mosca de la remolacha\n")
        print("0 - Forma física\n"
               "1 - Ubicación en la planta\n"
               "2 - Daños causados")
        mosca = [["forma física", "Insecto"],["ubicación en la planta", "Dentro de las hojas"],["daños causado","El tejido afectado se vuelve translucido"]]
        dato = int(input("Ingrese el numero del dato que quiera saber\n"))
        print("El dato de " + mosca[dato][0] + " es: ")
        print(mosca[dato][1])
        cambio_menu()


    elif plaga == 3:
        print("Ha elegido Pulgon\n")
        print("0 - Forma física\n"
               "1 - Ubicación en la planta\n"
               "2 - Daños causados")
        pulgon = [["forma física", "Insecto"],["ubicación en la planta", "Entre las hojas"],["daños causado","Se come la hoja"]]
        dato = int(input("Ingrese el numero del dato que quiera saber\n"))
        print("El dato de " + pulgon[dato][0] + " es: ")
        print(pulgon[dato][1])
        cambio_menu()


    elif plaga == 4:
        print("Ha elegido Nematodos\n")
        print("0 - Forma física\n"
               "1 - Ubicación en la planta\n"
               "2 - Daños causados")
        nematodos = [["forma física", "Gusano microscopico"],["ubicación en la planta", "En la raiz"],["daños causado","Daña las raices"]]
        dato = int(input("Ingrese el numero del dato que quiera saber\n"))
        print("El dato de " + nematodos[dato][0] + " es: ")
        print(nematodos[dato][1])
        cambio_menu()


def Mildui(semilla):
    f = 150
    semillas = 100
    fer = f * semilla / semillas
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
    kg_acefato = acefato * hec
    print("los kg de acefato son", kg_acefato)
    agua_hec = (kg_acefato * agua) / acefato
    return agua_hec


def Nematodos(hec):
    fenamifos = 7
    fenamifos_agua = fenamifos * hec
    return fenamifos_agua

def cambio_menu():
    print("¿Desea proseguir con el menú de control de plagas(1) o volver al de informacion(2)?")
    cambio_menu_eleccion = int(input())
    while cambio_menu_eleccion not in [1, 2]:
        print("Elige una opción valida")
    if cambio_menu_eleccion == 1:
        menu2()
    elif cambio_menu_eleccion ==2:
        menu1()

def menu2():
    print("A continuación se muestra el menú de control de plagas: ")
    print("1. Mildui")
    print("2. Mosca de la remalacha")
    print("3. Pulgon")
    print("4. Nematodos")
    plaga = int(input("Escoge tu plaga a tratar: "))
    while plaga >= 6 or plaga <= 0:
        print("Error, seleccione un numero de los mostrados en pantalla")
        plaga = int(input("Escoge tu plaga a tratar"))


    if plaga == 1:
        print("¿Desea obtener el método químico(1) o biológico(2)?")
        metodo = int(input())
        if metodo == 1:
           semilla = float(input("Dame los Kg de semilla "))
           while semilla < 0:
               print("Error, ingrese numero positivo")
               semilla = float(input("Dame los Kg de semilla "))
           res = Mildui(semilla)
           print("Los kilogramos necesarios son: ", res)
           cambio_menu()

        elif metodo ==2:
            for i in range(len(metodo_biologico)):
                if metodo_biologico[i][0] == "Mildui":
                    print("El método biológico para controlar la plaga puede ser con:")
                    print(metodo_biologico[i][1:])
                    cambio_menu()

    elif plaga == 2:
        print("¿Desea obtener el método químico(1) o biológico(2)?")
        metodo = int(input())
        if metodo == 1:
            hec = float(input("Dame el numero de hectareas: "))
            while hec < 0:
                print("Error, ingrese numero positivo")
                hec = float(input("Dame el numero de hectareas "))
            res = Mosca(hec)
            print("Los litros de agua con diazinon necesarios son: ", res)
            cambio_menu()

        elif metodo == 2:
            for i in range(len(metodo_biologico)):
                if metodo_biologico[i][0] == "Mosca":
                    print("El método biológico para controlar la plaga puede ser con:")
                    print(metodo_biologico[i][1:])
                    cambio_menu()



    elif plaga == 3:
        print("¿Desea obtener el método químico(1) o biológico(2)?")
        metodo = int(input())
        if metodo == 1:
            hec = float(input("Dame el numero de hectareas "))
            while hec < 0:
                print("Error, ingrese numero positivo")
                hec = float(input("Dame el numero de hectareas "))
                res = Pulgon(hec)
                print("Los litros de agua con acefato necesarios son:", res)
                cambio_menu()
        elif metodo == 2:
            for i in range(len(metodo_biologico)):
                if metodo_biologico[i][0] == "Pulgon":
                    print("El método biológico para controlar la plaga puede ser con:")
                    print(metodo_biologico[i][1:])
                    cambio_menu()

    elif plaga == 4:
        print("¿Desea obtener el método químico(1) o biológico(2)?")
        metodo = int(input())
        if metodo == 1:
            hec = float(input("Dame el numero de hectareas "))
            while hec < 0:
                print("Error, ingrese numero positivo")
                hec = float(input("Dame el numero de hectareas "))
            res = Nematodos(hec)
            print("Los litros de fenamifos necesarios son:", res)
            cambio_menu()
        elif metodo == 2:
            for i in range(len(metodo_biologico)):
                if metodo_biologico[i][0] == "Nematodos":
                    print("El método biológico para controlar la plaga puede ser con:")
                    print(metodo_biologico[i][1:])
                    cambio_menu()


metodo_biologico = [["Mildui", "Bicarbonato sódico", "Caldo Bordeles", "Jabón de potasa", "Cobre"],
                    ["Mosca", "Jabón potásico", "Azadiractin", "Azadiractin"],
                    ["Pulgon", "Cochinilla septepunctata", "Aphidoletes", "Plantas de tomate", "Trampas cromáticas"],
                    ["Nematodos", "ROtación de cultivos", "Solarización", "Variedades hortícolas"]]

menu1()


