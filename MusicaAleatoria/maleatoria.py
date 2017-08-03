from os import *
from glob import glob
import random


class maleatoria():
    def __init__(self,ruta,extension):
        self.ruta=ruta
        self.extension=extension

    def listar(self):
        return [arch.name for arch in scandir(self.ruta) if arch.is_file() and isExtension(arch.name,extension)]

    def renombrar(self):
        chdir(self.ruta)
        for cancion in lista:
            numeroaleatorio=str(random.randrange(10000))
            nuevoNombre=str("Archivo"+numeroaleatorio+self.extension)
            print(nombre+" Cambia por -> "+nuevoNombre) 
            rename(cancion,nuevoNombre)


    def actuar(self):
        lista=listar()
        renombrar(lista)
       
   



