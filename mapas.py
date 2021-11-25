#numbers = [1, 2, 3, 4, 5]
#squared = []

#for num in numbers:
#    squared.append(num ** 2)

#print(squared)

def square(number): #square() é uma função de transformação que mapeia um número para seu valor quadrado.
    return number ** 2

numbers = [1, 2, 3, 4, 5]

squared = map(square, numbers)

print(list(squared))