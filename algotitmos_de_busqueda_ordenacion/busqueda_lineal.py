import random

def busqueda_lineal( lista, objetivo, iter_lin=0):
    matche = False

    for elemento in lista: # O(n)
        iter_lin += 1
        if elemento == objetivo:
            matche = True
            break
    return (matche, iter_lin)

def run():
    tamano_de_la_lista = int(input('De que tamaño sera la lista? '))
    objetivo = int(input('Que número quieres encontrar? '))

    lista=[random.randint(0, 100) for i in range (tamano_de_la_lista)]

    (encontrado, iter_lin) = busqueda_lineal(lista, objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista ')
    print(f'El número de iteraciones fue {iter_lin} ')

if __name__ == '__main__':
    run()