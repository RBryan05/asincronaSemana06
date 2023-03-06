# Actividad asincrona semana 6, código.
print("        ")
print("Practica con variables que manejan operadores aritméticos.")
print("        ")
"Variables y datos que se utilizaran."

# Variables de suma.
sumaNum1 = 35
sumaNum2 = 9
sumaNum3 = 29
# Variables de resta.
restaNum1 = 14
restaNum2 = 3
restaNum3 = 16
restaNum4 = 11
#Variables de multiplicación.
multiNum1 = 3
multiNum2 = 4

# Operador aritmético SUMA: Sumar 3 variables distintas y asignar el valor a una cuarta variable.

print("Operador aritmético: SUMA")
suma = sumaNum1 + sumaNum2 + sumaNum3 

"Concatenación con: f-string"
print(f"El resultado de la suma de {sumaNum1} + {sumaNum2} + {sumaNum3} es igual a: {suma}")
print("        ")

#Operador aritmético RESTA: Restar 4 variables siendo en la tercera variable más alta que la primera.

print("---------------------------------------------------------------------------")
print("Operador aritmético: RESTA")
resta = restaNum1 - restaNum2 - restaNum3 - restaNum4

"Concatenación con: f-string"
print(f"El resultado de la resta de {restaNum1} - {restaNum2} - {restaNum3} - {restaNum4} es igual a: {resta}")
print("        ")

#Multiplicación: Multiplicar 2 variables asignarlas a otra variable y esa variable multiplicar por la segunda variable de suma y resta.

print("---------------------------------------------------------------------------")
print("Operador aritmético: MULTIPLICACIÓN")
multiplicación1 = multiNum1 * multiNum2
multiplicación2 = multiplicación1 * sumaNum2 * restaNum2

"Concatenación con: f-string"
print(f"El resultado de la primera multiplicacion es de {multiNum1} * {multiNum2} es igual a: {multiplicación1}")
print(f"El resultado de la segunda multiplicacion es de {multiplicación1} * {sumaNum2} * {restaNum2} es igual a: {multiplicación2}")
print("        ")

#Exponente: Sacar a la primera variable de la multiplicación el exponente de la segunda variable de la multiplicación

print("---------------------------------------------------------------------------")
print("Operador aritmético: EXPONENTE")
exponente1 = multiNum1 ** multiNum2

"Concatenación con: f-string"
print(f"El resultado del exponente de {multiNum1} ** {multiNum2} es igual a: {exponente1}")
print("        ")

#Sacar el módulo de la primera variable de la suma con la primera variable de la resta

print("---------------------------------------------------------------------------")
print("Operador aritmético: MÓDULO")
modulo1 = sumaNum1 % restaNum1

"Concatenación con: f-string"
print(f"El resultado del modulo de {sumaNum1} ** {restaNum1} es igual a: {modulo1}")
print("        ")

#Dividir la variable resultado del exponente entre la variable resultado del módulo

print("---------------------------------------------------------------------------")
print("Operador aritmético: DIVISIÓN")
division1 = exponente1 / modulo1

"Concatenación con: f-string"
print(f"El resultado de la division de {exponente1} ** {modulo1} es igual a: {division1}")
print("        ")

#Realizar la división entera de la división normal

print("---------------------------------------------------------------------------")
print("Operador aritmético: DIVISIÓN ENTERA")
division1 = exponente1 // modulo1

"Concatenación con: f-string"
print(f"El resultado entero de la division de {exponente1} ** {modulo1} es igual a: {division1}")

print("        ")
print("Con esto concluimos la actilivad de la semana 6 de Fundamentos De Programación")
print("        ")