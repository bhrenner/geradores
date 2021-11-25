        ### Combinando com outras ferramentas funcionais map()

import math

def is_positive(num):
     return num >= 0


def sanitized_sqrt(numbers):
     cleaned_iter = map(math.sqrt, filter(is_positive, numbers)) # Pega a raiz de cada num, e retorna só os positivos
     return list(cleaned_iter)

#print(sanitized_sqrt([25, 9, 81, -16, 0]))

    ## map() e reduce()

#reduce() aplicar-se-á a todos os itens e calcular cumulativamente um valor final

import functools
import operator
import os
import os.path

#files = os.listdir(os.path.expanduser("~"))#chama os.listdir() nesse caminho para obter uma lista com os caminhos de todos os arquivos que vivem no diretório

#print(functools.reduce(operator.add, map(os.path.getsize, files)))
#print(sum(map(os.path.getsize, files)))

    #Processando iteráveis baseados em tupla com starmap()
def starmap(function, iterable):
    for args in iterable:
        yield function(*args)

from itertools import starmap
#print(list(starmap(pow, [(2, 7), (4, 3)]))) # Faz um numero elevado a outro 2^7, usa pow() para calcular o poder do primeiro valor elevado para o segundo valor em cada tupla. 
#print(list(map(pow, (2, 7), (4, 3)))) #valor sai diferente porque leva duas tuplas em vez de uma lista de tuplas.
#print(list(map(pow, (2, 4), (7, 3)))) # Nesse caso sai o mesmo resultado porque Agora a primeira tupla fornece as bases e a segunda fornece os expoentes

        ### Codificação com estilo pythonic: substituição map()
    #Usando compreões de lista

 # Transformation function
def square(number):
     return number ** 2

numbers = [1, 2, 3, 4, 5, 6]

 # Using map()
print(list(map(square, numbers)))

print([square(x) for x in numbers])
# Using map()
map_obj = map(square, numbers)
print(map_obj)
print(list(map_obj))
# Using a generator expression
gen_exp = (square(x) for x in numbers)
print(gen_exp)
print(list(gen_exp))

"""Expressões geradoras são comumente usadas como argumentos em chamadas de função. 
Neste caso, você não precisa usar parênteses para criar a expressão do gerador porque 
os parênteses que você usa para chamar a função também fornecem a sintaxe para construir 
o gerador."""

gen2_exp = list(square(x) for x in numbers)
print(gen2_exp)