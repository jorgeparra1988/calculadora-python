print("ESTE PROGRAMA REALIZARÁ UNA OPERACIÓN ENTRE DOS NÚMEROS ELEGIDOS POR EL USUARIO\n")
numero1=float(input("Escriba el primer número:"))
numero2=float(input("Escriba el segundo número:"))
print("\nOperaciones posibles\n+...Suma\n-...Resta\n/...División\n*...Multiplicación")
simbolo=input("\nEscriba el símbolo de la operación a ejecutar:")
suma="+"
resta="-"
multiplicacion="*"
division="/"
if simbolo==suma:
    print(numero1,simbolo,numero2,"=",numero1+numero2)
elif simbolo==resta:
    print(numero1,simbolo,numero2,"=",numero1-numero2)
elif simbolo==multiplicacion:
    print(numero1,simbolo,numero2,"=",numero1*numero2)
elif simbolo==division:
    print(numero1,simbolo,numero2,"=",numero1/numero2)

else:
    print("ERROR: Simbolo de operacion invalido. Intentelo nuevamente.")






