
# Definição da classe Conta
class Conta:

    # Inicializador da classe Conta
    def __init__( self, numero ):

        self.__numero = numero
        self._saldo = 0.0


    # get saldo
    @property
    def saldo( self ):
        return self._saldo       


    # Método depositar
    def depositar( self, valor ):

        self._saldo += valor


    # Método sacar
    def sacar( self, valor ):

        self._saldo -= valor

# Fim da definição da classe Conta



# Definição da classe ContaCorrente
class ContaCorrente( Conta ):

    # Inicializador da classe ContaCorrente
    def __init__( self, numero, taxa ):

        super().__init__( numero )
        self.__taxa = taxa   


    # get taxa
    @property
    def taxa( self ):
        return self.__taxa            


    # metodo cobrar taxa
    def cobrar_taxa( self ):
        self._saldo -= self.__taxa

# Fim da definição da classe ContaCorrente



# Definição da classe ContaPoupanca
class ContaPoupanca( Conta ):

    # Inicializador da classe ContaPoupanca
    def __init__( self, numero, juros ):

        super().__init__( numero )
        self.__juros = juros    


    # get juros
    @property
    def juros( self ):
        return self.__juros    


    # Metodo aplicar_Juros
    def aplicar_juros( self ):

        self._saldo = self._saldo * (1 + self.juros)

# Fim da definição da classe ContaPoupanca