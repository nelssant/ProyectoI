"""Este Programa muestra un menu, e el menu el usuario puede elegir entre el numero 1 o el numero 2; la seleccion del numero 1 devuelve el Teorema de Pitagoras y la opcion 2 devuelve el juego del ahorcado
Autor: Nelson Santos
Universidad Mariano Galvez de Guatemala
Version Final 3.0
Fecha 09.01.2023 Boca del Monte Villa Canales"""
#Establecemos un menu para que el usuario pueda elegir lo que quiera mostrar
Menu_Ejercicios = int(input("Que ejercicio desea ejecutar? 1 = Triple de Pitagoras & 2 = Juego del Ahorcado "))
if Menu_Ejercicios == 1:
    Decision_Rango_TP = input("Desea establecer el rango para calcular el triple de pitagoras?, escriba Si (De lo contrario se mostrara el rango no mayor a 500) ")
    if Decision_Rango_TP == "Si":
        R_Rango_Triple_Pitagoras = int(input("Ingrese el rango para calcular los numeros que cumplen con el Triple de Pitagoras "))
        for i in range (1,(R_Rango_Triple_Pitagoras + 1)): #Damos el valor a c y posterior a ello, lo elevamos al cuadrado
            Numero_3 = i
            N3_Elevacion = Numero_3 ** 2
            for j in range (1,i): #Damos el valor a b y posterior a ello, lo elevamos al cuadrado
                Numero_2 = j
                N2_Elevacion = Numero_2 ** 2
                for k in range (1,j): #Damos el valor a a y posterior a ello, lo elevamos al cuadrado
                    Numero_1 = k
                    N1_Elevacion = Numero_1 ** 2
                    if N1_Elevacion + N2_Elevacion == N3_Elevacion: #Comparamos e imprimimos los resultados que den un valor booleano para nuestro IF
                        print("(",Numero_1,"+",Numero_2,"=",Numero_3,")")
        print("Finalizado ")
    else:
        for i in range (1,501): 
            Numero_3 = i
            N3_Elevacion = Numero_3 ** 2
            for j in range (1,i):
                Numero_2 = j
                N2_Elevacion = Numero_2 ** 2
                for k in range (1,j):    
                    Numero_1 = k
                    N1_Elevacion = Numero_1 ** 2
                    if N1_Elevacion + N2_Elevacion == N3_Elevacion:
                        print("(",Numero_1,"+",Numero_2,"=",Numero_3,")")
        print("Finalizado ")
