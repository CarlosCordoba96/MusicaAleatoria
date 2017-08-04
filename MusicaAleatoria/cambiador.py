from os import *
from glob import glob
import random


class maleatoria():
    def __init__(self,ruta,extension):
        self.ruta=ruta
        self.extension=extension
        lista=self.listar()
        self.renombrar(lista)

    def listar(self):
        return [arch.name for arch in scandir(self.ruta) if arch.is_file() and self.isExtension(arch.name)]


    def isExtension(self,nombre):
        if(nombre[len(nombre)-len(self.extension):]==self.extension):
            return True
        else:
            return False

    def renombrar(self,lista):
        chdir(self.ruta)
        for cancion in lista:
            numeroaleatorio=str(random.randrange(10000))
            nuevoNombre=str("File"+numeroaleatorio+self.extension)
            print(cancion+" Change for -> "+nuevoNombre) 
            rename(cancion,nuevoNombre)
  

        
