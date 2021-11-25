    ### Transformando Iteráveis de Números com Python's map()

def powers(x):
     return x ** 2, x ** 3

numbers = [1, 2, 3, 4]
#print(list(map(powers, numbers))) #cada chamada para retornar uma tupla com dois valores.

import math

numb = [1, 2, 3, 4, 5, 6, 7]
#print(list(map(math.factorial, numb))) #Transforma em uma nova lista contendo o fatorial de cada número na lista original.

def to_fahrenheit(c):
    return 9 / 5 * c + 32

def to_celsius(f):
    return (f - 32) * 5 / 9

celsius_temps = [100, 40, 80]
# Convert to Fahrenheit
#print(list(map(to_fahrenheit, celsius_temps)))

fahr_temps = [212, 104, 176]
# Convert to Celsius
#print(list(map(to_celsius, fahr_temps)))

        ### Conversão de strings em números

    # Convert to floating-point
#print(list(map(float, ["12.3", "3.3", "-15.2"])))

    # Convert to integer
#print(list(map(int, ["12", "3", "-15"])))

def to_float(number):
     try:
         return float(number.replace(",", "."))
     except ValueError:
         return float("nan")

print(list(map(to_float, ["12.3", "3,3", "-15.2", "One"]))) #Dentro, você usa uma instrução de tentativa que captura um se falha ao converter . 
                                                            #sua função retorna convertida em um número de ponto flutuante válido
                                                            #Caso contrário, você recebe um valor nan (Not a Number)
                                                    

