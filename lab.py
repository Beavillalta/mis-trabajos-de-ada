# variable tipo cadena

nombre_pais_de_nacimiento = "Honduras"

# variable tipo numero real

poblacion = 10117.001

# variable tipo entero 

departamentos_de_Honduras = 18

# variable tipo boolean

es_pais_Honduras = True

informacion = nombre_pais_de_nacimiento + "\n" + str(poblacion) + "\n" + str(departamentos_de_Honduras)
print(informacion)

"""  Límites de los enteros en Python: Enteros con signo (int): 

En Python, los enteros con signo son representados utilizando la notación de complemento a dos. El límite superior e inferior de los enteros con signo depende de la arquitectura de la máquina en la que se ejecuta Python. En la mayoría de las plataformas modernas de 32 bits, el límite inferior es -2,147,483,648 y el límite superior es 2,147,483,647. En plataformas de 64 bits, estos límites son mucho mayores.

Enteros sin signo (int): Python no tiene un tipo de dato específico para enteros sin signo, pero puedes utilizar enteros con signo para representar valores no negativos. Esto significa que el límite superior de los enteros no negativos será mayor que el límite superior de los enteros con signo en la misma plataforma.

Límites de los números de punto flotante en Python:

Números de punto flotante de precisión simple (float): En Python, los números de punto flotante de precisión simple siguen el estándar IEEE 754 de 32 bits. Tienen una precisión limitada y un rango limitado. El número más pequeño representable es del orden de 1e-38, y el número más grande es del orden de 1e38. Sin embargo, más allá de estos valores, los números de punto flotante pueden perder precisión y sufrir de desbordamiento o bajo flujo.

Números de punto flotante de doble precisión (float): Python también admite números de punto flotante de doble precisión, que siguen el estándar IEEE 754 de 64 bits. Tienen una precisión mucho mayor y un rango más amplio. El número más pequeño representable es del orden de 1e-308, y el número más grande es del orden de 1e308. """


# La fórmula para calcular la suma de los primeros n números pares es:

# suma = n * (n + 1)

# solicitar valor

n = int(input("Ingrese un valor entero para n: "))

suma = n * (n + 1)

print(f"el valor de la suma es {suma}")

