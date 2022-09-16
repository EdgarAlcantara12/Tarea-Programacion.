# Escribir un programa que pida 2 números y muestre paso a paso el cálculo de la raíz cuadrada de la suma del cuadrado de ambos.
#Importamos math.
import math


#ingresar numeros.
#Ingresa tu numero: Ejemplo Primer valor:5 , Segundo valor: 6
intA = int(input("Escribe tu primer valor "))
intB = int(input("Escribe tu segundo valor "))

#imprimimos la operacion.
print(intA,"2", "+", intB,"2" )

#Variables.
potA = (intA**2)
potB = (intB**2)

#variable sumpot se encargar de elevar al exponente y sumar.
sumpot = (intA**2 + intB**2)

#Imprimimos valores de pot A y B, Tambien la sumatoria.
print(potA, "+", potB)
print(sumpot)

#imprimimos los resultados.
print("Resultado Final =", math.sqrt(sumpot))

