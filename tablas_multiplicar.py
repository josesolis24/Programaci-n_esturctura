"""
 crear un programa que calcule e calcule e imprima latabla de multiplicar de 2

Restricciones:
1.-sin estuctura de control
2.- sin funciones

"""
num=int(input("insertar el numero de la tabla de multiplicar: "))
print("2 x 1 =", 2 * 1)
print("2 x 2 =", 2 * 2)
print("2 x 3 =", 2 * 3)
print("2 x 4 =", 2 * 4)
print("2 x 5 =", 2 * 5)
print("2 x 6 =", 2 * 6)
print("2 x 7 =", 2 * 7)
print("2 x 8 =", 2 * 8)
print("2 x 9 =", 2 * 9)
print("2 x 10 =", 2 * 10)

#Version 2

"""
crear un programa que calcule e calcule e imprima latabla de multiplicar de 2

Restricciones:
1.-con  estuctura de control
2.- sin funciones

"""
num=int(input("insertar el numero de la tabla de multiplicar:"))
for i in range(1, 11):
   multi=num*i 
   print(f"{num} x {i} = {multi}")
         

#Version 3
"""
crear un programa que calcule e calcule e imprima latabla de multiplicar de 2

Restricciones:
1.-con  estuctura de control
2.- con funciones

"""
def tabla_multiplicar(num):
    for i in range(1, 11):
        multi = num * i
        print(f"{num} x {i} = {multi}")
    
