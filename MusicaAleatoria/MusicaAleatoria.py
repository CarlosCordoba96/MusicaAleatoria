import cambiador

def main():
    print("Introduce the path where the files are: ")
    Path=input()
    print("Which format have the files, '.mp3', '.py'? : ")
    extension=input()
    musica=cambiador.maleatoria(Path,extension)


if __name__=="__main__":
    main()