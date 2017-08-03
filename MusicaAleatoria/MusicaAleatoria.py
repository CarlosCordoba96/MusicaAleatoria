from os import *
from glob import glob
def listar(ruta):
        return [arch.name for arch in scandir(ruta) if arch.is_file()]  



def renombrar(lista):
    for cancion in lista:
        print(cancion)
def main():
    print("Musica en :"+ getcwd())
    lista=listar(getcwd())
    renombrar(lista)


if __name__=="__main__":
    main()