
print("Ejemplo Python");
name=str(input("Ingrese su nombre:"));
num1=int(input("Ingrese un numero:"));
num2=int(input("Ingrese otro numero:"));
resultado=num1+num2;
#otra forma
#resultado=float(num1+num2);
print("El resultado es: ",float(resultado));
print("Ejercicios de operaciones modulares");
print("SUMA");
a1=int(input("ingrse un numero: "));
a2=int(input("ingrese otro numero: "));
b=int(a1-a2);
print("Resultado:",b);
#\n=salto de linea
print("Otros Ejemlos");
c=int(9-3);
print(c);
d=float(8*2.5);
print(d);
e=int(9//2);
print(e);
f=int(9/-2);
print(f);
g=int(9%2);
print(g);
h=int(9%-2);
print(h);
i=int(9%-2.0);
print(i);
j=int(4+3*5);
print(j);
k=int(4+3)*5;
print(k);

num=int(input("Ingrese un numero entero: "));
if(num>0):
    mesaje="El numero es positivo";
elif(num==0):
    mensaje="El numero es neutro";
else:
    mensaje="El numero es negativo";

    print(num,mensaje);

