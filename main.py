#valores de todos los talles
TALLE_XS=0
TALLE_S=1
TALLE_M=2
TALLE_L=3
TALLE_XL=4
TALLE_XXL=5
TALLE_XXXL=6
ESPECIAL=7
#todas las funciones de los talles cumplen casi la misma funcion pero con distintas variables.
def talle_pecho():
    
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

def talle_cadera():
    while True:
        try:
            cadera = int(input("INGRESE MEDIDA DE CADERA:  "))
            break
        except ValueError:
            print("ERROR : ingrese un numero")

    if 101 <= cadera <= 108:
        talleCadera = TALLE_XS
        print (cadera, "usted es talle XS")
    elif 109 <= cadera <= 116:
        talleCadera = TALLE_S
        print (cadera, "usted es talle S")    
    elif 117 <= cadera <= 125:  
        talleCadera = TALLE_M
        print (cadera, "usted es talle M")
    elif 126 <= cadera <= 137:  
        talleCadera = TALLE_L
        print (cadera, "usted es talle L")
    elif 138 <= cadera <= 149:
        talleCadera = TALLE_XL  
        print (cadera, "usted es talle XL")
    elif 150 <= cadera <= 161:  
        talleCadera = TALLE_XXL
        print (cadera, "usted es talle XXL")
    elif 162 <= cadera <= 173:  
        talleCadera = TALLE_XXXL
        print (cadera, "usted es talle 3XL")
    else :
        print (cadera,"usted es un talle Especial")

def talle_cintura():
    while True:
        try:
            cintura = int(input("INGRESE MEDIDA DE CINTURA:  "))
            break
        except ValueError:
            print("ERROR : ingrese un numero")

    if 70 <= cintura <= 78:
        talleCintura = TALLE_XS
        print (cintura, "usted es talle XS")
    elif 79 <= cintura <= 86:
        talleCintura = TALLE_S
        print (cintura, "usted es talle S")    
    elif 87 <= cintura <= 94:  
        talleCintura = TALLE_M
        print (cintura, "usted es talle M")
    elif 95 <= cintura <= 102:  
        talleCintura = TALLE_L
        print (cintura, "usted es talle L")
    elif 103 <= cintura <= 111:
        talleCintura = TALLE_XL 
        print (cintura, "usted es talle XL")
    elif 112 <= cintura <= 123:  
        talleCintura = TALLE_XXL
        print (cintura, "usted es talle XXL")
    elif 124 <= cintura <= 135:  
        talleCintura = TALLE_XXXL
        print (cintura, "usted es talle 3XL")
    else :
        print ("usted es un talle Especial")

def talle_ldbrazo():
    while True:
        try:
            ldbrazo = int(input("INGRESE MEDIDA DE LARGO DE BRAZO:  "))
            break
        except ValueError:
            print("ERROR : ingrese un numero")
    
    if 55 <= ldbrazo <= 61:
        talleldbrazo = TALLE_XS  
        print (ldbrazo, "usted es talle XS")
    elif 62 <= ldbrazo <= 63:
        talleldbrazo = TALLE_S
        print (ldbrazo, "usted es talle S")    
    elif 64 <= ldbrazo <= 65:
        talleldbrazo = TALLE_M  
        print (ldbrazo, "usted es talle M")
    elif 66 <= ldbrazo <= 67:
        talleldbrazo = TALLE_L  
        print (ldbrazo,"usted es talle L")
    elif 68 <= ldbrazo <= 69:
        talleldbrazo = TALLE_XL  
        print (ldbrazo, "usted es talle XL")
    elif 70 <= ldbrazo <= 71:
        talleldbrazo = TALLE_XXL  
        print (ldbrazo, "usted es talle XXL")
    elif 72 <= ldbrazo <= 73:
        talleldbrazo = TALLE_XXXL  
        print (ldbrazo, "usted es talle 3XL")
    else :
        print ("usted es un talle Especial")  
        print (ldbrazo)

def talle_entrepierna():
    while True:
        try:
            entrepierna = int(input("INGRESE MEDIDA DE ENTREPIERNA:  ")) 
            break
        except ValueError:
            print("ERROR : ingrese un numero")

    if 55 <= entrepierna <= 80: 
        print ("usted es talle XS")         
        talleentrepierna = TALLE_XS   
    elif 81 <= entrepierna <= 84:
        talleentrepierna = TALLE_S
        print (entrepierna, "usted es talle S")    
    elif 85 <= entrepierna <= 88:
        talleentrepierna = TALLE_M  
        print (entrepierna, "usted es talle M")
    elif 89 <= entrepierna <= 92:
        talleentrepierna = TALLE_L 
        print (entrepierna, "usted es talle L")
    elif 93 <= entrepierna <= 96:
        talleentrepierna = TALLE_XL
        print (entrepierna, "usted es talle XL")
    elif 97 <= entrepierna <= 100:
        talleentrepierna = TALLE_XXL 
        print (entrepierna, "usted es talle XXL")
    elif 101 <= entrepierna <= 120:
        talleentrepierna = TALLE_XXXL 
        print (entrepierna, "usted es talle 3XL")
    else :
        print (entrepierna, "usted es un talle Especial")

def run():
    print('Bienvenido!!!\n')
    print('Ingrese las medidas del equipo: ')
    #llamo a las funciones que me retornan el talle de cada parte del cuerpo
    talle_pecho()
    talle_cadera()
    talle_cintura()
    talle_ldbrazo()
    talle_entrepierna()


if __name__ == '__main__':
    run()