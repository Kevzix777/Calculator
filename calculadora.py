while True :

    print("\nCalculadora ➕ ➖ ✖️  ➗\n[1] Suma \n[2] Resta \n[3] Multiplicacion \n[4] Division \n[0] salir\n")
    
    #manejo de excepciones para la variable opcion en caso se introduzca un string 
    try:
        opcion = int(input("elige una opcion: "))
    except ValueError:
        print("**error**")
        continue

    #si opcion es igual a cero,se rompe el bucle.
    if opcion==0:
        break

    elif opcion > 4 or opcion < 0:
        print("**error**")
        continue

    #manejo de excepciones para la variables num1 y num2 en caso se introduzca un string 
    try:
        num1 = int(input("\nIngrese el primer numero: "))
        num2 = int(input("Ingrese el segundo numero: "))
    except ValueError:
       print("**ingrese valores numericos**")
       continue

    if opcion == 1:
        operacion = num1+num2
        print(f"\nEl resultado de la suma es >> {operacion}")
    elif opcion == 2:
        operacion = num1-num2
        print(f"\nEl resultado de la resta es >> {operacion}")
    elif opcion == 3:
        operacion = num1*num2
        print(f"\nEl resultado de la multiplicacion es >> {operacion}")
    elif opcion == 4:
        if num1 != 0 and num2 != 0:
            operacion = num1/num2
            print(f"\nEl resultado de la división es >> {operacion}")
        else:
            print("no se puede dividir por cero")


      


