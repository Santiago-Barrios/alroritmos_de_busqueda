import random

def busqueda_lineal( lista, objetivo):
    matche = False

    for elemento in lista: # O(n)
        if elemento == objetivo:
            matche = True
            break
    return matche

def run():
    tamano_de_la_lista = int(input('De que tamaño sera la lista? '))
    objetivo = int(input('Que número quieres encontrar? '))

    lista=[random.randint(0, 100) for i in range (tamano_de_la_lista)]

    encontrado = busqueda_lineal(lista, objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista ')

if __name__ == '__main__':
    run()