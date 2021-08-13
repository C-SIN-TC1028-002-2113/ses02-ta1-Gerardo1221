def main():
    #escribe tu código abajo de esta línea
    edad=int(input("Dame tu edad: "))
    año_act=int(input("Dame el año actual: "))
    edadfaltante=int(100-edad)
    edad_100=int(edadfaltante+año_act)
    print("Cumplirás 100 años en el año:",edad_100)



if __name__ == '__main__':
    main()
