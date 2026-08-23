a = 10
b = 20
a, b =  b , a
print(a,b)

#Swapping two numbers using temp variable
a = 10
b = 20
temp = a
a = b
b = temp
print(a,b)

#Swapping two numbers using arithemetic operation
a = 20
b = 10
a = a + b
b = a - b
a = a - b
print(a,b)

#Swapping two numbers using XOR opeartor
a = 20
b = 10
a = a ^ b
b = a ^ b
a = a ^ b
print(a,b)
