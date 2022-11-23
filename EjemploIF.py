option=int(input("\nMENU\n-----------------------------\n\t" +
                 "1. Mayor-Menor\n\t2. Comparacion\n\t3. Multiplo_de_7\n\t4. Par-Impar\n\t5. Telefonia\n\t6. Salir\n\n\t" +
                 " FAVOR INGRESAT OPCIÓN: "));

while(option !=6):
    if(option ==1):
        print("INGRESO DE VALORES");
        a=int(input("Ingrese un numero: "));
        b=int(input("Ingrese otro numero: "));
        if(a<b):
            print("Numero mayor: ",b);
            print("Numero menor: ",a);
        elif(a>b):
            print("Numero mayor: ",a);
            print("Numero menor: ",b);
        else:
            print("Ups! ambos son iguales");

        option = int(input("\nMENU\n-----------------------------\n\t" +
                           "1. Mayor-Menor\n\t2. Comparacion\n\t3. Multiplo_de_7\n\t4. Par-Impar\n\t5. Telefonia\n\t6. Salir\n\n\t" +
                           " FAVOR INGRESAT OPCIÓN: "));

    elif(option ==2):
        print("INGRESO DE VALORES");
        a = int(input("Ingrese un numero: "));
        b = int(input("Ingrese otro numero: "));
        c = int(input("Ingrese otro numero: "));
        if (a>b and a>c):
            print("Numero mayor: ", a);
        elif (b>a and b>c):
            print("Numero mayor: ", b);
        elif (c > a and c > b):
            print("Numero mayor: ", c);
        else:
            print("Ups! ambos son iguales");

        option = int(input("\nMENU\n-----------------------------\n\t" +
                           "1. Mayor-Menor\n\t2. Comparacion\n\t3. Multiplo_de_7\n\t4. Par-Impar\n\t5. Telefonia\n\t6. Salir\n\n\t" +
                           " FAVOR INGRESAT OPCIÓN: "));

    elif(option ==3):
        print("INGRESO DE VALORES");
        a = int(input("Ingrese un numero: "));
        b = int(input("Ingrese otro numero: "));
        c = int(input("Ingrese otro numero: "));
        suma=int(a+b+c);
        division=int(suma%7);
        if(division==0):
            print("Son multiplo de 7");
        else:
            print("No son multiplo de 7");

        option = int(input("\nMENU\n-----------------------------\n\t" +
                           "1. Mayor-Menor\n\t2. Comparacion\n\t3. Multiplo_de_7\n\t4. Par-Impar\n\t5. Telefonia\n\t6. Salir\n\n\t5" +
                           " FAVOR INGRESAT OPCIÓN: "));

    elif(option==4):
        print("INGRESO DE VALORES");
        a = int(input("Ingrese un numero: "));
        b = int(input("Ingrese otro numero: "));
        c = int(input("Ingrese otro numero: "));
        suma=int(a+b+c)//3
        print("Promedio: ",suma);
        if(suma%2 == 0):
            print("El promdeio es par");
        else:
            print("El promedio es impar");

    elif(option==5):

        name=str(input("Por favor ingrese su nombre: "));
        sec=float(input("Minutos consumidos por nacional:"));
        sec1 = float(input("Minutos consumidos por internacional:"));
        suma=(sec+sec1);

        if(suma>25):
            if(sec>25):
                sec-=25;
                pago=float((sec*0.5)+(sec1*2.25));
                print(name,"Tu pago total es de: Q", pago);
            else:
                resto=25-sec;
                sec1-=resto;
                pago=float(sec1*2.50)
                print(name,"Tu pago total es de: Q", pago);
        else:
            print("Tu llamada ha sido gratis!!");

        option = int(input("\nMENU\n-----------------------------\n\t" +
                           "1. Mayor-Menor\n\t2. Comparacion\n\t3. Multiplo_de_7\n\t4. Par-Impar\n\t5. Telefonia\n\t6. Salir\n\n\t" +
                           " FAVOR INGRESAT OPCIÓN: "));

    elif(option==6):
            break;
            print("Hasta pronto!!");
    else:
        print("\nFavor de ingresar solo opciones validas!!\n");

        option = int(input("\nMENU\n-----------------------------\n\t" +
                           "1. Mayor-Menor\n\t2. Comparacion\n\t3. Multiplo_de_7\n\t4. Par-Impar\n\t5. Telefonia\n\t6. Salir\n\n\t" +
                           " FAVOR INGRESAT OPCIÓN: "));
