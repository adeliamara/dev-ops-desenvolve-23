from abc import ABCMeta, abstractclassmethod

class Conta(metaclass=ABCMeta):
    
    def __init__(self, codigo):
        self.__codigo = codigo
        self.__saldo = 0
        
    def deposita(self, valor):
        self.__saldo += valor
    
    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self.__codigo, self.__saldo)
    
    def get_saldo(self):
        return self.__saldo
    
    @abstractclassmethod
    def passa_o_mes(self):
        pass

    
class ContaCorrente(Conta):
    
    def passa_o_mes(self):
        self.deposita(-2)
        
        
class ContaPoupanca(Conta):
    
    def passa_o_mes(self):
        saldo_atual = self.get_saldo()
        rendimento = saldo_atual * 0.1
        self.deposita(rendimento - 3)
        
class ContaInvestimento(Conta):
    pass
        
contaTeste1 = ContaCorrente(1)
contaTeste1.deposita(1000)
contaTeste2 = ContaCorrente(2)
contaTeste2.deposita(2000)
contaTeste3 = ContaPoupanca(3)
contaTeste3.deposita(3000)
#contaTeste4 = ContaInvestimento(3)
#contaTeste4.deposita(3000)

contas = [contaTeste1, contaTeste2, contaTeste3]

for conta in contas:
    conta.passa_o_mes()#duck typing
    print(conta)

