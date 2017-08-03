from os import *
from glob import glob
extension=".py"
def listar(ruta):
        return [arch.name for arch in scandir(ruta) if arch.is_file() and ispython(arch.name )]

def ispython(nombre):
    if(nombre[len(nombre)-len(extension):]==extension):
         return True
    else:
       return False

def renombrar(lista):
    for cancion in lista:
        print(cancion)
def main():
    print("Musica en :"+ getcwd())
    lista=listar(getcwd())
    renombrar(lista)


if __name__=="__main__":
    main()