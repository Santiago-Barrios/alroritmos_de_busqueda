import time

def factorial(n):
    respuesta = 1

    while n > 1:
        respuesta *= n
        n -= 1

    return respuesta

def factorial_r(n):

    if n == 1 or n == 0:
        return 1
    
    return factorial(n)

if __name__ == '__main__':
    n = int(input('Ingresa el numero del cual deseas saber su factorial: '))

    comienzo = time.time()
    factorial_r(n)
    final = time.time()
    print(f' {final - comienzo} ')

    comienzo = time.time()
    factorial(n)
    final = time.time()
    print(f' {final - comienzo} ')