
"""
  Una función es un conjunto de instrucciones agrupadas bajo un nombre en particular como un programa mas pequeño que cumple una funcion especifica. La funcion se puede reutulizar con el simple hecho de invocarla es decir mandarla llamar 

  Sintaxis:

   def nombredeMifuncion(parametros):
      bloque o conjunto de instrucciones

   nombredeMifuncion(parametros)

   Las funciones pueden ser de 4 tipos
  
    Funciones de tipo "Procedimiento" 
   1.- Funcion que no recibe parametros y no regresa valor
   3.- Funcion que recibe parametros y no regresa valor
    
    Funciones de tipo "Funcion"
   2.- Funcion que no recibe parametros y regresa valor
   4.- Funcion que recibe parametros y regresa valor

"""
#1.- Funcion que no recibe parametros y no regresa valor
def solucitarDatos1():
    nombre=input("Nombre")
    telefono=input("Telefono")
    print("Nombre:" +nombre+ "y su telefono " +telefono)
#3.- Funcion que recibe parametros y no regresa valor
def solucitarDatos3(nom,tel):
    nombre=nom
    telefono=tel 
    print("Nombre:" +nombre+ "y su telefono " +telefono)

#2.- Funcion que no recibe parametros y regresa valor
def solucitarDatos2():
    nombre=input("Nombre")
    telefono=input("Telefono")
    return nombre, telefono

#4.- Funcion que recibe parametros y regresa valor
def solucitarDatos4(nom, tel):
    nombre=nom
    telefono=tel
    return nombre, telefono

#Mandar a lla,ar o invocar la funcion 

solucitarDatos1()


nombre=input("escribe el nombre")
telefono=input("Escribeel telefono:")
solucitarDatos3(nombre, telefono)

nom, tel=solucitarDatos2()
print(f"/t/nLos datos de la agenda son: /n Nombre: {nom} /n Telefono: {tel}")

nombre=input("Escribe el nombre: ")
telefono=input("Escribe el telefono: ")
nom,tel=solucitarDatos4(nombre,telefono)
print(f"\t\nLos datos de la Agenda son:\n Nombre: {nom}\n Telefono:{tel}")
