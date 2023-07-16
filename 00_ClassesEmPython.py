#Praticando algumas Class em python 

class Conta:
    def __init__(self,numero,titular, saldo, limite): #Metodo de Inicialização
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        
        """  Dessa	maneira,	garantimos	que toda	instância	de	uma		Conta	
        tenha	os	atributos	que	definimos. """
        
        """	métodos	-	do	ponto	de	vista	do	código,
        são	as funções	dentro	de	uma	classe."""
    def deposita(self, valor ):
        self.saldo +=valor
        
    def sacar(self, valor):
        self.saldo -=valor
        
    def extrato(self):
        print("\n Numero: {} \n saldo: {}".format(self.numero, self.saldo))
        
        
        
conta = Conta('123-4', 'Allanyo', 120.0, 1000.0)
conta.deposita(20.0)
conta.extrato()