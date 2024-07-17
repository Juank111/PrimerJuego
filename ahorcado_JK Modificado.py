## Juego del Ahorcado
## Modificado por Juank

import random
import string


from Diccionario import palabras
from graficos_jk import vidas_diccionario_visual 

def palabra_valida(palabras):
    palabra = random.choice(palabras)

    while '_' in palabra or ' ' in palabra:
            palabra = random.choice(palabras)

    return palabra.upper()
    


def ahorcado():

    print("**************************************")
    print("*       Bienvenido(a) al juego del ahorcado       *")
    print("*            Juego modificado por Juank            *")
    print("*            Aprendiendo Python en 2022           *")
    print("**************************************")

    palabra = palabra_valida(palabras)

    letras_X_adivinar = set(palabra)
    letras_usadas = set()
    abcdario = set(string.ascii_uppercase)

    vidas = 10

    while len(letras_X_adivinar) > 0 and vidas > 0:

        if vidas == 10:
            print (f"Arrancas con {vidas} vidas y voy a estar contando tus letras: {' '.join(letras_usadas)}")
            adivinar = [letra if letra in letras_usadas else '_' for letra in palabra]
            print(vidas_diccionario_visual[vidas])
            print(f"palabra: {' '.join(adivinar)}")


        if vidas > 1 and vidas <10:
            print (f"Te quedan {vidas} vidas y has usado estas letras: {' '.join(letras_usadas)}")
            adivinar = [letra if letra in letras_usadas else '_' for letra in palabra]
            print(vidas_diccionario_visual[vidas])
            print(f"palabra: {' '.join(adivinar)}")
        elif vidas == 1:
            print (f"Te queda {vidas} vida! Mira bien las letras que has usado: {' '.join(letras_usadas)}")
            print("\n OJO ! Estás a punto de ser ahorcado. ")
            adivinar = [letra if letra in letras_usadas else '_' for letra in palabra]
            print(vidas_diccionario_visual[vidas])
            print(f"palabra: {' '.join(adivinar)}")

        letra_escogida = input("Por favor escoge y digita una letra:  ").upper()

        if letra_escogida in abcdario - letras_usadas:
            letras_usadas.add(letra_escogida)
            if letra_escogida in letras_X_adivinar:
                letras_X_adivinar.remove(letra_escogida)
                print(' ')

            else:
                vidas = vidas - 1
                print(f"\n  Tu letra {letra_escogida} no está en la palabra. ")
        elif letra_escogida in letras_usadas:
            print("\n Upsss!! Ya habías escogido esa letra. Por favor digita otra nueva ")
        else:
            print("\n Esta letra no es válida. ")
    
    if vidas == 0:
        print (vidas_diccionario_visual[vidas]) 
        print(f"Estás ahorcado!, perdiste!  ...cuanto lo lamento! La palabra era: {palabra}")

    elif vidas > 1: 
        print(f"Excelente!!  has adivinado la palabra  {palabra}! ")
        print (f"Quedaste con {vidas} vidas y usaste estas letras: {' '.join(letras_usadas)}")
        print(vidas_diccionario_visual[20])

    else:
        print(f"WOW! Estuviste cerca!! Lograste adivinar la palabra  {palabra}! ")
        print (f"Quedaste con {vidas} vida y usaste todas estas letras: {' '.join(letras_usadas)}")
        print(vidas_diccionario_visual[20])

ahorcado()


