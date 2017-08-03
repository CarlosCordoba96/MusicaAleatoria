from os import *
from glob import glob


def isExtension(nombre,extension):

    if(nombre[len(nombre)-len(extension):]==extension):
         return True
    else:
       return False

def listar(ruta,extension):
        return [arch.name for arch in scandir(ruta) if arch.is_file() and isExtension(arch.name,extension)]


def renombrar(lista):
    for cancion in lista:
        print(cancion)

def main():
    print("Introduce la ruta:")
    RUTA=input()
   # RUTA="E:\\Users\Carlos\Desktop\prueba"
    print("Que tipo de formato quieres cambiar: ")
    extension=input()
    lista=listar(RUTA,extension)
    renombrar(lista)


if __name__=="__main__":
    main()