'''def suma():
    n1 = int(input('numero 1: '))
    n2 = int(input('numero 2: '))
    print(n1+n2)
    print('Gracias por sumar')

try:
    suma()
    # Codigo que queremos probar
except  TypeError:
    print('Estas intentando concatenar tipos distintos')
    # Codigo a ejecutar si no hay error
except ValueError:
    print('Ese no es un numero')
else:
    print('Hiciste todo bien')
    # Codigo a ejecutar si no hay un error
finally:
    print('Eso fue todo')
    # Codigo que se va a ejecutar de todos modos'''

def pedir_numero():

    while True:
        try:
            numero = int(input('Dame un numero: '))
        except:
            print('Ese no es un numero')
        else:
            print(f'Ingresaste el numero {numero}')
            break
    print('Gracias')

pedir_numero()