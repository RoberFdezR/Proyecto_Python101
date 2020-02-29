#Proyecto Final 
#RANGO DE POPULARIDAD DE UN LISTADO DE PELICULAS
#1- Una ____________ es una fabrica ( o plano) que instancia (crea) ____________
#2- Los objetos tienen un unico ____________ y un conjunto comun de ___________
#3- Una variable de ______________ existe por toda la vida de un ______________
#4- Los metodos _______________ tienen acceso a las variables ____________ de sus objetos
#5- los nombres de Clases inician con una letra _____________
#6- los nombres de Metodos inician con una letra ________________
#7- los nombres de variables inician con una letra ________________

import random 

class Pelicula:
    def __init__(self, title):
        self.rango = random.randint(0,10)
        self.title = title
        print("Title " + self.name + " has been created with " + str(self.rango))

    def get_rango(self):
        return(str(self.rango))

    def get_title(self):
        return(str(self.title))

    def like(self):
        if self.rango + 1 < 10:
            self.rango = self.rango + 1
        else:
            self.rango = 10
            print("title " + self.title + " it now has a rank of " + str(self.rango) + " points of rank.")

    def dislike(self):
        if self.rango - 1 > 0:
            self.rango = self.rango - 1
            if self.rango < 0:
                self.rango = 0    
                print("title " + self.title + " no esta chida.")
            else:
                print("dislike tile " + self.title + " it now has a rank " + str(self.rango) + " points of rank.")            
        else:
            self.rango = 0
            print("title " + self.title + " no esta chida.")


mov1 = title = input("Ingresa un titulo 1: ")
mov2 = title = input("Ingresa un titulo 2: ")
mov3 = title = input("Ingresa un titulo 3: ")
mov4 = title = input("Ingresa un titulo 4: ")
mov5 = title = input("Ingresa un titulo 5: ")
mov6 = title = input("Ingresa un titulo 6: ")
mov7 = title = input("Ingresa un titulo 7: ")
mov8 = title = input("Ingresa un titulo 8: ")
mov9 = title = input("Ingresa un titulo 9: ")
mov10 = title = input("Ingresa un titulo 10: ")

mov10.get_rango()
mov9.get_rango()
mov8.get_rango()
mov7.get_rango()
mov6.get_rango()
mov5.get_rango()
mov4.get_rango()
mov3.get_rango()
mov2.get_rango()
mov1.get_rango()


titles = [mov1, mov2, mov3, mov4, mov5, mov6, mov7, mov8, mov9, mov10]
random.shuffle(titles)