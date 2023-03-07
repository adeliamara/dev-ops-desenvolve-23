from listas_and_polimorfismo import ContaCorrente

class ContaSalario:
    def __init__(self, codigo):
        self.__codigo = codigo
        self.__saldo = 0
        
    def __eq__(self, __o: object) -> bool:
        if not isinstance(__o, ContaSalario):
            return False
        return self.__codigo == __o.__codigo
        
    def deposita(self, valor):
        self.__saldo += valor
        
    def __str__(self):
        return "[>>Codigo {} saldo {}<<]".format(self.__codigo, self.__saldo)
    
    
    
    
conta1 = ContaSalario(1)
conta1.deposita(100)
print(conta1)

conta2 = ContaSalario(1)
print(conta2)
conta3 = ContaCorrente(1)
print(conta3)
print(conta1.__eq__(conta2))
print(conta1.__eq__(conta3))