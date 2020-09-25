#valores de todos los talles
TALLE_XS=0
TALLE_S=1
TALLE_M=2
TALLE_L=3
TALLE_XL=4
TALLE_XXL=5
TALLE_XXXL=6
ESPECIAL=7
def talle_cadera():
    
    while True:
        try:
            pecho = int(input("INGRESE MEDIDA DE PECHO:  "))
            break
        except ValueError:
            print("ERROR : ingrese un numero")

    if 82 <= pecho <= 90:
        tallePecho = TALLE_XS
        print (pecho, "usted es talle XS")
    elif 91 <= pecho <= 98:
        tallePecho = TALLE_S
        print (pecho, "usted es talle S") 
    elif 99 <= pecho <= 106: 
        tallePecho = TALLE_M 
        print (pecho, "usted es talle M")
    elif 107 <= pecho <= 114:  
        tallePecho = TALLE_L
        print (pecho, "usted es talle L")
    elif 115 <= pecho <= 123: 
        tallePecho = TALLE_XL 
        print (pecho, "usted es talle XL")
    elif 124 <= pecho <= 135: 
        tallePecho = TALLE_XXL
        print (pecho, "usted es talle XXL")
    elif 136 <= pecho <= 147: 
        tallePecho = TALLE_XXXL 
        print (pecho, "usted es talle 3XL")
    else :
        print (pecho, "usted es un talle Especial")
            
def talle_cintura():
    pass
def talle_ldbrazo():
    pass
def talle_entrepierna():
    pass

def run():
    print('Bienvenido!!!\n')
    print('Ingrese las medidas del equipo: ')
    talle_cadera()
    talle_cintura()
    talle_ldbrazo()
    talle_entrepierna()


if __name__ == '__main__':
    run()