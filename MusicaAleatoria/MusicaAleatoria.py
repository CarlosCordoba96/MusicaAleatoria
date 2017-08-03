from maleatoria import maleatoria

def main():
    print("Introduce la ruta:")
    #RUTA=input()
    RUTA="E:\\Users\Carlos\Desktop\prueba"
    print("Que tipo de formato quieres cambiar: ")
    #extension=input()
    extension=".txt"
    musica=maleatoria(RUTA,extension)


if __name__=="__main__":
    main()