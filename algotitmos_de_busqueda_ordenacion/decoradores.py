class CasillaDeVotacion:

    def __init__(self, identificador, pais):
        self._identificador = identificador
        self._pais = pais
        self._region = None

    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, region):
        if region in self._pais:
            self._region = region
        else:
            raise ValueError(f'La región {region} no es valida en {self._pais} ')

def run():
    casilla = CasillaDeVotacion(123, ['Popayán', 'Cali'])
    print(casilla.region)
    casilla.region = 'Popayán'
    print(casilla.region)
    casilla.region = 'Tulua'
    print(casilla.region)

if __name__ == '__main__':
    run()