class Coordenada:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distancia(self, otra_coordenada ):
        x_diff = (self.x - otra_coordenada.x)**2
        y_diff = (self.y - otra_coordenada.y)**2
        return( (x_diff + y_diff)**0.5)


def run():
    coordx_1 = int(input('ingrese el valor en x de la coordenada 1: '))
    coordy_1 = int(input('ingrese el valor en y de la coordenada 1: '))
    coordx_2 = int(input('ingrese el valor en x de la coordenada 2: '))
    coordy_2 = int(input('ingrese el valor en y de la coordenada 2: '))

    coord_1 = Coordenada( coordx_1, coordy_1 )
    coord_2 = Coordenada( coordx_2, coordy_2 )

    print( 'La distancia entre los puntos es = ' )
    print( coord_1.distancia(coord_2) )
    print( isinstance(coord_2, Coordenada) )

if __name__ == '__main__':
    run()
