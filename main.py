def run():
    print('Bienvenido!!!\n')
    print('Ingrese las medidas del equipo: ')
    while True:
    try:
        cadera = talle_cadera()
        break
    except ValueError:
        print("ERROR : ingrese un numero: ")
    
    while True:
    try:
        cintura = talle_cintura()
        break
    except ValueError:
        print("ERROR : ingrese un numero: ")
    
    while True:
    try:
        ldbrazo = talle_ld()
        break
    except ValueError:
        print("ERROR : ingrese un numero: ")


if __name__ == '__main__':
    run()