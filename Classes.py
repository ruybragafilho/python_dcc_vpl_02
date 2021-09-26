
# Definição da classe Conta
class Conta:

    # Inicializador da classe Conta
    def __init__( self, numero ):

        self.__numero = numero
        self.__saldo = 0.0


    # get numero
    @property
    def numero( self ):
        return self.__numero

    # get saldo
    @property
    def saldo( self ):
        return self.__saldo       


    # set numero
    @numero.setter
    def numero( self, numero ):
        self.__numero = numero        

    # set saldo
    @saldo.setter
    def saldo( self, saldo ):
        self.__saldo = saldo


    # Método depositar
    def depositar( self, valor ):
        self.saldo += valor

    # Método sacar
    def sacar( self, valor ):
        self.saldo -= valor

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

    # set taxa
    @taxa.setter
    def taxa( self, taxa ):
        self.__taxa = taxa


    # metodo cobrar taxa
    def cobrar_taxa( self ):
        self.saldo -= self.taxa

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

    # set juros
    @juros.setter
    def juros( self, juros ):
        self.__juros = juros


    # Metodo aplicar_Juros
    def aplicar_juros( self ):

        self.saldo = self.saldo * (1 + self.juros)

# Fim da definição da classe ContaPoupanca