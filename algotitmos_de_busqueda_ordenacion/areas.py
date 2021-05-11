import math

def square(side):
    area = side * side
    return area


def triangule(base, height):
    area = (base * height)/2
    return area

def circle(radius):
    area = math.pi * (radius**2)
    return area

def run():
    print("""
    Choose between the next options for getting the area 
    of the geametrical shape that you want:

    1. square
    2. Triangule
    3. circle

    """)
    opc = int(input( 'what is your option: '))

    if opc == 1:

        side = int(input('register the side of the square: '))
        area_square = square(side)
        print( 'the area of the square is = ' + str(area_square))

    elif opc == 2:

        base = int(input('register the base of the triangule: '))
        height = int(input('register the height of the triangule: '))
        area_trinagule = triangule( base, height )
        print(f'the area of the triangule is = {area_trinagule}')

    elif opc == 3:

        radius = int(input('register the circle radius: '))
        area_circle = circle( radius )
        print(f'The circle area is  = {area_circle}')

    else:
        print('You chose an invalid opcion, try again')


 
if __name__ == '__main__':
    run()