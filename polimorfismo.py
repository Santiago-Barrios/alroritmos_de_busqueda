class Persona:

    def __init__(self, nombre):
        self.nombre = nombre

    def avanza(self):
        print('Ando caminando')


class Ciclista(Persona):

    def __init__(self, nombre):
        super().__init__(nombre)

    def avanza(self):
        print('Ando pedaleando')

def run():
    persona = Persona(nombre='Santiago')
    persona.avanza()

    ciclista = Ciclista(nombre = 'Daniel')
    ciclista.avanza()


if __name__ == '__main__':
    run()