elif Menu_Ejercicios == 2:
    print("Para este juego se tiene un catalogo de 10 palabras, las mismas estan relacionadas con: Informatica, Vida Marina, Tecnologia, Lugares de Guatemala y Sonido (Es un simbolo nacional de Guatemala) ")
    print("Las letras deben de ser ingresadas en formato minuscula, de lo contrario el sistema lo tomara como una letra erronea")
    print("Toma en cuenta de que de la lista de 10 palabras, el sistema selecciona una de forma aleatoria!, QUe nervios! ")
    print("Iniciamos! ")
    import random
    N_Variables = [
            "Mariano Galvez",
            "Boca del Monte",
            "Guatemala",
            "Himno Nacional",
            "IA",
            "Tigre",
            "Megalodon",
            "Terabyte",
            "Python",
            "Galaxy S23 Ultra"
                ]
    # Para poder almacenar y luego manipular la palabra random de nuestra lista; usaremos la variable V_Seleccion_Aleatoria
    V_Seleccion_Aleatoria = random.choice(N_Variables)
    V_Seleccion_Aleatoria = V_Seleccion_Aleatoria.lower()
    Longitud = len(V_Seleccion_Aleatoria)
    Oportunidades = 6
    Comodin = "Sin usar" # Nos ayudara a poder saber cuando si podemos mostrar el comodin y cuando considerar si el usuario ingresa la palabra comodin
    A_asteriscos = [" " if Caracter == " " else "*" for Caracter in V_Seleccion_Aleatoria] # Ayuda a realizar el rellenado de los asteriscos considerando los espacios
    while Oportunidades > 0 and "*" in A_asteriscos:
        # Dado a que no podemos usar funciones, creamos los escenarios posibles acorde al numero de oportunidades
        if Oportunidades == 6:
            print("_" * 26)
            print("|" + " " * 11 + " |")
            print("|" + " " * 11 + " O")
            if Comodin != "Usado": 
                print("|" + " " * 11 + "/|\\" + " " * 3 + "comodin")
            else:
                print("|" + " " * 11 + "/|\\ ")    
            print("|" + " " * 11 + "/ \\ ")
            print("|")
            print(" " * (13 - Longitud // 2 ) + "".join(A_asteriscos))
        elif Oportunidades == 5:
            print("_" * 26)
            print("|" + " " * 11 + " |")
            print("|" + " " * 11 + " O")
            if Comodin != "Usado": 
                print("|" + " " * 11 + "/|\\ " + " " * 3 + "comodin")
            else:
                print("|" + " " * 11 + "/|\\ ")
            print("|" + " " * 11 + "/ ")
            print("|")
            print(" " * (13 - Longitud // 2 ) + "".join(A_asteriscos))
        elif Oportunidades == 4:
            print("_" * 26)
            print("|" + " " * 11 + " |")
            print("|" + " " * 11 + " O")
            if Comodin != "Usado": 
                print("|" + " " * 11 + "/|\\ " + " " * 3 + "comodin")
            else:
                print("|" + " " * 11 + "/|\\ ")
            print("|")
            print(" " * (13 - Longitud // 2 ) + "".join(A_asteriscos))
        elif Oportunidades == 3:
            print("_" * 26)
            print("|" + " " * 11 + " |")
            print("|" + " " * 11 + " O")
            if Comodin != "Usado":
                print("|" + " " * 11 + "/| " + " " * 3 + "comodin")
            else :
                print("|" + " " * 11 + "/| ")
            print("|")
            print(" " * (13 - Longitud // 2 ) + "".join(A_asteriscos))
        elif Oportunidades == 2:
            print("_" * 26)
            print("|" + " " * 11 + " |")
            print("|" + " " * 11 + " O")
            if Comodin != "Usado":
                print("|" + " " * 11 + " | " + " " * 3 + "comodin")
            else:
                print("|" + " " * 11 + " | ")
            print("|")
            print(" " * (13 - Longitud // 2 ) + "".join(A_asteriscos))
        elif Oportunidades == 1:
            print("_" * 26)
            print("|" + " " * 11 + " |")
            print("|" + " " * 11 + " O")
            if Comodin != "Usado":
                print("|" + " " * 11 + "   " + " " * 3 + "comodin")
            else:
                print("|")
                print(" " * (13 - Longitud // 2 ) + "".join(A_asteriscos))
        # Vamos a validar si nuestro comodin ha sido utilizado, si no ha sido usado; se le mueestra al usuario en un mensaje que puede utilizarlo
        if Comodin != "Usado":
            L_Letra= input("Ingrese una letra o la palabra Comodin (El comodin le dara una pista y solo se puede usar una vez) ")
            L_Letra= L_Letra.lower ()
            if L_Letra == "comodin":
                Comodin = "Usado"
                if V_Seleccion_Aleatoria == "mariano galvez":
                    print("Es una universidad, en ella lleva el el nombre de tu pais")
                elif V_Seleccion_Aleatoria == "boca del monte":
                    print ("Hay una universidad que tiene sede en dicho lugar; este pertenece a Vila Canales")
                elif V_Seleccion_Aleatoria == "guatemala":
                    print("Ha sido considerado el pais de la eterna primavera")
                elif V_Seleccion_Aleatoria == "himno nacional":
                    print("Es considerado entre muchos como una melodia nacional de las mas hermosas; siempre se reproduce antes de un partido de futbol")
                elif V_Seleccion_Aleatoria == "ia":
                    print("Ultima mente se ha puesto muy de moda ya que ayuda en muchas maneras, la misma debe de tener un proceso de entrenamiento y protocolos de seguridad; a Hawking le preocupaba")
                elif V_Seleccion_Aleatoria == "tigre":
                    print("Es un felino grande y carnivoro")
                elif V_Seleccion_Aleatoria == "megalodon":
                    print("Es acuatico y existen 2 peliculas al respecto; el actor principal es Jason Stathan")
                elif V_Seleccion_Aleatoria == "terabyte":
                    print("Es una unidad de medida que por lo general es standar con los HHD de las laptops al momento de comprarlas el numero equivale a: 1024")
                elif V_Seleccion_Aleatoria == "python":
                    print("Es un lenguaje de programacion de codigo abierto, es muy amigable y se representa mediante un reptil")
                elif V_Seleccion_Aleatoria == "galaxy s23 ultra":
                    print("Es la gama mas pro y de la serie S que ha sacado el fabricante surcoreano en el anio 2023")
                L_Letra= input("Ingrese una letra ")
                L_Letra= L_Letra.lower ()
                if L_Letra in V_Seleccion_Aleatoria:
                    for q in range (Longitud): #Ayudara a poder hacer el rellenado de la letra en donde esta nuestro asterisco
                        if V_Seleccion_Aleatoria[q] == L_Letra:
                            A_asteriscos[q] = L_Letra
                else:
                    Oportunidades = Oportunidades - 1
            else:
                if L_Letra in V_Seleccion_Aleatoria:
                    for q in range (Longitud):
                        if V_Seleccion_Aleatoria[q] == L_Letra:
                            A_asteriscos[q] = L_Letra
                else:
                    Oportunidades = Oportunidades - 1
        else:
            L_Letra= input("Ingrese una letra ")
            L_Letra= L_Letra.lower ()
            if L_Letra in V_Seleccion_Aleatoria:
                for q in range (Longitud):
                    if V_Seleccion_Aleatoria[q] == L_Letra:
                        A_asteriscos[q] = L_Letra
            else:
                Oportunidades = Oportunidades - 1
        Conteo_Asteriscos = A_asteriscos.count("*")
        # Por ultimo, imprimimos el dibujo final con la palabra completa y el estado en el que quedo el dibujo
        if Oportunidades == 0 and Conteo_Asteriscos > 0:
            print("La palabra era: ",V_Seleccion_Aleatoria)
        if Oportunidades == 1 and Conteo_Asteriscos == 0:
            print("_" * 26)
            print("|" + " " * 11 + " |")
            print("|" + " " * 11 + " O")
            if Comodin != "Usado":
                print("|" + " " * 11 + "   " + " " * 3 + "comodin")
            print("|")
            print(" " * (13 - Longitud // 2 ) + "".join(A_asteriscos))
            print("Adivinaste! ")
        if Oportunidades == 2 and Conteo_Asteriscos == 0:
            print("_" * 26)
            print("|" + " " * 11 + " |")
            print("|" + " " * 11 + " O")
            if Comodin != "Usado":
                print("|" + " " * 11 + " | " + " " * 3 + "comodin")
            else:
                print("|" + " " * 11 + " | ")
            print("|")
            print(" " * (13 - Longitud // 2 ) + "".join(A_asteriscos))
            print("Adivinaste! ")
        if  Oportunidades == 3 and Conteo_Asteriscos == 0:
            print("_" * 26)
            print("|" + " " * 11 + " |")
            print("|" + " " * 11 + " O")
            if Comodin != "Usado":
                print("|" + " " * 11 + "/| " + " " * 3 + "comodin")
            else :
                print("|" + " " * 11 + "/| ")
            print("|")
            print(" " * (13 - Longitud // 2 ) + "".join(A_asteriscos))
            print("Adivinaste! ")
        if Oportunidades == 4 and Conteo_Asteriscos == 0:
            print("_" * 26)
            print("|" + " " * 11 + " |")
            print("|" + " " * 11 + " O")
            if Comodin != "Usado": 
                print("|" + " " * 11 + "/|\\ " + " " * 3 + "comodin")
            else:
                print("|" + " " * 11 + "/|\\ ")
            print("|")
            print(" " * (13 - Longitud // 2 ) + "".join(A_asteriscos))
            print("Adivinaste! ")
        if Oportunidades == 5 and Conteo_Asteriscos == 0:
            print("_" * 26)
            print("|" + " " * 11 + " |")
            print("|" + " " * 11 + " O")
            if Comodin != "Usado": 
                print("|" + " " * 11 + "/|\\ " + " " * 3 + "comodin")
            else:
                print("|" + " " * 11 + "/|\\ ")
            print("|" + " " * 11 + "/ ")
            print("|")
            print(" " * (13 - Longitud // 2 ) + "".join(A_asteriscos))
            print("Adivinaste! ")
        if Oportunidades == 6 and Conteo_Asteriscos == 0:
            print("_" * 26)
            print("|" + " " * 11 + " |")
            print("|" + " " * 11 + " O")
            if Comodin != "Usado": 
                print("|" + " " * 11 + "/|\\" + " " * 3 + "comodin")
            else:
                print("|" + " " * 11 + "/|\\ ")  
            print("|")
            print(" " * (13 - Longitud // 2 ) + "".join(A_asteriscos))
            print("Adivinaste! ")    
else:  
    print ("Le recomiendo tomar un curso de lectura, solo se le han mostrado dos opciones, vuelva a ejecutar el programa")