#numbers = [-2, -1, 0, 1, 2]
#def extract_positive(numbers):
#     positive_numbers = []
 #    for number in numbers:
 #        if number > 0:  # Filtering condition
#             positive_numbers.append(number)
#     return positive_numbers

#print(extract_positive(numbers))
#positive_numbers = filter(lambda n: n > 0, numbers)
#print(positive_numbers)
#print(list(positive_numbers))
#def is_positive(n):
#     return n > 0

#print(list(filter(is_positive, numbers)))

#def identity(x):
#     return x

#identity(42)
#objects = [0, 1, [], 4, 5, "", None, 8]
#print(list(filter(identity, objects)))

#numbers = [1, 3, 10, 45, 6, 50]

#def extract_even(numbers):
#     even_numbers = []
#     for number in numbers:
#         if number % 2 == 0:  # Filtering condition
#             even_numbers.append(number)
#     return even_numbers

#def is_even(number):
#     return number % 2 == 1  # Filtering condition

#print( extract_even(numbers))
#lista = list(filter(is_even, numbers))
#print(lista)

#import math

#def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(math.sqrt(n)) + 1):
#         if n % i == 0:
#             return False
#     return True

#print(is_prime(5))
#print(is_prime(12))
#print(list(filter(is_prime, range(1, 51)))) #Esta chamada para extrair todos os números primos na faixa

#import statistics as st
#sample = [10, 8, 10, 8, 2, 7, 9, 3, 34, 9, 5, 9, 25]
#mean = st.mean(sample)

#print(mean)
#stdev = st.stdev(sample)
#low = mean - 2 * stdev
#high = mean + 2 * stdev
#clean_sample = list(filter(lambda x: low <= x <= high, sample))
#print(clean_sample)

#print(st.mean(clean_sample))

#words = ["variable", "file#", "header", "_non_public", "123Class"]
#print(list(filter(str.isidentifier, words)))
    ### Encontrando palavras do palíndromo
#def is_palindrome(word):
#     reversed_word = "".join(reversed(word))
#     return word.lower() == reversed_word.lower()

#print( is_palindrome("Racecar"))

#print(is_palindrome("Python"))

#words = ("filter", "Ana", "hello", "world", "madam", "racecar", 'ovo', 'bob')
#print(list(filter(is_palindrome, words)))

        ### A Praça dos Números Pares: e filter()map()
#numbers = [1, 3, 10, 45, 6, 50]
#def is_even(number):
#    return number % 2 == 0

#even_numbers = list(filter(is_even, numbers))
#print(even_numbers)
#print(list(map(lambda n: n ** 2, even_numbers)))
#print(list(map(lambda n: n ** 2, filter(is_even, numbers)))) #mostra como combinar e em uma única expressão

        ### A Soma dos Números Pares: e filter()reduce()
#from functools import reduce
#numbers = [1, 3, 10, 45, 6, 50]

#def is_even(number):
 #   return number % 2 == 0
#even_numbers = list(filter(is_even, numbers))
#print(reduce(lambda a, b: a + b, even_numbers))
#print(reduce(lambda a, b: a + b, filter(is_even, numbers)))

        ### Filtrando iteráveis com filterfalse() -- números ímpares
from itertools import filterfalse
numbers = [1, 3, 10, 45, 6, 50]

#def is_even(number):
 #    return number % 2 == 0

#print(list(filterfalse(is_even, numbers))) # devolve os numeros contrarios a funcao

    ##Filtrando os valores da NaN
#import statistics as st

#sample = [10.1, 8.3, 10.4, 8.8, float("nan"), 7.2, float("nan")]
#print(st.mean(sample))

# Generating a list with filter()
#list(filter(function, iterable))

# Generating a list with a list comprehension
#[item for item in iterable if function(item)]

def is_even(x):
     return x % 2 == 0

print(list(filter(is_even, numbers))) # Use filter()
print([number for number in numbers if is_even(number)])# Use a list comprehension

even_numbers = filter(is_even, numbers)
print(even_numbers)
print(list(even_numbers))

# Use a generator expression
even_numbers = (number for number in numbers if is_even(number))
print(even_numbers)

print(list(even_numbers))

        ## Uma expressão de gerador é tão eficiente quanto um chamado em termos de consumo 
        # de memória. Ambas as ferramentas devolvem iteradores que rendem itens sob demanda. 
        # Usar qualquer um pode ser uma questão de gosto, conveniência ou estilo. Então, 
        # você está no comando!filter()