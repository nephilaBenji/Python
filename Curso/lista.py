import random 

my_list = [0,1,2,3,4,5,6]
my_list_1 = ["abobrinha", 2, "café", 3.14]
elementos = len(my_list)

print(type (my_list))
print(my_list)
print(my_list_1)

for elemento in my_list:
    print(elemento)

for elemento in my_list_1:
    print(elemento)

elemento_1 = my_list_1[2]

elemento_2 = random.choice(my_list_1)

print(elemento_1)
print(elemento_2)
print(elementos)
