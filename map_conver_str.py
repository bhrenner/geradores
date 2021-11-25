    ### CONVERSÃO STR -> INT
str_nums = ["4", "8", "6", "5", "3", "2", "8", "9", "2", "5"]
int_nums = map(int, str_nums) #Converte para int

#print(int_nums)
#print(list(int_nums))
#print(str_nums)


#numbers = [-2, -1, 0, 1, 2]
#abs_values = list(map(abs, numbers))
#print(abs_values) #TODOS OS VALORES POSITIVOS
#print(list(map(float, numbers))) #TODOS EM FORMATO FLOAT

#words = ["Welcome", "to", "Real", "Python"]
#print(list(map(len, words))) # PALAVRAS PARA NUMEROS CONTANDO AS LETRAS

numbers = [1, 2, 3, 4, 5]
squared = map(lambda num: num ** 2, numbers) #lambda podem desempenhar o papel do primeiro argumento

#print(list(squared))

first_it = [1, 2, 3]
second_it = [4, 5, 6, 7]

#print(list(map(pow, first_it, second_it)))#Esta técnica permite que você mescla dois ou mais iteráveis de valores numéricos usando diferentes tipos de operações matemáticas.

#print(list(map(lambda x, y: x - y, [2, 4, 6], [1, 3, 5])))
#print( list(map(lambda x, y, z: x + y + z, [2, 4], [1, 3], [7, 8])))

string_it = ["processing", "strings", "with", "map"]
#print(list(map(str.capitalize, string_it)))
#print(list(map(str.upper, string_it)))
#print(list(map(str.lower, string_it)))

with_spaces = ["processing ", "  strings", "with   ", " map   "]
#print(list(map(str.strip, with_spaces))) # REMOVE OS ESPAÇOS

with_dots = ["processing..", "...strings", "with....", "..map.."]
#print(list(map(lambda s: s.strip("."), with_dots))) #REMOVE PONTOS COM LAMBDA

    ### Remoção da pontuação
import re

def remove_punctuation(word):
     return re.sub(r'[!?.:;,"()-]', "", word)

#print(remove_punctuation("...Python!"))

text = """Some people, when confronted with a problem, think
 "I know, I'll use regular expressions."
 Now they have two problems. Jamie Zawinski"""

words = text.split() #Coloca todas as palavras em uma lista
#print(words)
#print(list(map(remove_punctuation, words)))##USA map() PARA FAZER O MSM

def rotate_chr(c):
    rot_by = 3
    c = c.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # Keep punctuation and whitespace
    if c not in alphabet:
        return c
    rotated_pos = ord(c) + rot_by
    # If the rotation is inside the alphabet
    if rotated_pos <= ord(alphabet[-1]):
        return chr(rotated_pos)
    # If the rotation goes beyond the alphabet
    return chr(rotated_pos - len(alphabet))

print(ord("a"))
print(ord("b"))
print(chr(97))
print(chr(98))
print(chr(1))
print("".join(map(rotate_chr, "My secret message goes here.")))