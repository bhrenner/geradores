def dicio(cols, lista):
    company_dicts = (dict(zip(cols, d)) for d in lista)
    return company_dicts

"""
num1 = [4, 5, 6]
num2 = [5, 6, 7]

result = map(lambda n1, n2: n1+n2, num1, num2)
print(list(result))

"""

"""players = ['Alice', 'Bob', 'Cloe', 'Dain']
pla = [135, 138, 957, 456]
default_value_gen = (p for p in pla for x in range(len(players)))
d = dict(zip(players, default_value_gen))
"""

"""snakes = ['Anaconda', 'Python', 'Cobra', 'Boa', 'Lora']
colors = ['green', 'green', 'red', 'light-green', 'green-brown']

d = dict(zip(snakes, colors))
print(d)"""

# User-defined function to pass to map()
# function as the first argument
def getLength(iterable):
    return len(iterable)

def show_result(map_object):
    for item in map_object:
        print(item, end=' ')
    print('')  # for new line

# Generic Function to print the iterator and its content
def print_Iter(iter_in):
    if isinstance(iter_in, str):
        print("The input iterable, '{}' is a String. Its length is {}.".format(iter_in, len(iter_in)))
    if isinstance(iter_in, (list, tuple, set)):
        print("The input iterable, {} is a {}. It has {} elements.".format(iter_in, type(iter_in).__name__, len(iter_in)))
        for item in iter_in:
            print("The {} contains '{}' and its length is {}.".format(type(iter_in).__name__, item, len(item)))
    if isinstance(iter_in, dict):
        print("The input iterable, {} is a {}. It has {} elements.".format(iter_in, type(iter_in).__name__, len(iter_in)))
        for key, value in iter_in.items():
            print("Dict key is '{}' and value is {}.".format(key, value))


"""
 Desc:
  Python map() function to apply on a List iterable
"""

# Considering List as our iterable parameter
iter_List = ["Python", "CSharp", "Java"]
print_Iter(iter_List)

# Calling map() function on a list
map_result =  map(getLength, iter_List)
print("Type of map_result is {}".format(type(map_result)))

# Printing map() output
print("Lengths are: ")
show_result(map_result)
