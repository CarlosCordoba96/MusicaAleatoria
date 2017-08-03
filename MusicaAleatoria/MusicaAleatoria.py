from os import *
from glob import glob
import random

def isExtension(nombre,extension):

    if(nombre[len(nombre)-len(extension):]==extension):
         return True
    else:
       return False

def listar(ruta,extension):
        return [arch.name for arch in scandir(ruta) if arch.is_file() and isExtension(arch.name,extension)]


def renombrar(lista,extension,ruta):
    chdir(ruta)
    for cancion in lista:
        numeroaleatorio=str(random.randrange(10000))
        nuevoNombre=str("Archivo"+numeroaleatorio+extension)
        rename(cancion,nuevoNombre)
        

def main():
    print("Introduce la ruta:")
    #RUTA=input()
    RUTA="E:\\Users\Carlos\Desktop\prueba"
    print("Que tipo de formato quieres cambiar: ")
    #extension=input()
    extension=".txt"
    lista=listar(RUTA,extension)
    renombrar(lista,extension,RUTA)


if __name__=="__main__":
    main()