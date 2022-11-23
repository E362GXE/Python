print("============Tabla de ultiplicar 1 al 10===========");
num=int(input("Ingrese un numero entero: "));
if(num<0):
    num *= -1;
start=int(input("Ingrese la pocisión inicial: "));
end=int(input("Ingrese la pocisión fianl: "));
print("-------Tabla---------de: ", num);
for n in range (start,end+1):
    print(num,"*",n,"=", num*n);