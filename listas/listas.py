#exemplo 1
numbers = [10, 5, 7, 2, 1]
print("os numeros", numbers)
print("\n")
numbers[0] = 111
print("os numeros",numbers)
print("\n")
print(numbers[3])
print("\n")
numbers[1] = numbers[4]
print("os numeros",numbers)


#exemplo 2
my_list = [1, None, True, 'I am a string', 256, 0]
print(my_list)

#exemplo 3
numbers = [10, 5, 7, 2, 1]
print("\n list legth:", len(numbers))

#exemplo 4 
numbers = [10, 5, 7, 2, 1]
print("os numeros",numbers)
del numbers[1]
print("os numeros", numbers)

#----------------------------------------------
#Funcoes X Metodos / com lista
#----------------------------------------------
#exemplo: funcao
#result  = function(arg)
#exemplo: metodo
#result = data.method(arg)

#exemplo 5
numbers = [10, 5, 7, 2, 1]
print("os numeros",numbers)
print("\n")
numbers.append (4)
print("os numeros", numbers)
print("\n")
numbers.insert (0,222)
print("os numeros", numbers)
print("\n")

#exemplo 6 
my_list = []
for i in range(5):
    my_list.append (i + 1)
print(my_list)

#exemplo 7
my_list = []
for i in range(5):
    my_list.append (i + 1)
print(my_list)
for i in range(len(my_list)):
    total += i
print(total)

#exemplo 8
total = 0
my_list = []
for i in range(5):
    my_list.append (i + 1)
print(my_list)
for i in my_list:
    total += i
print(total)     


#exemplo 9 
my_list = [10, 1, 8, 3, 5]
print(my_list)
my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1] 
print(my_list)
            